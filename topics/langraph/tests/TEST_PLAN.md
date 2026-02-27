# LangGraph Testing Strategy

## Overview
This document outlines testing best practices for LangGraph agents, covering unit tests, integration tests, and observability validation.

## Test Categories

### 1. Unit Tests: Node Logic

Test individual nodes in isolation using mock state and deterministic inputs.

#### Example: Agent Node
```python
import pytest
from langchain_core.messages import HumanMessage, AIMessage
from unittest.mock import patch, MagicMock

def test_agent_node_with_tool_call():
    """Agent node should return tool_calls when LLM requests them."""
    # Arrange
    state = {
        "messages": [HumanMessage(content="Use a tool please")]
    }
    
    mock_llm = MagicMock()
    mock_response = AIMessage(
        content="",
        tool_calls=[{"id": "1", "function": {"name": "tool", "arguments": "{}"}}]
    )
    mock_llm.invoke.return_value = mock_response
    
    # Act
    result = agent_node(state)  # with patched LLM
    
    # Assert
    assert len(result["messages"]) == 1
    assert result["goto"] == "tools"
```

#### Example: Routing/Conditional Edges
```python
def test_should_continue_routing():
    """Route to END when no tool calls, to 'tools' when tool_calls exist."""
    # Test with tool call
    state_with_tools = {
        "messages": [AIMessage(content="", tool_calls=[...])]
    }
    assert should_continue(state_with_tools) == "tools"
    
    # Test without tool call
    state_no_tools = {
        "messages": [AIMessage(content="Final response")]
    }
    assert should_continue(state_no_tools) == END
```

### 2. Integration Tests: Graph Execution

Test the complete graph with small, deterministic inputs to verify node connections and state flow.

#### Example: Full Graph
```python
def test_agent_graph_single_turn():
    """Graph should process input message and return AI response."""
    # Use a deterministic mock LLM for reproducible results
    with patch('agent.llm_with_tools') as mock_llm:
        mock_llm.invoke.return_value = AIMessage(content="Hello!")
        
        result = agent_graph.invoke({
            "messages": [HumanMessage(content="Hi")]
        })
        
        assert len(result["messages"]) == 2
        assert result["messages"][-1].content == "Hello!"
```

#### Example: Tool Calling Loop
```python
def test_agent_graph_with_tool_call():
    """Graph should call tool when LLM requests it, then continue."""
    with patch('agent.llm_with_tools') as mock_llm, \
         patch('agent.example_tool') as mock_tool:
        
        # First call: LLM calls tool
        tool_call_response = AIMessage(
            content="",
            tool_calls=[{"id": "1", "function": {"name": "example_tool", 
                         "arguments": '{"query": "test"}'}, "type": "tool_use"}]
        )
        # Second call: LLM provides final response
        final_response = AIMessage(content="Tool said: test result")
        
        mock_llm.invoke.side_effect = [tool_call_response, final_response]
        mock_tool.return_value = "test result"
        
        result = agent_graph.invoke({
            "messages": [HumanMessage(content="Do something")]
        })
        
        # Verify tool was called
        mock_tool.assert_called_once()
        # Verify final response contains tool output
        assert "test result" in result["messages"][-1].content
```

### 3. State Mutation Tests

Test that state updates work correctly with custom reducers.

```python
def test_messages_state_append():
    """Messages should append correctly using add_messages reducer."""
    from langgraph.graph.message import add_messages
    
    initial = [HumanMessage(content="msg1")]
    update = [AIMessage(content="msg2")]
    
    result = add_messages(initial, update)
    assert len(result) == 2
    assert result[0].content == "msg1"
    assert result[1].content == "msg2"
```

### 4. Graph Structure Tests

Test that the graph is correctly constructed without executing nodes.

```python
def test_graph_structure():
    """Verify graph has correct nodes and edges."""
    # Get graph structure from compiled graph
    nodes = list(agent_graph.nodes)
    assert "agent" in nodes
    assert "tools" in nodes
    
    # Verify START → agent edge exists
    # Note: exact API depends on LangGraph version
```

### 5. Error Handling Tests

Test that errors in nodes are handled gracefully.

