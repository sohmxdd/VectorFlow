from pydantic import BaseModel
from typing import List


class NegotiationRequest(BaseModel):
    thread: str


class StrategyOption(BaseModel):
    name: str
    description: str
    aggressiveness_score: float
    estimated_win_probability: float
    estimated_collapse_risk: float
    rationale: str
    draft_reply: str
    simulated_client_reaction: str


class NegotiationAnalysis(BaseModel):
    negotiation_stage: str
    stage_confidence: float

    tone_score: float
    tone_trend: str
    power_balance: str

    leverage_points: List[str]
    detected_constraints: List[str]

    recommended_strategy: str
    strategy_options: List[StrategyOption]

    overall_win_probability: float
    collapse_risk: float

    summary: str