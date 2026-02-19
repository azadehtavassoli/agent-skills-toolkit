# A2A CLIENT TOPIC INSTRUCTIONS

- Use the official `a2a-sdk` package for all client implementation.
- Keep client templates under `topics/a2a_client/templates/`.
- Prefer modern APIs (`ClientFactory`, `ClientConfig`) for new code.
- Build request messages via official helper constructors.
- Handle both streamed updates and final responses explicitly.
- Enforce all core standards:
  - `core/GLOBAL_RULES.md`
  - `core/LOGGING_STANDARD.md`
  - `core/TESTING_STANDARD.md`
  - `core/STRUCTURED_OUTPUT_STANDARD.md`
