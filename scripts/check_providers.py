"""Minimal live connectivity checks. Never print keys, responses, or error bodies."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from llm import ModelRouter, openai_client, anthropic_client

router = ModelRouter("hybrid", "Follow the user's instruction exactly.")
router.validate()
failed = False
for role in ("strategy", "writer"):
    provider, model = router.routes[role]
    try:
        adapter = openai_client if provider == "openai" else anthropic_client
        text = adapter.generate("Reply with exactly OK.", router.system, model, max_tokens=512)
        if text.strip().rstrip(".") != "OK":
            raise RuntimeError("Unexpected response")
        print(f"PASS: {provider}/{model}")
    except Exception as exc:
        failed = True
        print(f"FAIL: {provider}/{model}: {type(exc).__name__}; HTTP {getattr(exc, 'status_code', 'n/a')}")
        # Report only known error codes, never provider bodies or credentials.
        code = getattr(exc, "code", None)
        if code in {"insufficient_quota", "rate_limit_exceeded", "model_not_found", "invalid_api_key",
                    "credit_balance_exhausted", "organization_spend_limit_exceeded",
                    "project_spend_limit_exceeded", "organization_usage_limit_exceeded", "slow_down"}:
            print(f"Provider error code: {code}")
sys.exit(1 if failed else 0)
