import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv

from app.schemas.negotiation import NegotiationAnalysis

# Load environment variables
load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    model=os.getenv("MODEL_NAME"),
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2,  # lower temp for analytical consistency
)

# Structured output parser
parser = PydanticOutputParser(pydantic_object=NegotiationAnalysis)

# Enhanced strategic prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a senior-level business negotiation strategist.

Your task is to analyze real-world business email negotiations and produce
structured negotiation intelligence.

Analytical Requirements:
- Detect negotiation stage precisely (Opening, Counter, Concession, Deadlock, Closing).
- Identify anchoring behavior and pricing pressure.
- Detect BATNA signals (threats of alternatives).
- Identify time-pressure leverage.
- Evaluate power asymmetry between parties.
- Extract leverage points and constraints separately.
- Aggressive strategies must increase collapse risk.
- Conservative strategies must lower collapse risk.
- Ensure probability scores (0 to 1) are realistic and internally consistent.
- overall_win_probability must align with recommended_strategy.
- strategy_options probabilities must be logically coherent relative to each other.

Think analytically before producing the final structured JSON.

Return ONLY valid JSON matching the required schema.
"""
        ),
        (
            "human",
            """
Email Thread:
{thread}

Internally analyze:
- Negotiation stage
- Tone trend progression
- Power balance
- Anchoring and pricing dynamics
- BATNA signals
- Time leverage
- Risk exposure

Then produce the final structured output.

{format_instructions}
"""
        ),
    ]
)


def analyze_thread(thread: str) -> NegotiationAnalysis:
    formatted_prompt = prompt.format_messages(
        thread=thread,
        format_instructions=parser.get_format_instructions(),
    )

    response = llm.invoke(formatted_prompt)

    return parser.parse(response.content)