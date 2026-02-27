"""
SKELETON: Basic LangGraph Agent with LangSmith Observability

This template demonstrates a minimal but complete LangGraph agent that:
1. Accepts user messages
2. Calls an LLM to generate responses
3. Optionally invokes tools based on the LLM output
4. Returns final responses
5. Automatically sends traces to LangSmith (if configured)

To use:
1. Replace LLM initialization with your chosen provider
2. Add your tools to the tools list
3. Run with LANGSMITH_TRACING=true to see traces in LangSmith UI
4. Extend state schema or add nodes as needed
"""

from typing import Annotated, TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langgraph.types import Command

from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_core.tools import tool


# ============================================================================
# STEP 1: Define State Schema
# ============================================================================

class AgentState(TypedDict):
    """
    State for the agent workflow.
    
    Fields:
        messages: Conversation history (auto-appending via add_messages reducer)
    """
    messages: Annotated[list[BaseMessage], add_messages]


# ============================================================================
# STEP 2: Define Tools (Example)
# ============================================================================

@tool
def example_tool(query: str) -> str:
    """
    Example tool that processes a query.
    Replace with actual tool implementations.
    """
    return f"Tool result for: {query}"


# Replace with your actual tools
TOOLS = [example_tool]


# ============================================================================
# STEP 3: Initialize LLM
# ============================================================================

# Example: OpenAI (requires OPENAI_API_KEY env var)
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Bind tools to LLM so it can generate tool_calls
llm_with_tools = llm.bind_tools(TOOLS)


# ============================================================================
# STEP 4: Define Agent Nodes
# ============================================================================

def agent_node(state: AgentState) -> Command[AgentState]:
    """
    LLM node: processes current messages and generates response or tool calls.
    
    Returns:
        Command with goto indicating next node (either "tools" or END)
    """
    messages = state["messages"]
    
    # Call LLM with message history
    response = llm_with_tools.invoke(messages)
    
    # Determine next step based on whether LLM requested tools
    if response.tool_calls:
        # LLM decided to call tools; add response and goto tools node
        return Command(
            update={"messages": [response]},
            goto="tools"
        )
    else:
        # LLM provided final response; end the graph
        return Command(
            update={"messages": [response]},
            goto=END
        )


# ============================================================================
# STEP 5: Build Graph
# ============================================================================

graph = StateGraph(AgentState)

# Add nodes
graph.add_node("agent", agent_node)
graph.add_node("tools", ToolNode(TOOLS))

# Define edges
graph.add_edge(START, "agent")
graph.add_edge("tools", "agent")  # After tool execution, return to agent

# Compile the graph
agent_graph = graph.compile()


# ============================================================================
# STEP 6: Usage Examples
# ============================================================================

if __name__ == "__main__":
    # Example 1: Simple invocation
    print("=== Example 1: Single Invocation ===")
    input_state = {
        "messages": [HumanMessage(content="What is 2 + 2?")]
    }
    result = agent_graph.invoke(input_state)
    print(f"Final message: {result['messages'][-1].content}")
    
    # Example 2: Streaming output
    print("\n=== Example 2: Streaming Output ===")
    input_state = {
        "messages": [HumanMessage(content="Tell me a short joke.")]
    }
    for step_output in agent_graph.stream(input_state):
        # step_output is typically {node_name: {state_updates}}
        print(f"Step: {step_output}")
    
    # Example 3: Multi-turn conversation
    print("\n=== Example 3: Multi-turn Conversation ===")
    messages = [
        HumanMessage(content="Hi, who are you?"),
    ]
    
    for turn in range(3):
        result = agent_graph.invoke({"messages": messages})
        # Extract assistant response
        assistant_msg = result["messages"][-1]
        messages = result["messages"]
        
        print(f"Turn {turn + 1}: {assistant_msg.content[:100]}...")
        
        # For demo, stop after first response
        if turn == 0:
            break


"""
NOTES FOR EXTENSION:

1. **Add Durable Execution (Thread ID)**
   config = {"configurable": {"thread_id": "user_123"}}
   result = agent_graph.invoke(input_state, config=config)
   # Next invoke with same thread_id resumes from saved state

2. **Add Human-in-the-Loop Interrupts**
   compiled = graph.compile(interrupt_before=["tools"])
   # Execution pauses before calling tools; user can inspect/modify state

3. **Enable LangSmith Tracing**
   export LANGSMITH_TRACING=true
   export LANGSMITH_API_KEY=<your-api-key>
   # Traces appear automatically in LangSmith UI

4. **Custom State & Nodes**
   - Extend AgentState with domain-specific fields
   - Add conditional edges for complex routing
   - Use stream() to debug intermediate steps

5. **Error Handling**
   - Wrap node logic in try/except
   - Return error messages instead of raising exceptions
   - Use LangSmith to analyze failure patterns
"""
