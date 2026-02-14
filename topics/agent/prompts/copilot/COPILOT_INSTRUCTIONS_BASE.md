# Copilot Instructions Base

## Hard Rules (MUST FOLLOW)
1. All I/O MUST use Pydantic `BaseModel`.
2. Agents MUST use modern framework adapters (LangChain: `create_agent`).
3. Agents MUST emit debug-level rotating file logs.
4. Tests MUST use fake models/stubs; no real LLM/provider calls.
5. Evaluations MUST log structured timestamped results.
6. File handlers MUST rotate (`maxBytes=10MB`, `backupCount=5`) and stay configurable.

## Topic References
- `topics/agent/INSTRUCTIONS.md`
- `topics/agent/compliance/REQUIRED_CAPABILITIES.md`
- `topics/agent/frameworks/langchain/30_LANGCHAIN_AGENT_FRAMEWORK.md`
- `topics/agent/frameworks/langchain/34_LANGCHAIN_STRUCTURED_OUTPUT_AND_PROMPTS.md`
- `topics/agent/frameworks/langchain/36_LANGCHAIN_LOGGING.md`
- `core/GLOBAL_RULES.md`
- `core/LOGGING_STANDARD.md`
- `core/TESTING_STANDARD.md`
- `core/STRUCTURED_OUTPUT_STANDARD.md`
