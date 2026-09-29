"""OpenAI Responses API adapter."""
import os
from functools import lru_cache


@lru_cache(maxsize=1)
def client():
    from openai import OpenAI
    return OpenAI(max_retries=0, timeout=600)


def generate(prompt, system, model, max_tokens=16000):
    response = client().responses.create(
        model=model, instructions=system, input=prompt,
        max_output_tokens=max_tokens,
        reasoning={"effort": os.getenv("STRATEGY_REASONING_EFFORT") or "medium"},
        store=False,
    )
    if response.status != "completed":
        raise RuntimeError(f"OpenAI response did not complete: {response.status}")
    text = response.output_text.strip()
    if not text:
        raise RuntimeError("OpenAI returned no text")
    return text
