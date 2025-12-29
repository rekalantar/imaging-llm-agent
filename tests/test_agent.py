from __future__ import annotations
import json
from unittest.mock import patch, MagicMock
from imaging_llm_agent.agent.router import make_plan

def test_make_plan_success():
    with patch("imaging_llm_agent.agent.router.load_llm_config") as mock_cfg, \
         patch("imaging_llm_agent.agent.router.make_openai_client") as mock_make_client:
        mock_cfg.return_value.provider = "lmstudio"
        mock_cfg.return_value.model = "local-model"
        mock_cfg.return_value.base_url = "http://localhost:1234/v1"
        mock_cfg.return_value.api_key = "not-needed"

        mock_client = MagicMock()
        mock_make_client.return_value = mock_client

        response_json = {
            "calls": [{"tool": "segment_oars", "args": {"image_path": "/tmp/ct.nii", "output_path": "/tmp/out.nii"}}],
            "notes": "ok"
        }
        mock_client.chat.completions.create.return_value.choices[0].message.content = json.dumps(response_json)

        plan = make_plan("Segment OARs from /tmp/ct.nii to /tmp/out.nii")
        assert plan.calls[0].tool == "segment_oars"
