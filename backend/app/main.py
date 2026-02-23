from fastapi import FastAPI
from app.schemas.negotiation import NegotiationAnalysis, StrategyOption

app = FastAPI(title="VectorFlow API")


@app.get("/")
def root():
    return {"message": "VectorFlow is running 🚀"}


@app.post("/analyze", response_model=NegotiationAnalysis)
def analyze_negotiation(thread: str):

    dummy_strategy = StrategyOption(
        name="Conditional Concession",
        description="Offer a concession in exchange for commitment.",
        aggressiveness_score=0.5,
        estimated_win_probability=0.72,
        estimated_collapse_risk=0.18,
        rationale="Client shows moderate flexibility but wants assurance.",
        draft_reply="We’re willing to adjust pricing if we can secure a 12-month contract.",
        simulated_client_reaction="Client likely to counter with minor adjustment."
    )

    return NegotiationAnalysis(
        negotiation_stage="Counter Offer",
        stage_confidence=0.82,
        tone_score=0.1,
        tone_trend="stable",
        power_balance="balanced",
        leverage_points=["Long-term partnership", "Delivery speed"],
        detected_constraints=["Budget sensitivity"],
        recommended_strategy="Conditional Concession",
        strategy_options=[dummy_strategy],
        overall_win_probability=0.73,
        collapse_risk=0.17,
        summary="Negotiation is stable with moderate opportunity for structured concessions."
    )