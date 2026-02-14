# Skill: LANGCHAIN_LOGGING

## Purpose
Enforce debug-level, file-based, structured logging for LangChain agents with deterministic traceability.

## When to use
- Any LangChain agent workflow
- Tool-calling and orchestration pipelines
- Evaluation and regression runs

## Hard Rules (MUST)
1. **All agents MUST log to file at DEBUG level** (console-only logging is insufficient).
2. **File handlers MUST rotate** with defaults `maxBytes=10MB` and `backupCount=5` (configurable).
3. **Use structured log records** (JSON lines preferred) and include timezone-aware timestamps.
4. **Do not use deprecated agent executors**; use `create_agent` and invoke through current runtime APIs.
5. **Log tool calls, agent decisions, and sanitized I/O** for each step.
6. **Never log secrets or sensitive data** (API keys, auth headers, PII).

## Required Log Fields
- `timestamp`
- `request_id`
- `agent_type`
- `operation`
- `status`
- `duration_ms`
- `tool_name` (if any)
- `input` (sanitized)
- `output` (sanitized)
- `error_type` and `error_message` when failed

## Workflow
1. Build logger with `RotatingFileHandler` at DEBUG level.
2. Attach structured formatter.
3. Create helper wrappers for `agent.invoke(...)` and tool execution logging.
4. Emit start/success/failure events with request-scoped metadata.
5. Validate rotation and redaction behavior via tests.

## Output Checklist
- [ ] Debug log file generated per service/agent
- [ ] Rotation configured (10MB, 5 backups, configurable)
- [ ] Structured logs include required fields
- [ ] Agent steps + tool calls are logged
- [ ] Errors include structured diagnostics
- [ ] Secret-redaction checks included in tests
