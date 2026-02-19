# A2A SERVER TOPIC INSTRUCTIONS

- Use the official `a2a-sdk` package for all server-side implementation.
- Keep server templates under `topics/a2a_server/templates/`.
- Use `A2AStarletteApplication` + `DefaultRequestHandler` + explicit task storage.
- Define and publish a complete `AgentCard` with skills and capabilities.
- Keep agent executor behavior deterministic and auditable.
- Enforce all core standards:
  - `core/GLOBAL_RULES.md`
  - `core/LOGGING_STANDARD.md`
  - `core/TESTING_STANDARD.md`
  - `core/STRUCTURED_OUTPUT_STANDARD.md`
