import contextlib
import io
import json
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace as NS
import unittest
from unittest.mock import patch

import run
from llm import ModelRouter, anthropic_client, openai_client


class RoutingTests(unittest.TestCase):
    def test_v1_ignores_hybrid_settings(self):
        with patch.dict(os.environ, {"CONTENT_MODEL": "legacy", "STRATEGY_MODEL": "new"}, clear=True):
            router = ModelRouter("v1", "style")
            self.assertEqual(set(router.routes.values()), {("anthropic", "legacy")})

    def test_hybrid_routing_and_missing_key(self):
        with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test"}, clear=True):
            router = ModelRouter("hybrid", "style")
            with self.assertRaisesRegex(ValueError, "OPENAI_API_KEY"):
                router.validate()
            with patch.dict(os.environ, {"OPENAI_API_KEY": "test"}):
                router.validate()
            self.assertEqual(router.routes['writer'][0], 'anthropic')
            self.assertEqual(router.routes['editor'][0], 'openai')
            with patch.object(openai_client, 'generate', return_value='strategy') as call:
                self.assertEqual(router.generate('strategy', 'input'), 'strategy')
                call.assert_called_once_with('input', 'style', 'gpt-5.6-sol', 16000)

    def test_retries_only_transient_errors(self):
        with patch.dict(os.environ, {}, clear=True):
            router = ModelRouter('v1', 'style')
        transient = Exception('not printed'); transient.status_code = 429
        with patch.object(anthropic_client, 'generate', side_effect=[transient, 'ok']) as call, patch('llm.time.sleep'):
            self.assertEqual(router.generate('writer', 'prompt'), 'ok')
            self.assertEqual(call.call_count, 2)
        auth = Exception('not printed'); auth.status_code = 401
        with patch.object(anthropic_client, 'generate', side_effect=auth) as call:
            with self.assertRaises(Exception):
                router.generate('writer', 'prompt')
            self.assertEqual(call.call_count, 1)

    def test_adapters_reject_incomplete_or_empty_text(self):
        with patch.object(openai_client, 'client') as client:
            for status, text in [('incomplete', 'partial'), ('completed', '')]:
                client.return_value.responses.create.return_value = NS(status=status, output_text=text)
                with self.assertRaises(RuntimeError):
                    openai_client.generate('input', 'style', 'model')
            client.return_value.responses.create.return_value = NS(status='completed', output_text=' final ')
            self.assertEqual(openai_client.generate('input', 'style', 'model'), 'final')
            self.assertFalse(client.return_value.responses.create.call_args.kwargs['store'])
        with patch.object(anthropic_client, 'client') as client:
            client.return_value.messages.create.return_value = NS(stop_reason='max_tokens', content=[])
            with self.assertRaises(RuntimeError):
                anthropic_client.generate('input', 'style', 'model')
            client.return_value.messages.create.return_value = NS(stop_reason='end_turn', content=[NS(type='text', text='final')])
            self.assertEqual(anthropic_client.generate('input', 'style', 'model'), 'final')

    def test_hybrid_requires_isolated_empty_directory(self):
        with TemporaryDirectory() as tmp, patch.object(ModelRouter, 'validate'), contextlib.redirect_stderr(io.StringIO()):
            nonempty=Path(tmp)/'used'; nonempty.mkdir(); (nonempty/'keep').write_text('existing')
            for extra in [[], ['--output-dir', str(run.ROOT/'output'/'test')], ['--output-dir', str(run.ROOT/'samples'/'test')], ['--output-dir', str(nonempty)]]:
                with patch('sys.argv', ['run.py','--profile','hybrid']+extra), self.assertRaises(SystemExit):
                    run.main()
            self.assertEqual((nonempty/'keep').read_text(), 'existing')

    def test_full_pipeline_for_both_profiles(self):
        # Exercise all stages with actual prompts/calendar and mocked provider responses.
        source=run.ROOT/'output'/'2026-08'
        for profile in ('v1','hybrid'):
            seen=[]
            rounds={}
            def generate(router, role, prompt, label='', max_tokens=16000):
                seen.append((role,label))
                if label in ('strategic-brief','creative-brief','calendar'):
                    file={'strategic-brief':'1-strategic-brief.md','creative-brief':'2-creative-brief.md','calendar':'3-calendar.md'}[label]
                    return (source/file).read_text()
                if label.startswith('qc-'):
                    rounds[label]=rounds.get(label,0)+1
                    fail=label=='qc-01' and rounds[label]==1
                    return '```json\n'+json.dumps({'verdict':'FAIL' if fail else 'PASS','checks':{},'verify_flags':[],'edit_notes':'revise'})+'\n```'
                return '# Finished test post\n'
            with TemporaryDirectory() as tmp, patch.object(ModelRouter,'validate'), patch.object(ModelRouter,'generate',generate), contextlib.redirect_stdout(io.StringIO()):
                out=Path(tmp)/'result'
                argv=['run.py','--profile',profile,'--month','2026-08','--corpus',str(source/'0-corpus.md'),'--output-dir',str(out)]
                with patch('sys.argv',argv):
                    run.main()
                self.assertEqual(len(list((out/'posts').glob('*.md'))),15)
                self.assertIn('15/15 posts passed', (out/'5-qc-report.md').read_text())
                self.assertIn(('writer','rewrite-01'),seen)
                self.assertTrue(all(role=='strategy' for role,label in seen if label in ('strategic-brief','creative-brief','calendar')))
                self.assertTrue(all(role=='editor' for role,label in seen if label.startswith('qc-')))
                if profile=='v1':
                    seen.clear()
                    with patch('sys.argv',argv+['--from-stage','4']):
                        run.main()
                    self.assertEqual(seen,[])


if __name__ == '__main__':
    unittest.main()
