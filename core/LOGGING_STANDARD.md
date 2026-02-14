# LOGGING STANDARD

## Mandatory Logging Requirements
- Agents MUST write debug-level logs to files on disk.
- Logs MUST include timezone-aware timestamps.
- Logs MUST include per-step execution events.
- Logs MUST include tool call events with sanitized inputs and outputs.
- Logs MUST include decision reasoning summaries for routing and action choices.

## File and Rotation Policy
- Log handlers MUST use rotation with defaults: `maxBytes=10MB`, `backupCount=5`.
- Log paths and rotation settings MUST be configurable.

## Naming Convention
- Log files MUST follow: `<topic>_<component>_<date>.log` or equivalent deterministic convention.

## Structured Format
- Logs MUST use structured JSON-lines format.
- Required fields: `timestamp`, `run_id`, `request_id`, `topic`, `component`, `operation`, `status`, `duration_ms`.
- Conditional fields: `tool_name`, `input`, `output`, `reasoning`, `error_type`, `error_message`.

## Security
- Secrets, credentials, and sensitive personal data MUST be redacted before logging.
