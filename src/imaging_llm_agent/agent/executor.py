from __future__ import annotations
from typing import Any, Dict, List
from .schema import Plan
from ..tools.registry import TOOL_REGISTRY

def execute_plan(plan: Plan) -> Dict[str, Any]:
    results: List[Dict[str, Any]] = []
    for call in plan.calls:
        fn = TOOL_REGISTRY.get(call.tool)
        if fn is None:
            results.append({"tool": call.tool, "ok": False, "error": "Unknown tool"})
            continue
        try:
            out = fn(**call.args)
            results.append({"tool": call.tool, "ok": True, "output": out})
        except Exception as e:
            results.append({"tool": call.tool, "ok": False, "error": str(e)})
    return {"notes": plan.notes, "results": results}
