"""Deterministic RAG evaluation pipeline template with Pydantic I/O and structured logging."""

from __future__ import annotations

import json
import logging
import uuid
from datetime import datetime, UTC
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Callable

from pydantic import BaseModel, Field


class EvaluationSample(BaseModel):
    question: str
    ground_truth: str
    answer: str
    contexts: list[str]


class EvaluationResult(BaseModel):
    run_id: str
    timestamp: str
    context_precision: float
    context_recall: float
    faithfulness: float
    answer_relevancy: float
    threshold_failures: list[str] = Field(default_factory=list)


class EvaluationThresholds(BaseModel):
    context_precision: float = 0.75
    context_recall: float = 0.70
    faithfulness: float = 0.80
    answer_relevancy: float = 0.75


def build_eval_logger(
    log_file: str = "logs/rag_evaluation.log",
    max_bytes: int = 10 * 1024 * 1024,
    backup_count: int = 5,
) -> logging.Logger:
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("rag_evaluation")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(handler)
    return logger


def run_rag_evaluation(
    samples: list[EvaluationSample],
    evaluator: Callable[[list[EvaluationSample]], dict[str, float]],
    thresholds: EvaluationThresholds | None = None,
) -> EvaluationResult:
    thresholds = thresholds or EvaluationThresholds()
    logger = build_eval_logger()
    run_id = str(uuid.uuid4())

    logger.debug(json.dumps({
        "timestamp": datetime.now(UTC).isoformat(),
        "run_id": run_id,
        "operation": "evaluation_start",
        "status": "pending",
        "sample_count": len(samples),
    }))

    metrics = evaluator(samples)
    failures: list[str] = []
    for metric_name, threshold in thresholds.model_dump().items():
        if metrics[metric_name] < threshold:
            failures.append(metric_name)

    result = EvaluationResult(
        run_id=run_id,
        timestamp=datetime.now(UTC).isoformat(),
        context_precision=metrics["context_precision"],
        context_recall=metrics["context_recall"],
        faithfulness=metrics["faithfulness"],
        answer_relevancy=metrics["answer_relevancy"],
        threshold_failures=failures,
    )

    logger.debug(json.dumps({
        "timestamp": datetime.now(UTC).isoformat(),
        "run_id": run_id,
        "operation": "evaluation_complete",
        "status": "success",
        "output": result.model_dump(),
    }))

    return result
