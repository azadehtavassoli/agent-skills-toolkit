# Copilot Instructions Base

Use these defaults for all repositories that adopt `agent-skills-toolkit`.

## Hard Rules (MUST FOLLOW)
1. **All I/O MUST use Pydantic `BaseModel`** for structured validation.
2. **Agents MUST use `create_agent` from LangChain** — do not use deprecated APIs like `create_tool_calling_agent` or `AgentExecutor`.
3. **All agents MUST have DEBUG file logging** (timestamps, steps, decisions, tool calls, inputs/outputs).
4. **No real API keys or real LLM calls in tests**; always use `GenericFakeChatModel` or stubs.
5. **All evaluations MUST log results** with timestamps and structured logs.
6. **All file handlers MUST rotate** (`maxBytes=10MB`, `backupCount=5`) and be configurable.

## LangChain API Usage
- `from langchain.agents import create_agent`
- Tool definitions via `@tool` and/or Pydantic `args_schema`
- `response_format=YourSchema` for deterministic structured output

## Discovery Entry Point
- `instructions/TABLE_OF_CONTENTS.md`
- `instructions/TOC.yaml`

## References
- `instructions/COPILOT_LANGCHAIN_HARD_RULES.md`
- `topics/agent/frameworks/langchain/30_LANGCHAIN_AGENT_FRAMEWORK.md`
- `topics/agent/frameworks/langchain/34_LANGCHAIN_STRUCTURED_OUTPUT_AND_PROMPTS.md`
- `topics/agent/frameworks/langchain/36_LANGCHAIN_LOGGING.md`
