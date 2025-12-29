# imaging-llm-agent
LLM-based medical imaging inference engine. Routes natural language prompts (for segmentation/synthesis/segmentation) to currently-available deep learning models. FastAPI + structured outputs.

## Quickstart (LM Studio)

1) Start LM Studio Local Server (default): `http://localhost:1234/v1`

2) Install + run this API.


Example requests:
- "Segment spleen from this CT"
- "Segment liver + kidneys + spleen"
- "Register two CTs (rigid)"