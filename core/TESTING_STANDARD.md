# TESTING STANDARD

## Deterministic Test Policy
- Tests MUST produce deterministic outcomes in CI.
- Randomness MUST be seeded and controlled.

## LLM Isolation
- Tests MUST use `GenericFakeChatModel` or deterministic stubs/mocks.
- Real API keys, network provider calls, and live LLM invocations are prohibited in automated tests.

## Required Coverage
- Tool routing tests are mandatory.
- Structured output validation tests are mandatory.
- RAG groundedness tests are mandatory for retrieval topics.
- Logging verification tests are mandatory for agent/runtime components.

## Assertions
- Tests MUST assert typed schema conformance.
- Tests MUST assert explicit failure behavior (no silent fallback).
