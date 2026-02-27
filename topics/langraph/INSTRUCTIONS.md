# LangGraph Implementation Instructions

## Overview
This document provides step-by-step guidance for implementing LangGraph-based agents and integrating LangSmith observability into your development workflow.

## Prerequisites
- Python 3.9+
- Familiarity with state machines and event-driven architecture
- Understanding of LLMs and function/tool calling
- (Optional) LangChain knowledge for higher-level components

## Installation

### Core Dependencies
```bash
pip install -U langgraph langchain langchain-openai
```

### LangSmith Setup (Recommended)
```bash
# No additional installation needed; set environment variables for tracing
# See "Observability Setup" section below
```

### Optional: Other Model Providers
- **Anthropic**: `pip install langchain-anthropic`
- **Google**: `pip install langchain-google-genai`
- **Local models**: `pip install ollama` or use LangChain integrations

## Core Concepts

### 1. StateGraph
A `StateGraph` is the foundation of any LangGraph agent. It defines:
- **State schema**: Pydantic model or `TypedDict` of the workflow state
- **Nodes**: Named functions that process the state
- **Edges**: Transitions between nodes (can be conditional)
- **Entry/Exit points**: `START` and `END` sentinels

### 2. MessagesState (Recommended)
Built-in state class optimized for agent patterns:
```python
from langgraph.graph import MessagesState

class MessagesState(TypedDict):
    messages: Annotated[list, add_messages]  # Auto-merges new messages
```
Use this for chat-based agents; extend it with custom fields if needed.

### 3. Nodes
Functions that receive state and return updates:
```python
def my_node(state: MessagesState) -> dict:
    # Process messages, call LLM, invoke tools, etc.
    return {"messages": [new_message]}
```
Return values are merged into state via the node's configured output policy.

### 4. Edges & Routing
- **Deterministic edges**: Always transition to the same next node
- **Conditional edges**: Use a function to decide the next node based on state
  ```python
  def route_decision(state: MessagesState) -> str:
      if some_condition:
          return "node_a"
      else:
          return "node_b"
  
  graph.add_conditional_edges("current_node", route_decision, {...})
  ```

### 5. Compilation & Execution
```python
compiled_graph = graph.compile()

# Single invocation
result = compiled_graph.invoke({"messages": [...]})

# Streaming
for output in compiled_graph.stream({"messages": [...]}):
    print(output)

# With human interrupts
config = {"configurable": {"thread_id": "user_123"}}
result = compiled_graph.invoke({...}, config=config)
```

## Implementation Patterns

### Pattern 1: Simple Sequential Agent
```python
from langgraph.graph import StateGraph, MessagesState, START, END

def agent_node(state: MessagesState):
    # Call LLM, process response
    ...
    return {"messages": [response]}

graph = StateGraph(MessagesState)
graph.add_node("agent", agent_node)
graph.add_edge(START, "agent")
graph.add_edge("agent", END)
```

### Pattern 2: Agent with Tool Calling Loop
```python
from langgraph.prebuilt import ToolNode

def should_continue(state: MessagesState) -> str:
    last_message = state["messages"][-1]
    if last_message.tool_calls:
        return "tools"
    else:
        return END

graph.add_node("agent", agent_node)
graph.add_node("tools", ToolNode(tools))
graph.add_edge(START, "agent")
graph.add_conditional_edges("agent", should_continue)
graph.add_edge("tools", "agent")
```

### Pattern 3: Multi-step Workflow with Human Approval
```python
def approval_node(state: MessagesState):
    # This node will trigger an interrupt
    # User reviews state["messages"] and provides feedback
    return {"messages": [user_feedback_message]}

graph.add_node("generate", generate_node)
graph.add_node("review", approval_node)
graph.add_edge(START, "generate")
graph.add_edge("generate", "review")

# Compile with interrupt handling
compiled = graph.compile(interrupt_before=["review"])

# First invocation hits the interrupt
output = compiled.invoke({"messages": [...]}, config={"thread_id": "123"})

# User reviews output["messages"]
# Then continue from the interrupt
output = compiled.invoke(None, config={"thread_id": "123"})
```

## Observability Setup

### Basic LangSmith Tracing
Set environment variables to enable automatic tracing:
```bash
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=<your-api-key>
export LANGSMITH_PROJECT=<project-name>
```

Then run your agent normally—all invocations are traced automatically.

### Verify LangSmith Connection
```python
from langsmith import Client

client = Client()
projects = client.list_projects()
print(f"Connected to {len(projects)} projects")
```

### Advanced: Manual Tracing
If environment variables don't work, use the LangSmith client directly:
```python
from langsmith.client import Client

langsmith_client = Client()

config = {
    "configurable": {"thread_id": "user_123"},
    "callbacks": [langsmith_callback]  # Requires LangSmith integration
}

result = compiled_graph.invoke(input_state, config=config)
```

