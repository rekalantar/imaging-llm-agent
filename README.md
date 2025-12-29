# imaging-llm-agent
LLM-based medical imaging inference engine. Routes natural language prompts (for segmentation/synthesis/segmentation) to currently-available deep learning models. FastAPI + structured outputs.

## Install
Clone this repository.

```bash
cd imaging-llm-agent
poetry install
```

Check if the module is installed successfully:
```bash
poetry run python -c "import imaging_llm_agent; print('import OK')"
```

If module name cannot be found, force install:
```bash
poetry run pip install -e .
```

## Configure
Edit .env for your chosen provider

```bash
cp .env.example .env
```

### LM Studio (recommended)
Start LM Studio → Local Server → Start Server. Keep:

```bash
LLM_PROVIDER=lmstudio
LLM_BASE_URL=http://localhost:1234/v1
LLM_API_KEY=not-needed
LLM_MODEL=local-model
```

### Ollama
Set:

```bash
LLM_PROVIDER=ollama
LLM_BASE_URL=http://localhost:11434/v1
LLM_API_KEY=ollama
LLM_MODEL=llama3.1:8b
```

### OpenAI cloud
```bash
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4.1-mini
```

## Run the API
```bash
poetry run uvicorn src.imaging_llm_agent.api.main:app --reload --port 8000
```

- Swagger UI: http://localhost:8000/docs
- Health: http://localhost:8000/health


## Example requests
curl -s http://localhost:8000/run
-H "Content-Type: application/json"
-d '{"text":"Segment spleen from /tmp/ct.nii.gz to /tmp/spleen_mask.nii.gz"}'

curl -s http://localhost:8000/run
-H "Content-Type: application/json"
-d '{"text":"Register moving /tmp/moving.nii.gz to fixed /tmp/fixed.nii.gz; output to /tmp/reg_out"}'

## Quickstart (LM Studio)

1) Start LM Studio Local Server (default): `http://localhost:1234/v1`

2) Install + run this API.

## Example requests
```bash
curl -s http://localhost:8000/run \
-H "Content-Type: application/json" \
-d '{"text":"Segment spleen from /tmp/ct.nii.gz to /tmp/spleen_mask.nii.gz"}'

curl -s http://localhost:8000/run \
-H "Content-Type: application/json" \
-d '{"text":"Register moving /tmp/moving.nii.gz to fixed /tmp/fixed.nii.gz; output to /tmp/reg_out"}'
```

## Run tests
```bash
poetry run pytest
poetry run uvicorn src.imaging_llm_agent.api.main:app --reload --port 8000
```