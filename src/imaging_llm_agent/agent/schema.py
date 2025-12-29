from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Dict, Any, List, Literal, Optional

ToolName = Literal["segment_oars", "register_ants_rigid", "register_torch_deformable"]

class ToolCall(BaseModel):
    tool: ToolName
    args: Dict[str, Any] = Field(default_factory=dict)

class Plan(BaseModel):
    calls: List[ToolCall] = Field(default_factory=list)
    notes: Optional[str] = None

class RunRequest(BaseModel):
    text: str
