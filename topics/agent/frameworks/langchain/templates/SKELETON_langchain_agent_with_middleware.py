from pydantic import BaseModel, Field
from langchain.agents import create_agent
from langchain.middleware import LoggingMiddleware, SummarizationMiddleware

# Structured output schema
class SummarizedOutcome(BaseModel):
    summary: str

# Tools
def simple_tool(x: str) -> str:
    return f"Processed: {x}"

tools = [
    {
        "name": "simple_tool",
        "description": "Process string.",
        "parameters_schema": {"x": str},
        "func": simple_tool,
    }
]

# Attach middleware
middleware = [
    LoggingMiddleware(),          # logs calls and decisions
    SummarizationMiddleware(),    # summarizes context
]

agent = create_agent(
    model="openai/gpt-4o-mini",
    tools=tools,
    system_prompt="Agent with logging and summarization",
    middleware=middleware,
    response_format=SummarizedOutcome,
)

if __name__ == "__main__":
    out = agent.invoke({"x": "Example text"})
    print(out.structured_response.json())
