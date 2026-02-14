import pytest
from langchain.memory import ConversationBufferMemory
from myproject.agents.agent_memory import agent_with_memory  # adjust

def test_memory_accumulates_context():
    """
    Ensure memory stores conversation state over multiple steps.
    """
    # Arrange
    memory = ConversationBufferMemory()
    agent_with_memory.memory = memory

    # Act & Assert
    agent_with_memory.invoke({"message": "hello"})
    agent_with_memory.invoke({"message": "again"})

    stored = memory.load_memory_variables({})
    assert "hello" in str(stored)
    assert "again" in str(stored)
