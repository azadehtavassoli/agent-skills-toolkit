# agent-skills-toolkit

Framework-agnostic, topic-based governance system for deterministic AI agent development.

## Repository Structure

- `core/` — global engineering standards and governance policies
- `topics/` — topic packs with skill definitions, instructions, shared logic, and framework adapters
  - `topics/agent/frameworks/`: `langchain`, `google-adk`
  - `topics/ui/frameworks/`: `streamlit`, `gradio`
- `bundles/` — bundle definitions
- `COPILOT_TOPIC_REGISTRY.md` — topic-to-standard mapping for Copilot integration
- `GOVERNANCE.md` — extension and review governance
- `ROADMAP.md` — planned topic expansion

## Standards First

All topics and framework adapters must comply with:
- `core/GLOBAL_RULES.md`
- `core/LOGGING_STANDARD.md`
- `core/TESTING_STANDARD.md`
- `core/STRUCTURED_OUTPUT_STANDARD.md`
- `core/VERSIONING_POLICY.md`
