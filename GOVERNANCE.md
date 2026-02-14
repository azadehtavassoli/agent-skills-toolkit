# GOVERNANCE

## Adding a New Topic
1. Create `topics/<topic>/SKILL.md` and `topics/<topic>/INSTRUCTIONS.md`.
2. Define shared abstractions under `topics/<topic>/shared/`.
3. Register required standards in `COPILOT_TOPIC_REGISTRY.md`.

## Adding a New Framework Adapter
1. Create `topics/<topic>/frameworks/<adapter>/` with `templates/` and `tests/`.
2. Implement adapter-specific logic only in adapter folder.
3. Verify compliance with `core/*` standards and topic compliance files.

## Updating Shared Logic
- Shared logic changes MUST remain framework-agnostic.
- Changes MUST include backward-compatibility notes.
- Deterministic behavior and schema validation MUST be preserved.

## PR Review Checklist
- Determinism confirmed
- No hidden LLM calls
- Explicit routing and no silent fallback
- Structured logging and rotation configured
- Pydantic schema boundaries enforced
- Deterministic tests included

## Required Test Coverage
- Routing tests
- Structured output validation tests
- Logging verification tests
- Topic-specific groundedness/evaluation tests where applicable

## Logging Verification Steps
1. Confirm debug file logs are generated.
2. Confirm JSON-line entries with required fields.
3. Confirm tool call and decision events are logged.
4. Confirm rotation settings: 10MB / 5 backups (configurable).

## Structured Output Verification Steps
1. Confirm all structured interfaces use Pydantic models.
2. Confirm schema validation is enforced at boundaries.
3. Confirm failure paths return explicit typed errors.

## Prohibited Patterns
- Hidden or implicit LLM calls
- Silent fallback logic
- Raw dict public outputs
- Framework-coupled shared logic
- Real LLM/provider calls in automated tests
