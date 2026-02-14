# agent-skills-toolkit
A versioned, reusable skill and template library for AI pair-programming agents (Copilot, ChatGPT, Claude). Enforces architecture, guardrails, and modern patterns for agentic, RAG, and backend systems.

## Instruction overlays
- `instructions/COPILOT_LANGCHAIN_HARD_RULES.md`: hard rules to pin modern LangChain (`create_agent`), enforce Pydantic I/O, debug rotating file logs, and mock-only tests.
- `templates/prompts/copilot/COPILOT_INSTRUCTIONS_BASE.md`: base instructions snippet to copy into project-level Copilot instructions.
