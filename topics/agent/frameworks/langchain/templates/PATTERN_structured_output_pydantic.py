from pydantic import BaseModel, Field
from typing import List, Optional

class BaseAgentResponse(BaseModel):
    """
    Base structured output schema for agent responses.
    Extend this for domain-specific agents.
    """
    summary: str = Field(..., description="A concise summary of the agent’s findings.")

class SearchResult(BaseAgentResponse):
    """
    Example pattern: structured search result output.
    """
    query: str = Field(..., description="Original query passed to the agent.")
    top_snippets: List[str] = Field(..., description="Relevant retrieved document snippets.")

class ToolCallOutcome(BaseModel):
    """
    Pattern for tool call result object.
    """
    name: str = Field(..., description="Tool name that was invoked.")
    args: dict = Field(..., description="Arguments passed to the tool.")
    result: Optional[str] = Field(None, description="Output from the tool call.")
