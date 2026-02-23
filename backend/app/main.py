from fastapi import FastAPI
from app.schemas.negotiation import NegotiationAnalysis
from app.agents.negotiation_agent import analyze_thread

app = FastAPI(title="VectorFlow API")


@app.get("/")
def root():
    return {"message": "VectorFlow is running "}


@app.post("/analyze", response_model=NegotiationAnalysis)
def analyze_negotiation(thread: str):
    return analyze_thread(thread)