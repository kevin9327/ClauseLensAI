from pathlib import Path
from typing import Any, Dict, List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .clause_engine import PRESET_CONTRACTS, analyze_custom_contract

ROOT_DIR = Path(__file__).resolve().parent.parent
PUBLIC_DIR = ROOT_DIR / "public"

app = FastAPI(title="ClauseLens Studio — Interactive Contract X-Ray & Counter-Offer Studio", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class AnalyzeRequest(BaseModel):
    text: str
    title: str = "Custom Pasted Agreement"


@app.get("/api/health")
def get_health() -> Dict[str, Any]:
    return {
        "status": "ok",
        "service": "ClauseLens Studio",
        "presets_count": len(PRESET_CONTRACTS),
        "skill_pack": "challengepost/learn-ai-basics (all 5 public devpost/ artifacts approved)",
    }


@app.get("/api/presets")
def get_presets() -> List[Dict[str, Any]]:
    return PRESET_CONTRACTS


@app.post("/api/analyze")
def post_analyze(req: AnalyzeRequest) -> Dict[str, Any]:
    return analyze_custom_contract(req.text, req.title)


if PUBLIC_DIR.exists():
    app.mount("/", StaticFiles(directory=str(PUBLIC_DIR), html=True), name="public")
