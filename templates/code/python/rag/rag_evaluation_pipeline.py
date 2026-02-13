"""
RAG Evaluation Pipeline using RAGAS
Follows agent-skills-toolkit evaluation patterns
"""
from typing import List, Dict
from pydantic import BaseModel, Field
import logging
from datetime import datetime
import json
import os

from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    context_precision,
    context_recall,
    faithfulness,
    answer_relevancy
)
from langchain_openai import ChatOpenAI, OpenAIEmbeddings


# Structured Models (MUST use Pydantic)
class EvaluationSample(BaseModel):
    """Single evaluation sample"""
    question: str = Field(description="Question to evaluate")
    ground_truth: str = Field(description="Expected answer")
    answer: str = Field(description="Generated answer from RAG")
    contexts: List[str] = Field(description="Retrieved contexts")


class EvaluationResult(BaseModel):
    """Evaluation results"""
    context_precision: float = Field(description="Context precision score")
    context_recall: float = Field(description="Context recall score")
    faithfulness: float = Field(description="Faithfulness score")
    answer_relevancy: float = Field(description="Answer relevancy score")
    timestamp: str = Field(description="Evaluation timestamp")
    sample_count: int = Field(description="Number of samples evaluated")
    alerts: List[str] = Field(default_factory=list, description="Triggered alerts")


# Evaluation Pipeline
class RAGEvaluationPipeline:
    """RAG evaluation pipeline with logging and thresholds"""
    
    def __init__(
        self,
        judge_model: str = "gpt-4",
        embedding_model: str = "text-embedding-3-small",
        thresholds: Dict[str, float] = None,
        log_file: str = "logs/rag_evaluation.log"
    ):
        self.judge_llm = ChatOpenAI(model=judge_model, temperature=0)
        self.embeddings = OpenAIEmbeddings(model=embedding_model)
        
        # Default thresholds
        self.thresholds = thresholds or {
            "context_precision": 0.75,
            "context_recall": 0.70,
            "faithfulness": 0.80,
            "answer_relevancy": 0.75
        }
        
        # Setup logging
        self.logger = self._setup_logger(log_file)
    
    def _setup_logger(self, log_file: str) -> logging.Logger:
        """Setup evaluation logger"""
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        
        logger = logging.getLogger("rag_evaluation")
        logger.setLevel(logging.INFO)
        logger.handlers.clear()
        
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            '{"timestamp":"%(asctime)s","level":"%(levelname)s","message":%(message)s}'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger
    
    def evaluate(self, samples: List[EvaluationSample]) -> EvaluationResult:
        """Run evaluation on samples"""
        
        self.logger.info(json.dumps({
            "operation": "evaluation_start",
            "sample_count": len(samples)
        }))
        
        # Convert to RAGAS dataset format
        eval_data = {
            "question": [s.question for s in samples],
            "ground_truth": [s.ground_truth for s in samples],
            "answer": [s.answer for s in samples],
            "contexts": [s.contexts for s in samples]
        }
        dataset = Dataset.from_dict(eval_data)
        
        # Run evaluation
        result = evaluate(
            dataset=dataset,
            metrics=[
                context_precision,
                context_recall,
                faithfulness,
                answer_relevancy
            ],
            llm=self.judge_llm,
            embeddings=self.embeddings
        )
        
        # Check thresholds and generate alerts
        alerts = []
        for metric, threshold in self.thresholds.items():
            score = result[metric]
            if score < threshold:
                alert = f"{metric} below threshold: {score:.3f} < {threshold}"
                alerts.append(alert)
                self.logger.warning(json.dumps({
                    "operation": "threshold_alert",
                    "metric": metric,
                    "score": score,
                    "threshold": threshold
                }))
        
        # Structure result
        evaluation_result = EvaluationResult(
            context_precision=result["context_precision"],
            context_recall=result["context_recall"],
            faithfulness=result["faithfulness"],
            answer_relevancy=result["answer_relevancy"],
            timestamp=datetime.now().isoformat(),
            sample_count=len(samples),
            alerts=alerts
        )
        
        self.logger.info(json.dumps({
            "operation": "evaluation_complete",
            "results": evaluation_result.dict()
        }))
        
        return evaluation_result


# Testing with Mocks (For unit tests - uses GenericFakeChatModel)
def create_mock_evaluation_pipeline() -> RAGEvaluationPipeline:
    """Create evaluation pipeline with mocked components for testing"""
    from langchain_core.language_models.fake_chat_models import GenericFakeChatModel
    
    class MockRAGEvaluationPipeline(RAGEvaluationPipeline):
        def __init__(self, log_file: str = "logs/test_rag_evaluation.log"):
            # Use fake LLM for testing
            self.judge_llm = GenericFakeChatModel(
                messages=iter(["Mocked evaluation response"])
            )
            self.embeddings = None  # Mock embeddings if needed
            
            self.thresholds = {
                "context_precision": 0.75,
                "context_recall": 0.70,
                "faithfulness": 0.80,
                "answer_relevancy": 0.75
            }
            
            self.logger = self._setup_logger(log_file)
        
        def evaluate(self, samples: List[EvaluationSample]) -> EvaluationResult:
            """Mock evaluation - returns deterministic results"""
            self.logger.info(json.dumps({
                "operation": "mock_evaluation_start",
                "sample_count": len(samples)
            }))
            
            # Return mock results for testing
            return EvaluationResult(
                context_precision=0.85,
                context_recall=0.78,
                faithfulness=0.92,
                answer_relevancy=0.88,
                timestamp=datetime.now().isoformat(),
                sample_count=len(samples),
                alerts=[]
            )
    
    return MockRAGEvaluationPipeline()


# Example Usage
if __name__ == "__main__":
    # Prepare evaluation samples
    samples = [
        EvaluationSample(
            question="What is the capital of France?",
            ground_truth="The capital of France is Paris.",
            answer="Paris is the capital of France.",
            contexts=[
                "Paris is the capital and most populous city of France.",
                "France is a country in Western Europe."
            ]
        ),
        EvaluationSample(
            question="Who wrote Romeo and Juliet?",
            ground_truth="William Shakespeare wrote Romeo and Juliet.",
            answer="Romeo and Juliet was written by William Shakespeare.",
            contexts=[
                "Romeo and Juliet is a tragedy written by William Shakespeare.",
                "Shakespeare was an English playwright and poet."
            ]
        ),
        # Add more samples (MUST have minimum 20 for meaningful results)
    ]
    
    # Run evaluation (use real pipeline in production)
    # pipeline = RAGEvaluationPipeline()
    
    # For testing - use mock pipeline
    pipeline = create_mock_evaluation_pipeline()
    results = pipeline.evaluate(samples)
    
    print(f"Context Precision: {results.context_precision:.3f}")
    print(f"Context Recall: {results.context_recall:.3f}")
    print(f"Faithfulness: {results.faithfulness:.3f}")
    print(f"Answer Relevancy: {results.answer_relevancy:.3f}")
    
    if results.alerts:
        print("\nAlerts:")
        for alert in results.alerts:
            print(f"  - {alert}")
