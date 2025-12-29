from __future__ import annotations
from typing import Callable, Dict
from .segmentation import segment_oars
from .registration import register_ants_rigid

TOOL_REGISTRY: Dict[str, Callable] = {
    "segment_oars": segment_oars,
    "register_ants_rigid": register_ants_rigid,
}
