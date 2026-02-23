import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from app.schemas.negotiation import NegotiationAnalysis

load_dotenv()

llm = ChatGroq(
    model=os.getenv("MODEL_NAME"),
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2,
)

parser = PydanticOutputParser(pydantic_object=NegotiationAnalysis)

analysis_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a senior negotiation strategist.

Perform a deep strategic analysis of the email negotiation.

Analyze:
- Exact negotiation stage
- Tone progression across messages
- Anchoring behavior
- BATNA signals
- Time-pressure leverage
- Power asymmetry
- Pricing psychology
- Risk exposure

Be detailed and analytical.
Do NOT output JSON.
Write structured strategic reasoning.
"""
        ),
        (
            "human",
            "Email Thread:\n{thread}"
        ),
    ]
)


extraction_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are converting expert negotiation analysis into structured intelligence.

Rules:
- Follow schema strictly.
- Probabilities must be between 0 and 1.
- Aggressive strategies increase collapse risk.
- Conservative strategies lower collapse risk.
- overall_win_probability must align with recommended_strategy.
- Ensure logical consistency across strategy options.
Return ONLY valid JSON.
"""
        ),
        (
            "human",
            """
Based on the following expert analysis:

{analysis}

Produce structured negotiation intelligence.

{format_instructions}
"""
        ),
    ]
)


def analyze_thread(thread: str) -> NegotiationAnalysis:
    
    formatted_analysis_prompt = analysis_prompt.format_messages(thread=thread)
    analysis_response = llm.invoke(formatted_analysis_prompt)

    strategic_analysis = analysis_response.content

    
    formatted_extraction_prompt = extraction_prompt.format_messages(
        analysis=strategic_analysis,
        format_instructions=parser.get_format_instructions(),
    )

    extraction_response = llm.invoke(formatted_extraction_prompt)

    return parser.parse(extraction_response.content)