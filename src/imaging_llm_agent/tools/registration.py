from __future__ import annotations
from pathlib import Path
from typing import Dict, Any
from .io import ensure_dir

def register_rigid(fixed_path: str, moving_path: str, output_dir: str) -> Dict[str, Any]:
    ensure_dir(output_dir)
    tfm_path = str(Path(output_dir) / "rigid_transform.txt")
    resampled_path = str(Path(output_dir) / "moving_resampled.nii.gz.txt")
    Path(tfm_path).write_text(f"STUB rigid transform fixed={fixed_path} moving={moving_path}\n")
    Path(resampled_path).write_text(f"STUB resampled moving={moving_path} -> fixed={fixed_path}\n")
    return {"transform_path": tfm_path, "resampled_path": resampled_path, "backend": "stub"}

def register_deformable(fixed_path: str, moving_path: str, output_dir: str) -> Dict[str, Any]:
    ensure_dir(output_dir)
    tfm_path = str(Path(output_dir) / "deform_transform.txt")
    resampled_path = str(Path(output_dir) / "moving_resampled.nii.gz.txt")
    Path(tfm_path).write_text(f"STUB deformable transform fixed={fixed_path} moving={moving_path}\n")
    Path(resampled_path).write_text(f"STUB resampled moving={moving_path} -> fixed={fixed_path}\n")
    return {"transform_path": tfm_path, "resampled_path": resampled_path, "backend": "stub"}
