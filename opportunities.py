"""Opt-in v2 opportunity review. Never calls the calendar or writing pipeline."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
from datetime import datetime, timezone

import yaml

from llm import ModelRouter

ROOT = Path(__file__).resolve().parent
PROMPTS = ROOT / 'prompts' / 'opportunities'
DIMENSIONS = ('relevance', 'originality', 'evidence', 'commercial_value', 'buyer_depth')


def require(condition, message):
    if not condition:
        raise ValueError(message)


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    result = {}
    for key, value in node.value:
        key = loader.construct_object(key, deep=deep)
        require(key not in result, f'Duplicate YAML key: {key}')
        result[key] = loader.construct_object(value, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def read_yaml(path):
    return yaml.load(path.read_text(), Loader=UniqueLoader)


def indexed(records):
    result = {record['id']: record for record in records}
    require(len(result) == len(records), 'Duplicate record IDs')
    return result


def load_inputs(corpus, month, baseline):
    require(re.fullmatch(r'\d{4}-(0[1-9]|1[0-2])', month), 'Month must be YYYY-MM')
    strategy = read_yaml(ROOT / 'strategy/marketing-strategy.yml')
    offers = read_yaml(ROOT / 'knowledge/offers.yml')
    proof = read_yaml(ROOT / 'knowledge/proof.yml')
    offer_ids = set(indexed(offers['offerings']))
    capabilities = indexed(proof['capabilities'])
    cases = indexed(proof['cases'])
    for group in strategy['commercial_direction'].values():
        if isinstance(group, dict):
            require(set(group.get('offering_ids', [])) <= offer_ids, 'Unknown strategy offering')
    for record in list(capabilities.values()) + list(cases.values()):
        require(set(record['offer_refs'] + record.get('related_offer_refs', [])) <= offer_ids,
                'Unknown proof offering')
    for offer in offers['offerings']:
        require(set(offer['capability_refs']) <= set(capabilities), 'Unknown capability reference')
        require(set(offer['proof_refs'] + offer['related_proof_refs']) <= set(cases), 'Unknown case reference')
    text = corpus.read_text()
    require(text.strip(), 'Corpus is empty')
    # Paragraph IDs preserve original wording without an LLM-generated evidence summary.
    chunks = {f'C{i:04d}': value for i, value in enumerate(re.split(r'\n\s*\n', text), 1) if value.strip()}
    expected = ['1-strategic-brief.md', '2-creative-brief.md', '3-calendar.md',
                'posts/01-article.md', 'posts/03-explainer-reel.md', 'posts/06-carousel.md',
                'posts/07-video-feature.md', 'posts/11-static.md']
    baseline_files = {name: (baseline / name).read_text() for name in expected}
    return {
        'month': month, 'strategy': strategy, 'offers': offers, 'proof': proof,
        'corpus': chunks, 'corpus_sha256': hashlib.sha256(corpus.read_bytes()).hexdigest(),
        'history': {'status': 'unknown', 'note': 'Generated v1 outputs are not confirmed published history.'},
        'baseline': {'status': 'generated_control_sample_not_publication_history', 'files': baseline_files},
    }


def parse_json(text):
    text = text.strip()
    if text.startswith('```json') and text.endswith('```'):
        text = text[len('```json'):-3].strip()
    def no_duplicates(pairs):
        out = {}
        for key, value in pairs:
            require(key not in out, f'Duplicate JSON key: {key}')
            out[key] = value
        return out
    return json.loads(text, object_pairs_hook=no_duplicates)


def fields(obj, names, label):
    require(isinstance(obj, dict), f'{label} must be an object')
    require(set(obj) == set(names), f'{label} must have exactly: {", ".join(names)}')


def string(value, label):
    require(isinstance(value, str) and bool(value.strip()), f'{label} must be nonempty text')


def strings(value, label, allow_empty=False):
    require(isinstance(value, list) and (allow_empty or bool(value)), f'{label} must be a list')
    for item in value:
        string(item, label)


def validate_candidates(data, inputs):
    fields(data, ['opportunities'], 'Generator result')
    candidates = data['opportunities']
    require(isinstance(candidates, list) and 1 <= len(candidates) <= 10, 'Expected 1–10 opportunities')
    ids = set()
    offers = indexed(inputs['offers']['offerings'])
    cases = indexed(inputs['proof']['cases'])
    capabilities = indexed(inputs['proof']['capabilities'])
    text_fields = ['id', 'title', 'thesis', 'primary_reader', 'business_decision', 'technical_decision',
                   'why_now', 'why_xavor', 'next_step']
    for candidate in candidates:
        fields(candidate, text_fields + ['alternatives', 'offering_ids', 'evidence', 'unknowns'], 'Opportunity')
        for key in text_fields:
            string(candidate[key], key)
        require(re.fullmatch(r'O\d{2}', candidate['id']), 'Opportunity ID must be O01, O02, etc.')
        require(candidate['id'] not in ids, 'Duplicate opportunity ID')
        ids.add(candidate['id'])
        for key in ['alternatives', 'offering_ids', 'unknowns']:
            strings(candidate[key], key, allow_empty=(key == 'unknowns'))
        require(len(candidate['alternatives']) >= 2, 'Compare at least two approaches')
        require(set(candidate['offering_ids']) <= set(offers), 'Unknown opportunity offering')
        evidence = candidate['evidence']
        require(isinstance(evidence, list) and evidence, 'Evidence is required')
        kinds = set()
        for item in evidence:
            fields(item, ['kind', 'ref', 'claim', 'basis', 'quote'], 'Evidence')
            require(item['kind'] in ('corpus', 'case', 'capability'), 'Unknown evidence kind')
            require(item['basis'] in ('source_report', 'inference'), 'Label reports versus inference')
            string(item['claim'], 'Evidence claim')
            string(item['ref'], 'Evidence reference')
            string(item['quote'], 'Evidence quote')
            kinds.add(item['kind'])
            if item['kind'] == 'corpus':
                require(item['ref'] in inputs['corpus'], 'Unknown corpus reference')
                source = inputs['corpus'][item['ref']]
            else:
                collection = cases if item['kind'] == 'case' else capabilities
                require(item['ref'] in collection, 'Unknown library reference')
                record = collection[item['ref']]
                source = json.dumps(record, ensure_ascii=False)
                linked = record['offer_refs'] + record.get('related_offer_refs', [])
                require(set(candidate['offering_ids']) & set(linked), 'Evidence unrelated to selected offerings')
            require(len(item['quote']) >= 15 and item['quote'] in source, 'Evidence quote must match its source')
        require('corpus' in kinds and bool(kinds & {'case', 'capability'}),
                'Each opportunity needs a corpus signal and Xavor evidence')
    return candidates


def validate_critique(data, candidates, inputs):
    fields(data, ['reviews', 'baseline_comparison', 'history_limit'], 'Critic result')
    string(data['history_limit'], 'History limitation')
    require(isinstance(data['reviews'], list), 'Reviews must be a list')
    by_id = {x['id']: x for x in candidates}
    seen = set()
    for review in data['reviews']:
        fields(review, ['id', 'decision', 'scores', 'reason', 'required_changes', 'evidence_checks'], 'Review')
        require(review['id'] in by_id and review['id'] not in seen, 'Unknown or duplicate review ID')
        seen.add(review['id'])
        require(review['decision'] in ('keep', 'revise', 'reject'), 'Unknown critic decision')
        string(review['reason'], 'Review reason')
        strings(review['required_changes'], 'Required changes', allow_empty=True)
        fields(review['scores'], DIMENSIONS, 'Scores')
        require(all(type(v) is int and 1 <= v <= 5 for v in review['scores'].values()), 'Scores must be integers 1–5')
        evidence = by_id[review['id']]['evidence']
        checks = review['evidence_checks']
        require(isinstance(checks, list) and len(checks) == len(evidence), 'Review every evidence item')
        indices = set()
        for check in checks:
            fields(check, ['index', 'status', 'reason'], 'Evidence check')
            require(type(check['index']) is int and 0 <= check['index'] < len(evidence), 'Invalid evidence index')
            require(check['index'] not in indices, 'Duplicate evidence check')
            indices.add(check['index'])
            require(check['status'] in ('supported', 'qualified', 'unsupported'), 'Invalid evidence status')
            string(check['reason'], 'Evidence-check reason')
        if review['decision'] == 'keep':
            require(all(x['status'] == 'supported' for x in checks), 'Cannot keep unresolved evidence')
            require(not review['required_changes'], 'Cannot keep required changes')
            require(not by_id[review['id']]['unknowns'], 'Cannot keep unresolved factual prerequisites')
            require(min(review['scores'].values()) >= 3, 'Cannot keep a failing dimension')
        else:
            require(review['required_changes'], 'Explain remediation or reason to abandon')
    require(seen == set(by_id), 'Critic omitted opportunities')
    comparison = data['baseline_comparison']
    fields(comparison, ['assessment', 'observations'], 'Baseline comparison')
    string(comparison['assessment'], 'Comparison assessment')
    require(isinstance(comparison['observations'], list) and comparison['observations'], 'Comparison observations required')
    for item in comparison['observations']:
        fields(item, ['baseline_file', 'quote', 'opportunity_ids', 'finding'], 'Comparison observation')
        require(item['baseline_file'] in inputs['baseline']['files'], 'Unknown baseline file')
        string(item['quote'], 'Baseline quote')
        require(len(item['quote']) >= 15 and item['quote'] in inputs['baseline']['files'][item['baseline_file']],
                'Baseline comparison quote must match')
        strings(item['opportunity_ids'], 'Comparison opportunities')
        require(set(item['opportunity_ids']) <= set(by_id), 'Unknown compared opportunity')
        string(item['finding'], 'Comparison finding')
    return data


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def render_review(candidates, critique, inputs):
    lines = ['# V2 opportunity review', '', 'Status: awaiting human review. No calendar or posts were generated.',
             '', 'Scores are model judgments, not measured business outcomes.',
             'Published-content history is unknown. The v1 control sample contains generated outputs.', '']
    reviews = {r['id']: r for r in critique['reviews']}
    cases = indexed(inputs['proof']['cases']); caps = indexed(inputs['proof']['capabilities'])
    for decision, heading in [('keep', 'Recommended for review'), ('revise', 'Needs revision'), ('reject', 'Rejected')]:
        lines += [f'## {heading}', '']
        selected = [x for x in candidates if reviews[x['id']]['decision'] == decision]
        if not selected:
            lines += ['None.', '']
        for item in selected:
            review = reviews[item['id']]
            lines += [f"### {item['id']}: {item['title']}", '', item['thesis'], '',
                      f"Primary reader: {item['primary_reader']}", '',
                      f"Business decision: {item['business_decision']}", '',
                      f"Technical decision: {item['technical_decision']}", '',
                      'Approaches to evaluate: ' + '; '.join(item['alternatives']), '',
                      f"Why now: {item['why_now']}", '', f"Xavor connection: {item['why_xavor']}", '',
                      f"Critic: {review['reason']}", '',
                      'Scores (1–5): ' + ', '.join(f'{k}: {v}' for k, v in review['scores'].items()), '',
                      'Evidence:', '']
            checks = {x['index']: x for x in review['evidence_checks']}
            for index, evidence in enumerate(item['evidence']):
                ref = evidence['ref']
                if evidence['kind'] == 'corpus':
                    link = f'[{ref}](corpus.md#{ref.lower()})'
                else:
                    record = (cases if evidence['kind'] == 'case' else caps)[ref]
                    link = f"[{ref}]({record['source_url']})"
                check = checks[index]
                lines += [f"- {link} ({evidence['basis']}, {check['status']}): {evidence['claim']} {check['reason']}"]
            lines += ['', 'Unresolved prerequisites: ' + ('; '.join(item['unknowns']) or 'None identified by the generator.'), '',
                      'Required changes: ' + ('; '.join(review['required_changes']) or 'None identified by the critic.'), '',
                      f"Proposed next step: {item['next_step']}", '']
    comparison = critique['baseline_comparison']
    lines += ['## Comparison with v1', '', comparison['assessment'], '']
    for item in comparison['observations']:
        lines += [f"- {item['baseline_file']} ({', '.join(item['opportunity_ids'])}): {item['finding']}",
                  f"  Baseline excerpt: {item['quote']}"]
    lines += ['', 'History limitation: ' + critique['history_limit'], '',
              '## Review gate', '', 'Choose which opportunities to approve, revise, or drop. Approval is not recorded automatically.',
              'This command has no calendar, drafting, publishing, or continuation stage.', '']
    return '\n'.join(lines)


def prepare_output(path):
    path = path.resolve()
    for protected in [ROOT / 'output', ROOT / 'samples', ROOT / 'strategy', ROOT / 'knowledge', ROOT / 'prompts', ROOT / 'brand', ROOT / '.git']:
        require(path != protected and protected not in path.parents, 'Output directory is protected')
    require(not path.exists() or (path.is_dir() and not any(path.iterdir())), 'Use a new, empty output directory')
    path.mkdir(parents=True, exist_ok=True)
    return path


def execute(inputs, out, router=None):
    manifest = {'schema_version': 1, 'status': 'prepared', 'month': inputs['month'],
                'created_at': datetime.now(timezone.utc).isoformat(), 'corpus_sha256': inputs['corpus_sha256'],
                'history_status': 'unknown', 'human_approval': None,
                'routes': {k: list(v) for k, v in router.routes.items() if k in ('strategy', 'editor')} if router else None}
    revision = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True, capture_output=True)
    manifest['code_revision'] = revision.stdout.strip() if revision.returncode == 0 else 'unknown'
    write_json(out / 'inputs.json', inputs)
    manifest['inputs_sha256'] = hashlib.sha256((out / 'inputs.json').read_bytes()).hexdigest()
    (out / 'corpus.md').write_text('\n\n'.join(f'## {key}\n\n{value}' for key, value in inputs['corpus'].items()))
    templates = {name: (PROMPTS / f'{name}.md').read_text() for name in ('system', 'generator', 'critic')}
    write_json(out / 'prompt-snapshot.json', templates)
    manifest['prompts_sha256'] = hashlib.sha256((out / 'prompt-snapshot.json').read_bytes()).hexdigest()
    write_json(out / 'manifest.json', manifest)
    if router is None:
        (out / 'PREPARED.md').write_text('# Inputs prepared\n\nNo model calls were made. No opportunities or critic findings have been generated.\n')
        return
    try:
        generator_inputs = {k: v for k, v in inputs.items() if k != 'baseline'}
        raw = router.generate('strategy', templates['generator'] + '\n\nINPUT DATA:\n' + json.dumps(generator_inputs, ensure_ascii=False), label='opportunities')
        (out / 'generator-response.txt').write_text(raw)
        data = parse_json(raw)
        candidates = validate_candidates(data, inputs)
        write_json(out / 'opportunities.json', data)
        raw = router.generate('editor', templates['critic'] + '\n\nINPUT DATA:\n' + json.dumps({'context': inputs, 'candidates': data}, ensure_ascii=False), label='opportunity-critic')
        (out / 'critic-response.txt').write_text(raw)
        critique = validate_critique(parse_json(raw), candidates, inputs)
        write_json(out / 'critique.json', critique)
        (out / 'review.md').write_text(render_review(candidates, critique, inputs))
        manifest['status'] = 'awaiting_human_review'
    except Exception as exc:
        manifest['status'] = 'failed'
        manifest['error_type'] = type(exc).__name__
        manifest['note'] = 'No approved output. Inspect saved stage responses locally; rerun into a new directory.'
        raise
    finally:
        write_json(out / 'manifest.json', manifest)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--month', required=True)
    parser.add_argument('--corpus', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--prepare-only', action='store_true', help='Validate and snapshot inputs without API calls')
    args = parser.parse_args()
    try:
        inputs = load_inputs(args.corpus, args.month, ROOT / 'samples/v1-baseline')
        # The preserved baseline is August. Other months need a separate comparison design.
        require(args.month == '2026-08', 'This comparison milestone uses August 2026')
        expected = ROOT / 'output/2026-08/0-corpus.md'
        require(inputs['corpus_sha256'] == hashlib.sha256(expected.read_bytes()).hexdigest(),
                'Comparison must use the unchanged August corpus')
        router = None
        if not args.prepare_only:
            env_file = ROOT / '.env'
            if env_file.exists():
                for line in env_file.read_text().splitlines():
                    if line.strip() and not line.lstrip().startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        os.environ.setdefault(key.strip(), value.strip().strip('\"\''))
            router = ModelRouter('hybrid', (PROMPTS / 'system.md').read_text())
            router.validate(roles=('strategy', 'editor'))
        out = prepare_output(args.output_dir)
        execute(inputs, out, router)
    except (ValueError, OSError, yaml.YAMLError) as exc:
        parser.error(str(exc))
    print(f"{'Prepared inputs without model calls' if args.prepare_only else 'Stopped for human review'}: {out}")


if __name__ == '__main__':
    main()
