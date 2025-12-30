from __future__ import annotations
import json
import re
from .schema import Plan
from .llm_client import load_llm_config, make_openai_client

SYSTEM_PROMPT = """You are an imaging workflow router.

Return ONLY valid JSON and commentary.

JSON format:
{
  "calls": [{"tool": "...", "args": {...}}],
  "notes": "..."
}

Allowed tools (tool field must be exactly one of):
- "segment_oars"  args: {"image_path": "...", "output_dir": "...", "organs": ["..."]}
- "register_rigid"  args: {"fixed_path": "...", "moving_path": "...", "output_dir": "..."}
- "register_deformable"  args: {"fixed_path": "...", "moving_path": "...", "output_dir": "..."}

Rules:
- If required paths are missing: return {"calls": [], "notes": "Missing ..."}.
- Never invent file paths.
- Prefer segment_oars when multiple organs requested.
"""

def _extract_json(text: str) -> str:
    # Prefer whole-string JSON
    t = text.strip()
    if t.startswith("{") and t.endswith("}"):
        return t

    # Fallback: extract first {...} block
    m = re.search(r"\{.*\}", t, flags=re.DOTALL)
    if not m:
        raise ValueError(f"LLM did not return JSON. Got: {text[:2000]}")
    return m.group(0)

def make_plan(user_text: str) -> Plan:
    cfg = load_llm_config()
    client = make_openai_client(cfg)

    resp = client.chat.completions.create(
        model=cfg.model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text},
        ],
        temperature=0.0,
        # IMPORTANT: LM Studio seems picky about response_format;
        # use plain text mode and validate ourselves.
        response_format={"type": "text"},
    )

    content = resp.choices[0].message.content
    json_str = _extract_json(content)
    return Plan.model_validate(json.loads(json_str))
