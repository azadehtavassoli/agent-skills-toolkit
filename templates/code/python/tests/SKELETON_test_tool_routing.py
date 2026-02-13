import pytest
from langchain_core.language_models.fake_chat_models import GenericFakeChatModel
from myproject.agents.agent_main import agent  # adjust import
from myproject.tools.tool_router import web_search  # example tool

def test_tool_routing_sequence():
    """
    Ensure agent calls the correct tool with expected args.
    """
    # Arrange: fake model simulates a tool call
    fake_model = GenericFakeChatModel(
        messages=iter([
            # Model responds with a tool call message structure
            {
                "role": "assistant",
                "tool_calls": [
                    {
                        "name": "web_search",
                        "args": {"query": "expected query"},
                        "id": "call_1",
                    }
                ],
            },
            # Model then provides final text
            "Search complete"
        ])
    )
    agent.llm = fake_model

    # Act
    res = agent.invoke({"query": "expected query"})

    # Assert
    # Check tool call was executed properly
    executed = any(message.tool_calls for message in res.messages)
    assert executed, "Agent did not make a tool call"

    # Validate correct tool name and args
    calls = [call for msg in res.messages for call in getattr(msg, "tool_calls", [])]
    assert any(c["name"] == "web_search" for c in calls)
    assert any(c["args"].get("query") == "expected query" for c in calls)
