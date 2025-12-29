from __future__ import annotations
from pathlib import Path
from typing import Dict, Any, List
from .io import ensure_parent, ensure_dir

def segment_oars(image_path: str, organs: List[str], output_dir: str) -> Dict[str, Any]:
    ensure_dir(output_dir)
    outputs = {}
    for organ in organs:
        out_path = str(Path(output_dir) / f"{organ}_mask.nii.gz.txt")
        Path(out_path).write_text(f"STUB {organ} mask from {image_path}\n")
        outputs[organ] = out_path
    return {"outputs": outputs, "backend": "stub"}
