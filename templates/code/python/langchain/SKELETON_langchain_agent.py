from pydantic import BaseModel, Field
from langchain.agents import create_agent

# 1) Define structured response schema
class SearchResult(BaseModel):
    query: str = Field(description="Executed search query")
    top_docs: list[str] = Field(description="Top relevant document snippets")

# 2) Define tools (simple example)
def dummy_search(query: str) -> str:
    """
    Sample tool that pretends to search data.
    """
    return f"Results for: {query}"

tools = [
    {
        "name": "dummy_search",
        "description": "Search for relevant documents.",
        "parameters_schema": {"query": str},
        "func": dummy_search,
    }
]

# 3) Create agent with schema
agent = create_agent(
    model="openai/gpt-4o-mini",            # model (provider dependent)
    tools=tools,
    system_prompt="Helpful agent that uses tools responsibly",
    response_format=SearchResult,          # structured output
)

# 4) Run the agent
if __name__ == "__main__":
    result = agent.invoke({"query": "climate change impact"})
    structured_data = result.structured_response
    print(structured_data.json())
