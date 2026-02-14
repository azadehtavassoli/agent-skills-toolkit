import pytest
from langchain_core.language_models.fake_chat_models import GenericFakeChatModel
from myproject.agents.agent_main import agent

def test_agent_integration_low_cost_model():
    """
    Integration test: agent with fake model should go through main path.
    """
    fake_model = GenericFakeChatModel(
        messages=iter(["Final step completed"])
    )
    agent.llm = fake_model  # inject fake model
    response = agent.invoke({"query": "integration test"})
    assert "completed" in response.text