## Development Best Practices

### 1. State Design
- Keep state schema lean; use Pydantic for validation
- Use `Annotated` with `add_messages` for append-only message lists
- Version your state if backward compatibility is needed
- Document what each field represents

### 2. Node Implementation
- Nodes should be pure functions (same input = same output)
- Return only the fields you modify; let the graph merge updates
- Use type hints for inputs and outputs
- Keep nodes focused on a single responsibility

### 3. Error Handling
```python
def safe_node(state: MessagesState):
    try:
        result = risky_operation()
        return {"messages": [result]}
    except Exception as e:
        # Return error message or retry signal
        return {"messages": [AIMessage(content=f"Error: {e}")]}
```

### 4. Testing
- Unit test individual nodes in isolation
- Use mock states to test conditional edges
- Test graph structure (connectivity, cycles) separately
- Integration test with small, deterministic inputs
- Use `invoke()` for single runs; `stream()` to inspect intermediate steps

### 5. Debugging
- Examine traces in LangSmith UI for failures
- Use `stream()` to inspect intermediate state at each step
- Log key decisions at node level (combined with LangSmith for context)
- Compare runs with different inputs in LangSmith side-by-side

### 6. Performance
- Streams reduce time-to-first-token for UX
- Parallel node execution happens automatically when safe
- Consider async/await for I/O-bound operations
- Monitor token usage and latency in LangSmith dashboards

## Directory Structure

```
your_project/
├── agents/
│   ├── __init__.py
│   └── graph.py          # StateGraph definition
├── nodes/
│   ├── __init__.py
│   ├── llm_node.py       # LLM call logic
│   ├── tool_node.py      # Tool invocation
│   └── routing.py        # Conditional edge logic
├── schemas/
│   ├── __init__.py
│   └── state.py          # Pydantic state models
├── tests/
│   ├── __init__.py
│   ├── test_nodes.py
│   └── test_graph.py
└── main.py               # Entry point
```

## External Integrations & Frameworks

### LangChain Integration
LangGraph works seamlessly with LangChain components:
- **LLMs**: `ChatOpenAI`, `ChatAnthropic`, etc.
- **Tools**: `@tool` decorator, ToolNode
- **Retrievers**: Plug into nodes for RAG
- **Output parsers**: Parse tool calls and structured outputs

### LangSmith Integration
- **Automatic tracing**: Set env vars, no code changes
- **Manual tracing**: Use `LangSmithTracer` callback for advanced control
- **Evaluation**: Use LangSmith's evaluation framework to run evals on traces

### Framework Compatibility
LangGraph is framework-agnostic and does not lock you into specific LLMs or libraries. Use it with:
- OpenAI SDK directly
- Anthropic SDK directly
- Any HTTP-based LLM API
- Local models via Ollama or vLLM

## Common Patterns & Anti-Patterns

✅ **DO**:
- Define explicit state flows; avoid hidden globals
- Test nodes independently before integration
- Use condition functions for routing; avoid if/else spaghetti in nodes
- Enable LangSmith tracing early in development
- Keep nodes stateless; let the graph manage state
- Use type hints throughout

❌ **DON'T**:
- Put all logic in a single mega-node
- Rely on side effects instead of state updates
- Ignore interrupts and checkpoints for long-running workflows
- Skip LangSmith setup; make observability a first-class concern
- Create cycles in the graph without explicit loop limits
- Mutate state directly; always return new values

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'langgraph'"
**Solution**: `pip install -U langgraph`

### Issue: LangSmith traces not appearing
**Solution**:
1. Verify `LANGSMITH_API_KEY` is set: `echo $LANGSMITH_API_KEY`
2. Check `LANGSMITH_TRACING=true`
3. Call `Client().list_projects()` to verify connectivity
4. Check LangSmith UI project name matches `LANGSMITH_PROJECT`

### Issue: State not being updated correctly
**Solution**:
1. Ensure nodes return only modified fields (dict, not full state)
2. Use `Annotated[list, add_messages]` for append-only lists
3. Verify edge policy (reducer, output keys) matches state definition

### Issue: Graph compilation fails with cycle error
**Solution**:
1. Review all edges; ensure no unintended cycles
2. Use `stream()` to visualize execution path
3. Conditional edges can create cycles; add loop limits if needed

## References
- [LangGraph Docs](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangSmith Docs](https://docs.langchain.com/langsmith/home)
- [LangChain Academy: LangGraph Course](https://academy.langchain.com/)
- [LangGraph GitHub](https://github.com/langchain-ai/langgraph)
