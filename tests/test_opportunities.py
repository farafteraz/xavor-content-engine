import copy
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

import opportunities as op
from llm import ModelRouter


def fixture():
    inputs = op.load_inputs(op.ROOT / 'output/2026-08/0-corpus.md', '2026-08', op.ROOT / 'samples/v1-baseline')
    ref, text = next((k, v) for k, v in inputs['corpus'].items() if len(v) >= 30)
    case = inputs['proof']['cases'][0]
    data = {'opportunities': [{
        'id': 'O01', 'title': 'Fixture only', 'format': 'carousel', 'starting_point': 'xavor_experience', 'reader_value': 'A useful scoped lesson', 'thesis': 'A qualified test hypothesis.',
        'primary_reader': 'CTO', 'business_decision': 'Choose a deployment boundary.',
        'technical_decision': 'Evaluate hosted and local inference.',
        'alternatives': ['Local model with capacity constraints.', 'Hosted model with a different data boundary.'],
        'why_now': 'An attributed August signal.', 'why_xavor': 'Scoped implementation experience.',
        'next_step': 'Discuss constraints.', 'offering_ids': ['ai-use-case-development'], 'unknowns': [],
        'evidence': [
            {'kind': 'corpus', 'ref': ref, 'claim': 'Test source report.', 'basis': 'source_report', 'quote': text[:30]},
            {'kind': 'case', 'ref': case['id'], 'claim': 'Test scoped report.', 'basis': 'source_report', 'quote': case['reusable_claim']},
        ],
    }]}
    baseline_name = '2-creative-brief.md'
    critique = {
        'reviews': [{'id': 'O01', 'decision': 'keep', 'scores': dict.fromkeys(op.DIMENSIONS, 3),
                     'reason': 'Fixture judgment only.', 'required_changes': [], 'writer_notes': [],
                     'evidence_checks': [{'index': i, 'status': 'supported', 'impact': 'context', 'reason': 'Fixture scope check.'} for i in range(2)]}],
        'baseline_comparison': {'assessment': 'Fixture comparison only.', 'observations': [{
            'baseline_file': baseline_name, 'quote': inputs['baseline']['files'][baseline_name][:40],
            'opportunity_ids': ['O01'], 'finding': 'Fixture difference.'}]},
        'history_limit': 'Published history is unknown.',
    }
    return inputs, data, critique


