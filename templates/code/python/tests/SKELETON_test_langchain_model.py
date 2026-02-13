import pytest
from langchain_core.language_models.fake_chat_models import GenericFakeChatModel
from myproject.agents.agent_main import agent  # modify to your import

def test_structured_agent_output():
    """
    Agent should return output conforming to the structured schema.
    """
    # Arrange: Fake model responses
    fake_model = GenericFakeChatModel(
        messages=iter([
            # Provide a deterministic chat response
            "OK: {\"result\": \"success\"}"
        ])
    )
    agent.llm = fake_model  # inject fake model

    # Act
    output = agent.invoke({"input_data": "test"})

    # Assert
    structured = output.structured_response
    assert hasattr(structured, "result")
    assert structured.result == "success"
