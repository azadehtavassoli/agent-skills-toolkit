# Skill: ERROR_RESPONSES_AND_LOGGING

## Purpose
Ensure consistent error handling and robust, persistent structured logging across FastAPI routes, services, and agent execution contexts. Logging must capture detailed trace information, including debug-level logs written to file.

## When to use
- Any backend endpoint implementation
- During agent execution or multi-step workflows
- When integrating external tools or systems
- For production observability and debugging

## Hard Rules (MUST)
1. **Standardized error response schema.**
   - All HTTP error responses must use a consistent JSON structure:  
     `{ code: str, message: str, details?: dict }`.

2. **Structured logging with persistent files.**
   - Log messages must be written to one or more log files.
   - Logs must include timestamps, log level, module, and structured context.
   - Log files must capture debug-level information during development.

3. **Debug logs for agent execution steps.**
   - Logs must record:
     - Agent reasoning steps  
     - Tool invocation calls and results  
     - Inputs/outputs for each step  
     - Memory state changes (if any)  
   - Debug logs must be written separate from standard operational logs.

4. **Configurable logging settings.**
   - Log file location, log level, rotation policy, and retention must be configurable via environment or settings object.

5. **No unfiltered internal errors to clients.**
   - Raw tracebacks must not leak in HTTP responses; they must be captured only in logs.

## Soft Preferences (SHOULD)
- Use structured formats (JSON) for logs to facilitate ingestion into monitoring systems.
- Prefer separate loggers for:
  - HTTP access
  - Agent internal executions
  - Tool integrations
  - Database/repository interactions

## Anti-patterns
- Printing tracebacks to stdout/stderr without file persistence.
- Logging only free-form text without structured fields.
- Omitting debug context in logs used for troubleshooting.
- Hardcoding log paths or rotation policies.

## Workflow
1. **Configure logger at startup**
   - Read settings for log file path, level, and rotation rules.
2. **Initialize handlers**
   - Add file handler(s) with DEBUG and INFO level outputs.
   - Add structured formatter (JSON or annotated text).
3. **Wrap application and agent execution**
   - Middleware/routing should capture incoming requests and context.
   - Wrap agent steps in logging context to capture decisions.
4. **Error cases**
   - Log exception details with stack info at ERROR level.
   - Return client response with safe message and status code.

## Output Checklist
- [ ] Logging configured via settings
- [ ] Log file(s) exist with correct rotation/retention
- [ ] Debug logs capture agent steps and tool calls
- [ ] Structured logs include timestamp + level + context
- [ ] No raw internal tracebacks are exposed to clients
