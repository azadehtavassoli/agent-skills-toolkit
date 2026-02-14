from pydantic import BaseModel, Field
from langchain.agents import create_agent
from langchain.memory import ConversationBufferMemory

# 1) Structured output schema
class StepResponse(BaseModel):
    action: str
    result: str
    memory_snapshot: list[str]

# 2) Tools
def echo_tool(message: str) -> str:
    return f"ECHO: {message}"

tools = [
    {
        "name": "echo_tool",
        "description": "Echo user text.",
        "parameters_schema": {"message": str},
        "func": echo_tool,
    }
]

# 3) Memory
memory = ConversationBufferMemory()

# 4) Build agent with memory
agent = create_agent(
    model="openai/gpt-4o-mini",
    tools=tools,
    memory=memory,
    system_prompt="Agent that uses memory and tools",
    response_format=StepResponse,
)

# 5) Invoke
if __name__ == "__main__":
    answer = agent.invoke({"message": "Hello!"})
    print(answer.structured_response.json())
