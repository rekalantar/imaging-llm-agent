from __future__ import annotations
from pathlib import Path
from typing import Dict, Any, List
from .io import ensure_parent, ensure_dir

SUPPORTED_ORGANS = {"liver", "spleen", "kidneys", "lungs", "heart"}
def segment_oars(image_path: str, output_dir: str, organs: List[str] | None = None) -> Dict[str, Any]:
    ensure_dir(output_dir)

    if organs is None:
        organs = list(SUPPORTED_ORGANS)

    outputs = {}
    for organ in organs:
        out_path = str(Path(output_dir) / f"{organ}_mask.nii.gz")
        # Path(out_path).write_text(f"STUB {organ} mask from {image_path}\n")
        outputs[organ] = out_path
    return {"outputs": outputs, "backend": "stub"}
