import pytest
from myproject.tools.tool_router import my_tool  # replace with your tool

def test_tool_returns_expected_result():
    """
    Test a tool directly, ensuring its output is correct given specific inputs.
    """
    result = my_tool("input_example")
    assert isinstance(result, str)
    assert "input_example" in result
