from __future__ import annotations
import json
import logging
from .schema import Plan
from .llm_client import load_llm_config, make_openai_client

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are an imaging workflow router.

Return ONLY valid JSON matching this schema:
{ "calls": [ {"tool": "...", "args": {...}} ], "notes": "..." }

Tools:
- segment_oars(image_path, organs, output_dir)
- register_ants_rigid(fixed_path, moving_path, output_dir)

Rules:
- If required paths are missing, return {"calls": [], "notes": "...missing..."}.
- Never invent file paths.
- Prefer segment_oars when multiple organs are requested.
"""

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
        response_format={"type": "json_object"},
    )
    content = resp.choices[0].message.content
    plan_dict = json.loads(content)
    return Plan.model_validate(plan_dict)
