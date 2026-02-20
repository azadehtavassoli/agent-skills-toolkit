# Copilot LangChain Hard Rules

## Hard Rules (MUST FOLLOW)
1. **All I/O MUST use Pydantic `BaseModel`** for structured validation.
2. **Agents MUST use `create_agent` from LangChain** — do not use deprecated APIs like `create_tool_calling_agent` or `AgentExecutor`.
3. **All agents MUST have DEBUG file logging** with rotating handlers.
4. **No real API keys or real LLM calls in tests**; always use `GenericFakeChatModel` or stubs/mocks.
5. **All evaluations MUST log results** with timestamps and structured logs.
6. **All file handlers MUST rotate** (`maxBytes=10MB`, `backupCount=5`) and be configurable.
7. **Agent, helper, and tool functions MUST use complete Google-style docstrings** with `Args:` and `Returns:` sections.
8. **Pydantic structured output models MUST describe every field** using `Field(..., description="...")`.

## LangChain API Usage
- Use `from langchain.agents import create_agent`.
- Pass tools using `@tool` or explicit schema signatures (`args_schema` with Pydantic).
- Use `response_format=YourSchema` in `create_agent` for deterministic structured output.

## Docstring and Schema Contract
- For every function used by an agent workflow (tools, routers, helpers, memory handlers), include a Google-style docstring with:
  - concise one-line summary
  - `Args:` entries for **every** argument in `name (type): description` format
  - `Returns:` section describing result semantics
- Tool docstrings must explain **what the tool does** and **when the agent should use it**.
- Avoid partial docstrings (summary-only or missing `Args:` / `Returns:`).
- In output schemas (`BaseModel` classes), annotate each field with `Field(..., description="...")`.

## Required Logging Fields
- `timestamp`, `request_id`, `agent_type`, `operation`, `status`, `duration_ms`
- `tool_name`, `input`, `output`, `error_type`, `error_message`

## Test Policy
- Unit/integration tests MUST be deterministic.
- Tests MUST assert structured outputs against Pydantic models.
- Tests MUST avoid network calls and provider SDK execution.
