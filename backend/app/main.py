from fastapi import FastAPI
from app.schemas.negotiation import (
    NegotiationAnalysis,
    NegotiationRequest,
)
from app.agents.negotiation_agent import analyze_thread

app = FastAPI(title="VectorFlow API")


@app.get("/")
def root():
    return {"message": "VectorFlow is running 🚀"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/analyze", response_model=NegotiationAnalysis)
def analyze_negotiation(request: NegotiationRequest):
    return analyze_thread(request.thread)