class OpportunityTests(unittest.TestCase):
    def test_evidence_fails_closed(self):
        inputs, data, _ = fixture()
        mutations = [
            lambda c: c['offering_ids'].append('invented-offer'),
            lambda c: c['evidence'][0].update(ref='C9999'),
            lambda c: c['evidence'][0].update(quote='A fabricated supporting quotation.'),
            lambda c: c['evidence'][1].update(ref='invented-case'),
            lambda c: c.update(starting_point='external_signal', evidence=c['evidence'][1:]),
            lambda c: c.update(offering_ids=['plm-migration']),
            lambda c: c.update(calendar='Unrequested stage'),
        ]
        for mutate in mutations:
            bad = copy.deepcopy(data); mutate(bad['opportunities'][0])
            with self.subTest(mutation=mutate), self.assertRaises(ValueError):
                op.validate_candidates(bad, inputs)
        duplicate = copy.deepcopy(data); duplicate['opportunities'] *= 2
        with self.assertRaisesRegex(ValueError, 'Duplicate opportunity'):
            op.validate_candidates(duplicate, inputs)

    def test_keep_cannot_bypass_evidence_or_review(self):
        inputs, data, critique = fixture()
        candidates = op.validate_candidates(data, inputs)
        op.validate_critique(critique, candidates, inputs)
        changes = [
            lambda r: r['evidence_checks'][0].update(status='unsupported', impact='blocking'),
            lambda r: r['evidence_checks'][0].update(status='qualified', impact='blocking'),
            lambda r: r['scores'].update(originality=2),
            lambda r: r['scores'].update(evidence=True),
            lambda r: r['required_changes'].append('Verify a claim.'),
            lambda r: r['evidence_checks'].pop(),
            lambda r: r['evidence_checks'][1].update(index=0),
        ]
        for change in changes:
            bad = copy.deepcopy(critique); change(bad['reviews'][0])
            with self.subTest(change=change), self.assertRaises(ValueError):
                op.validate_critique(bad, candidates, inputs)
        candidates[0]['unknowns'] = ['Product availability']
        op.validate_critique(critique, candidates, inputs)  # Unused context is not a blocker.

    def test_every_candidate_and_baseline_quote_checked(self):
        inputs, data, critique = fixture()
        for key, value in [('quote', 'This is an invented baseline quote.'), ('baseline_file', 'invented.md'), ('opportunity_ids', ['O99'])]:
            bad = copy.deepcopy(critique); bad['baseline_comparison']['observations'][0][key] = value
            with self.assertRaises(ValueError):
                op.validate_critique(bad, data['opportunities'], inputs)
        critique['reviews'] = []
        with self.assertRaisesRegex(ValueError, 'omitted'):
            op.validate_critique(critique, data['opportunities'], inputs)

    def test_full_review_stops_without_writer_or_approval(self):
        inputs, data, critique = fixture()
        with TemporaryDirectory() as tmp:
            out = op.prepare_output(Path(tmp) / 'review')
            router = ModelRouter('hybrid', 'test')
            with patch.object(router, 'generate', side_effect=[json.dumps(data), json.dumps(critique)]) as call:
                op.execute(inputs, out, router)
            self.assertEqual([c.args[0] for c in call.call_args_list], ['strategy', 'editor'])
            self.assertNotIn('"baseline":', call.call_args_list[0].args[1])
            self.assertIn('"baseline":', call.call_args_list[1].args[1])
            manifest = json.loads((out / 'manifest.json').read_text())
            self.assertEqual(manifest['status'], 'awaiting_human_review')
            self.assertIsNone(manifest['human_approval'])
            self.assertIn('Recommended for review', (out / 'review.md').read_text())
            self.assertFalse((out / 'posts').exists())
            self.assertFalse((out / '3-calendar.md').exists())

    def test_reject_all_is_valid(self):
        inputs, data, critique = fixture()
        review = critique['reviews'][0]
        review.update(decision='reject', required_changes=['Abandon because no distinct buyer argument is established.'])
        review['scores']['originality'] = 1
        op.validate_critique(critique, data['opportunities'], inputs)
        result = op.render_review(data['opportunities'], critique, inputs)
        self.assertIn('## Recommended for review\n\nNone.', result)
        self.assertIn('## Rejected\n\n### O01', result)

    def test_partial_failure_keeps_diagnostics_and_no_review(self):
        inputs, data, _ = fixture()
        for responses in [['not json'], [json.dumps(data), '{"reviews": []}']]:
            with TemporaryDirectory() as tmp:
                out = op.prepare_output(Path(tmp) / 'failed')
                router = ModelRouter('hybrid', 'test')
                with patch.object(router, 'generate', side_effect=responses), self.assertRaises(ValueError):
                    op.execute(inputs, out, router)
                self.assertEqual(json.loads((out / 'manifest.json').read_text())['status'], 'failed')
                self.assertTrue((out / 'generator-response.txt').exists())
                self.assertFalse((out / 'review.md').exists())

    def test_prepare_only_needs_no_keys_or_calls(self):
        inputs, _, _ = fixture()
        with TemporaryDirectory() as tmp, patch.dict(os.environ, {}, clear=True), patch.object(ModelRouter, 'generate') as call:
            out = op.prepare_output(Path(tmp) / 'prepared')
            op.execute(inputs, out)
            call.assert_not_called()
            self.assertEqual(json.loads((out / 'manifest.json').read_text())['status'], 'prepared')
            self.assertFalse((out / 'opportunities.json').exists())

    def test_protected_nonempty_and_symlink_outputs(self):
        for name in ['output/test-v2', 'samples/test-v2', 'knowledge/test-v2', 'prompts/test-v2', '.git/test-v2']:
            with self.assertRaisesRegex(ValueError, 'protected'):
                op.prepare_output(op.ROOT / name)
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'existing').write_text('keep')
            with self.assertRaisesRegex(ValueError, 'empty'):
                op.prepare_output(root)
            (root / 'link').symlink_to(op.ROOT / 'samples', target_is_directory=True)
            with self.assertRaisesRegex(ValueError, 'protected'):
                op.prepare_output(root / 'link' / 'test-v2')
            self.assertEqual((root / 'existing').read_text(), 'keep')

    def test_only_active_roles_need_credentials(self):
        with patch.dict(os.environ, {'OPENAI_API_KEY': 'test'}, clear=True):
            router = ModelRouter('hybrid', 'test')
            router.validate(roles=('strategy', 'editor'))
            with self.assertRaisesRegex(ValueError, 'ANTHROPIC_API_KEY'):
                router.validate()

    def test_cli_enforces_same_month_and_corpus_before_calls(self):
        import contextlib
        import io
        with TemporaryDirectory() as tmp, patch.object(ModelRouter, 'generate') as call:
            corpus = Path(tmp) / 'corpus.md'
            corpus.write_text('Changed source for a comparison.')
            for month, source in [('2026-09', op.ROOT / 'output/2026-08/0-corpus.md'), ('2026-08', corpus)]:
                out = Path(tmp) / 'result'
                argv = ['opportunities.py', '--month', month, '--corpus', str(source), '--output-dir', str(out), '--prepare-only']
                with patch('sys.argv', argv), contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                    op.main()
                self.assertFalse(out.exists())
            call.assert_not_called()

    def test_evergreen_case_and_editorial_origins_need_no_news(self):
        inputs, data, _ = fixture()
        candidate = data['opportunities'][0]
        candidate.update(why_now='', technical_decision='', business_decision='', alternatives=[])
        candidate['evidence'] = candidate['evidence'][1:]
        op.validate_candidates(data, inputs)
        record = inputs['editorial_inputs']['records'][1]
        candidate.update(starting_point='buyer_question', evidence=[{
            'kind': 'editorial', 'ref': record['id'], 'claim': 'User-described buying dynamics.',
            'basis': 'source_report', 'quote': record['statement']}])
        op.validate_candidates(data, inputs)

    def test_keep_with_writer_note_and_open_context(self):
        inputs, data, critique = fixture()
        data['opportunities'][0]['unknowns'] = ['Client deployment requirements, not claimed in content.']
        review = critique['reviews'][0]
        review['evidence_checks'][0].update(status='qualified', impact='writer_note')
        review['writer_notes'] = ['Correct the incidental digest date.']
        op.validate_critique(critique, data['opportunities'], inputs)
        self.assertIn('Writer notes:', op.render_review(data['opportunities'], critique, inputs))
        review['evidence_checks'][0].update(impact='blocking')
        with self.assertRaisesRegex(ValueError, 'blocking'):
            op.validate_critique(critique, data['opportunities'], inputs)

    def test_competitive_gap_requires_observation_and_inference(self):
        inputs, data, _ = fixture()
        candidate = data['opportunities'][0]
        record = inputs['competitive_context']['records'][0]
        candidate.update(starting_point='competitive_gap', evidence=[{
            'kind': 'competitive', 'ref': record['id'], 'claim': 'Possible differentiation hypothesis.',
            'basis': 'inference', 'quote': record['statement']}])
        op.validate_candidates(data, inputs)
        candidate['evidence'][0]['basis'] = 'source_report'
        with self.assertRaisesRegex(ValueError, 'inference'):
            op.validate_candidates(data, inputs)

    def test_duplicate_keys_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate JSON'):
            op.parse_json('{"opportunities": [], "opportunities": []}')
        with self.assertRaisesRegex(ValueError, 'Duplicate YAML'):
            op.yaml.load('id: first\nid: second\n', Loader=op.UniqueLoader)


if __name__ == '__main__':
    unittest.main()
