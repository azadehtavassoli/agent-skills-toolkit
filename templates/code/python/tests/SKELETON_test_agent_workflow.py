import pytest
from myproject.workflows.langgraph_flow import graph  # modify

def test_langgraph_workflow_sequence():
    """
    Test that a workflow executes through expected nodes
    and transitions produce the correct state keys.
    """
    initial_state = {"user_input": "abc"}
    result = graph.invoke(initial_state)
    
    # Assert that each key was written
    assert "ai1_output" in result
    assert "ai2_output" in result
