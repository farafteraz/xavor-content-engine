"""Minimal live connectivity checks. Never print keys, responses, or error bodies."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from llm import ModelRouter

router = ModelRouter("hybrid", "Follow the user's instruction exactly.")
router.validate()
failed = False
for role in ("strategy", "writer"):
    provider, model = router.routes[role]
    try:
        text = router.generate(role, "Reply with exactly OK.", "connection-check", max_tokens=512)
        if text.strip().rstrip(".") != "OK":
            raise RuntimeError("Unexpected response")
        print(f"PASS: {provider}/{model}")
    except Exception as exc:
        failed = True
        print(f"FAIL: {provider}/{model}: {type(exc).__name__}; HTTP {getattr(exc, 'status_code', 'n/a')}")
sys.exit(1 if failed else 0)
