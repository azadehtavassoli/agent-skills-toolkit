from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict

# Define a shared state type
class WorkflowState(TypedDict):
    user_input: str
    ai1_output: str
    ai2_output: str

# Nodes
def agent_one(state: WorkflowState) -> dict:
    return {"ai1_output": state["user_input"].upper()}

def agent_two(state: WorkflowState) -> dict:
    return {"ai2_output": state["ai1_output"][::-1]}

# 1) Build graph
graph = StateGraph(WorkflowState)
graph.add_node("agent1", agent_one)
graph.add_node("agent2", agent_two)
graph.add_edge(START, "agent1")
graph.add_edge("agent1", "agent2")
graph.add_edge("agent2", END)

# 2) Run workflow
if __name__ == "__main__":
    initial = {"user_input": "hello"}
    result = graph.invoke(initial)
    print(result)
