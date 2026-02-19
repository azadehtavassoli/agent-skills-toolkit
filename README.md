# agent-skills-toolkit
A versioned, reusable skill and template library for AI pair-programming agents (Copilot, ChatGPT, Claude). Enforces architecture, guardrails, and modern patterns for agentic, RAG, backend, UI, and document-intelligence systems.

## Instruction overlays
- `instructions/COPILOT_LANGCHAIN_HARD_RULES.md`: hard rules to pin modern LangChain (`create_agent`), enforce Pydantic I/O, debug rotating file logs, and mock-only tests.
- `instructions/TABLE_OF_CONTENTS.md`: human-readable discovery index for topics, instructions, frameworks, and templates.
- `instructions/TOC.yaml`: machine-readable discovery index for automated instruction routing.
- `topics/agent/prompts/copilot/COPILOT_INSTRUCTIONS_BASE.md`: base instructions snippet to copy into project-level Copilot instructions.

## Repository structure
- `core/`: global engineering standards (logging, testing, structured output, governance rules).
- `topics/<topic>/`: topic-level skills and instructions.
- `topics/<topic>/frameworks/<framework>/`: framework-specific skills/templates/tests.
- `topics/<topic>/shared/`: framework-agnostic patterns and templates.
- `topics/<topic>/frameworks/<framework>/templates/` and `topics/<topic>/prompts/`: portable prompt and code snippets.
- `bundles/`: curated starter bundles.

## Main topics
- Agents: `topics/agent/`
- RAG: `topics/rag/`
- FastAPI: `topics/fastapi/`
- UI: `topics/ui/`
- Document Intelligence: `topics/document_intelligence/`
- MCP: `topics/mcp/`
- A2A Server: `topics/a2a_server/`
- A2A Client: `topics/a2a_client/`
