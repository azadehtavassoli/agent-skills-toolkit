# Skill: RAG_EVALUATION

## Purpose
Define deterministic, testable RAG evaluation pipelines with structured outputs and reproducible logging.

## When to use
- Any RAG feature release
- Retriever/reranker prompt changes
- Pre-merge regression checks

## Hard Rules (MUST)
1. **All evaluation inputs/outputs MUST use Pydantic models.**
2. **All evaluation runs MUST emit structured logs** with timestamp and run_id.
3. **Unit tests MUST use `GenericFakeChatModel` or stubs**; no real LLM calls.
4. **Evaluation pipeline MUST support offline deterministic mode** for CI.
5. **Threshold failures MUST be surfaced as machine-readable artifacts** (JSON).

## Core Metrics
- `context_precision`
- `context_recall`
- `faithfulness`
- `answer_relevancy`

## Workflow
1. Build dataset from typed `EvaluationSample` models.
2. Run evaluator (RAGAS or equivalent) and collect metrics.
3. Validate against thresholds.
4. Persist `EvaluationResult` JSON and structured logs.
5. In tests, stub evaluator and LLM to fixed outputs.

## Output Checklist
- [ ] Dataset schema validated
- [ ] Metrics computed and serialized
- [ ] Threshold checks enforced
- [ ] Logs written with run metadata
- [ ] Tests avoid external LLM/network calls
