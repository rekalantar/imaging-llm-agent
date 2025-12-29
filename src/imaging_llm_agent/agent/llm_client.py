from __future__ import annotations
import os
from dataclasses import dataclass
from openai import OpenAI

@dataclass(frozen=True)
class LLMConfig:
    provider: str
    base_url: str | None
    api_key: str | None
    model: str

def load_llm_config() -> LLMConfig:
    provider = os.environ.get("LLM_PROVIDER", "lmstudio").lower()

    if provider in ("lmstudio", "ollama"):
        base_url = os.environ.get("LLM_BASE_URL")
        if not base_url:
            raise ValueError("LLM_BASE_URL must be set for lmstudio/ollama (e.g. http://localhost:1234/v1)")
        api_key = os.environ.get("LLM_API_KEY", "not-needed")
        model = os.environ.get("LLM_MODEL", "local-model")
        return LLMConfig(provider=provider, base_url=base_url, api_key=api_key, model=model)

    if provider == "openai":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY must be set when LLM_PROVIDER=openai")
        model = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")
        return LLMConfig(provider=provider, base_url=None, api_key=api_key, model=model)

    raise ValueError(f"Unknown LLM_PROVIDER={provider}. Use: lmstudio | ollama | openai")

def make_openai_client(cfg: LLMConfig) -> OpenAI:
    if cfg.base_url:
        return OpenAI(base_url=cfg.base_url, api_key=cfg.api_key)
    return OpenAI(api_key=cfg.api_key)
