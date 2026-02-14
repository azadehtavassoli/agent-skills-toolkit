from langchain.tools import tool

@tool
def web_search(query: str) -> str:
    """Run a simple web search."""
    return f"Fake results for {query}"

# List of tools
TOOLS = [web_search]
