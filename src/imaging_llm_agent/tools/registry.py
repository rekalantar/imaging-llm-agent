from __future__ import annotations
from typing import Callable, Dict
from .segmentation import segment_oars
from .registration import register_rigid, register_deformable

TOOL_REGISTRY: Dict[str, Callable] = {
    "segment_oars": segment_oars,
    "register_rigid": register_rigid,
    "register_deformable": register_deformable,
}