```python
def test_llm_call_fails():
    """Agent should handle LLM errors gracefully."""
    with patch('agent.llm_with_tools') as mock_llm:
        mock_llm.invoke.side_effect = Exception("API error")
        
        # Node should catch and return error message (or re-raise as appropriate)
        # Depends on your error handling strategy
        # Example: return Command with error message
        result = agent_node({
            "messages": [HumanMessage(content="Hi")]
        })
        
        # Verify error is captured
        assert len(result["messages"]) == 1
```

### 6. LangSmith Observability Tests

Test that tracing is correctly configured and produces expected traces.

```python
def test_langsmith_tracing_enabled():
    """Verify LangSmith client can connect (requires API key)."""
    import os
    from langsmith import Client
    
    # This test requires LANGSMITH_API_KEY env var
    if not os.getenv("LANGSMITH_API_KEY"):
        pytest.skip("LANGSMITH_API_KEY not set")
    
    client = Client()
    projects = client.list_projects()
    assert len(projects) > 0
```

```python
def test_agent_produces_trace():
    """Agent invocation should produce a trace in LangSmith."""
    import os
    os.environ["LANGSMITH_TRACING"] = "true"  # Enable tracing
    
    result = agent_graph.invoke({
        "messages": [HumanMessage(content="Test")]
    })
    
    # Verify trace was created by checking LangSmith
    # This may require polling or immediate availability
    # See LangSmith docs for trace retrieval API
```

## Test Fixtures and Mocking

### Mock LLM
```python
import pytest
from unittest.mock import MagicMock
from langchain_core.messages import AIMessage

@pytest.fixture
def mock_llm():
    llm = MagicMock()
    llm.invoke.return_value = AIMessage(content="Mocked response")
    llm.bind_tools.return_value = llm
    return llm
```

### Sample State
```python
@pytest.fixture
def sample_state():
    from langchain_core.messages import HumanMessage
    return {
        "messages": [HumanMessage(content="Hello")]
    }
```

### Agent Graph with Mocks
```python
@pytest.fixture
def agent_with_mocks(mock_llm):
    # Patch the real LLM with mock before building graph
    with patch('agent.llm', mock_llm):
        with patch('agent.llm_with_tools', mock_llm):
            from agent import agent_graph
            yield agent_graph
```

## Acceptance Criteria

A well-tested LangGraph agent should:

- ✅ All nodes execute without errors given valid input
- ✅ State is correctly propagated through the graph
- ✅ Conditional edges route to the correct next node
- ✅ Tool calls are formatted correctly and invoked
- ✅ Graph terminates at END (no infinite loops)
- ✅ LangSmith traces contain expected node names and state updates
- ✅ Error cases are handled gracefully (no silent failures)
- ✅ Streaming output contains intermediate steps (if implemented)
- ✅ Multi-turn conversations maintain message history correctly
- ✅ Human-in-the-loop interrupts pause at expected nodes

## Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=agent tests/

# Run specific test file
pytest tests/test_nodes.py

# Run with verbose output
pytest -v tests/

# Run LangSmith integration tests (requires API key)
pytest tests/test_langsmith.py --skip-ci
```

## CI/CD Integration

Suggested GitHub Actions workflow:
```yaml
name: Test LangGraph Agent
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -e .
      - run: pytest tests/ --cov=agent
      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

## Debugging Failed Tests

1. **Use `stream()` to inspect intermediate steps**:
   ```python
   for step in agent_graph.stream(input_state):
       print(step)  # See what each node produces
   ```

2. **Enable LangSmith tracing to see full trace**:
   ```python
   os.environ["LANGSMITH_TRACING"] = "true"
   # Then check LangSmith UI for trace details
   ```

3. **Mock incrementally**: Start with all mocked, then replace mocks one-by-one to find the failing component

4. **Use pytest debugger**:
   ```bash
   pytest --pdb tests/test_agent.py  # Drop into debugger on failure
   ```

## Performance & Load Testing

For agents with many tool calls or long conversations:

```python
def test_agent_handles_long_conversation():
    """Agent should handle many turns without degradation."""
    messages = [HumanMessage(content=f"Message {i}") 
                for i in range(100)]
    
    result = agent_graph.invoke({"messages": messages})
    assert len(result["messages"]) > 100
```

Track latency and token usage via LangSmith dashboards for production agents.
