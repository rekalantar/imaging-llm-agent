from __future__ import annotations
import logging
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from ..agent.schema import RunRequest
from ..agent.router import make_plan
from ..agent.executor import execute_plan
from ..agent.llm_client import load_llm_config

load_dotenv()
logging.basicConfig(level=logging.INFO)

app = FastAPI(title="Imaging LLM Agent", version="0.1.0")

@app.get("/health")
def health():
    cfg = load_llm_config()
    return {
        "ok": True,
        "version": "0.2.0",
        "llm_provider": cfg.provider,
        "llm_model": cfg.model,
        "llm_base_url": cfg.base_url,
    }

@app.post("/run")
def run(req: RunRequest):
    try:
        plan = make_plan(req.text)
        result = execute_plan(plan)
        return {"plan": plan.model_dump(), "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"docs": "/docs", "health": "/health", "run": "/run"}
