from __future__ import annotations
import tempfile
from pathlib import Path
from imaging_llm_agent.tools.segmentation import segment_oars
from imaging_llm_agent.tools.registration import register_rigid

def test_segment_oars_creates_outputs():
    with tempfile.TemporaryDirectory() as d:
        img = str(Path(d) / "ct.nii.gz")
        Path(img).write_text("fake")
        outdir = str(Path(d) / "masks")
        r = segment_oars(img, ["liver", "spleen"], outdir)
        assert Path(r["outputs"]["liver"]).exists()
        assert Path(r["outputs"]["spleen"]).exists()

def test_register_rigid_creates_outputs():
    with tempfile.TemporaryDirectory() as d:
        fixed = str(Path(d) / "fixed.nii.gz")
        moving = str(Path(d) / "moving.nii.gz")
        Path(fixed).write_text("fake")
        Path(moving).write_text("fake")
        outdir = str(Path(d) / "reg")
        r = register_rigid(fixed, moving, outdir)
        assert Path(r["transform_path"]).exists()
        assert Path(r["resampled_path"]).exists()
