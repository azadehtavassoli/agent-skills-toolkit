from langchain_core.language_models.fake_chat_models import GenericFakeChatModel

from topics.rag.shared.rag_evaluation_pipeline import (
    EvaluationSample,
    run_rag_evaluation,
)


def test_run_rag_evaluation_stubbed() -> None:
    _fake_llm = GenericFakeChatModel(messages=iter(["ok"]))

    samples = [
        EvaluationSample(
            question="q1",
            ground_truth="gt1",
            answer="a1",
            contexts=["c1"],
        )
    ]

    def stub_evaluator(_: list[EvaluationSample]) -> dict[str, float]:
        return {
            "context_precision": 0.9,
            "context_recall": 0.8,
            "faithfulness": 0.95,
            "answer_relevancy": 0.85,
        }

    result = run_rag_evaluation(samples=samples, evaluator=stub_evaluator)

    assert result.context_precision == 0.9
    assert result.threshold_failures == []
