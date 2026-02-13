import pytest
from langchain_core.language_models.fake_chat_models import GenericFakeChatModel
from myproject.agents.rag_agent import rag_agent  # adjust import
from myproject.retrieval import fake_retriever  # fake retriever that returns known docs

def test_rag_agent_groundedness():
    """
    Ensure RAG agent responses are grounded in the retriever results.
    """
    # Arrange: fake model returns a structured response
    fake_model = GenericFakeChatModel(
        messages=iter([
            "Answer grounded in retrieved context: example_result"
        ])
    )
    rag_agent.llm = fake_model
    rag_agent.retriever = fake_retriever  # deterministic retriever

    # Act: run with a query
    response = rag_agent.invoke({"query": "test query"})

    # Assert: groundedness conditions
    text = response.text.lower()
    for doc in fake_retriever.get_documents("test query"):
        assert doc.lower() in text, "Agent output not grounded in retrieved docs"
