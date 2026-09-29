"""Anthropic adapter, loaded only when selected."""
from functools import lru_cache


@lru_cache(maxsize=1)
def client():
    import anthropic
    return anthropic.Anthropic(max_retries=0, timeout=600)


def generate(prompt, system, model, max_tokens=16000):
    response = client().messages.create(
        model=model, max_tokens=max_tokens, system=system,
        messages=[{"role": "user", "content": prompt}],
    )
    if response.stop_reason != "end_turn":
        raise RuntimeError(f"Anthropic response stopped: {response.stop_reason}")
    text = "".join(b.text for b in response.content if b.type == "text").strip()
    if not text:
        raise RuntimeError("Anthropic returned no text")
    return text
