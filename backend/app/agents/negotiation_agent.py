import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from app.schemas.negotiation import NegotiationAnalysis

# Initialize LLM
llm = ChatGroq(
    model=os.getenv("MODEL_NAME"),
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3,
)

# Structured parser
parser = PydanticOutputParser(pydantic_object=NegotiationAnalysis)

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an expert business negotiation analyst.
Analyze the email thread and produce structured negotiation intelligence.

Follow the required JSON format strictly.
Be realistic with probabilities (0 to 1).
Do not hallucinate unrealistic leverage points.
"""
        ),
        (
            "human",
            "Email Thread:\n{thread}\n\n{format_instructions}"
        ),
    ]
)


def analyze_thread(thread: str) -> NegotiationAnalysis:
    formatted_prompt = prompt.format_messages(
        thread=thread,
        format_instructions=parser.get_format_instructions()
    )

    response = llm.invoke(formatted_prompt)

    return parser.parse(response.content)