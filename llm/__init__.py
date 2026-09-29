"""Role-based provider routing; v1 keeps every role on Claude."""
import os
import time

from . import anthropic_client, openai_client


class ModelRouter:
    def __init__(self, profile, system):
        if profile not in ("v1", "hybrid"):
            raise ValueError(f"Unknown profile: {profile}")
        self.system = system
        legacy = os.getenv("CONTENT_MODEL") or "claude-opus-4-8"
        if profile == "v1":
            self.routes = {r: ("anthropic", legacy) for r in ("strategy", "writer", "editor")}
        else:
            strategy = os.getenv("STRATEGY_MODEL") or "gpt-5.6-sol"
            self.routes = {
                "strategy": (os.getenv("STRATEGY_PROVIDER") or "openai", strategy),
                "writer": (os.getenv("DRAFTING_PROVIDER") or "anthropic",
                           os.getenv("DRAFTING_MODEL") or legacy),
                "editor": (os.getenv("EDITOR_PROVIDER") or "openai",
                           os.getenv("EDITOR_MODEL") or strategy),
            }

    def validate(self):
        for provider, model in self.routes.values():
            if provider not in ("openai", "anthropic"):
                raise ValueError(f"Unsupported provider: {provider}")
            key = "OPENAI_API_KEY" if provider == "openai" else "ANTHROPIC_API_KEY"
            if not os.getenv(key):
                raise ValueError(f"{key} is not set")
            if not model.strip():
                raise ValueError("Model must not be empty")

    def describe(self):
        return ", ".join(f"{role}={provider}/{model}"
                         for role, (provider, model) in self.routes.items())

    def generate(self, role, prompt, label="", max_tokens=16000):
        provider, model = self.routes[role]
        adapter = openai_client if provider == "openai" else anthropic_client
        for attempt in range(5):
            try:
                return adapter.generate(prompt, self.system, model, max_tokens)
            except Exception as exc:
                # Retry transient transport/rate/server errors, never auth or bad requests.
                if getattr(exc, "code", None) in {
                    "insufficient_quota", "credit_balance_exhausted",
                    "organization_spend_limit_exceeded", "project_spend_limit_exceeded",
                    "organization_usage_limit_exceeded",
                }:
                    raise
                status = getattr(exc, "status_code", None)
                transient = status in (408, 409, 429) or (status is not None and status >= 500)
                transient = transient or type(exc).__name__ in ("APIConnectionError", "APITimeoutError")
                if not transient or attempt == 4:
                    raise
                wait = 20 * (attempt + 1)
                print(f"  [{label}] {type(exc).__name__}; retrying in {wait}s")
                time.sleep(wait)
