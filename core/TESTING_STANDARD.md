# Testing Standard

## Deterministic tests
1. Tests MUST NOT call real LLM providers.
2. External SDK/network calls MUST be replaced with fakes, stubs, or monkeypatched doubles.
3. Deterministic/default mode MUST be tested separately from optional LLM mode.
4. Contract tests MUST assert output structure and key fields.

## Topic framework test checklist
- Binary stream conversion path is covered.
- Default mode avoids LLM dependencies.
- Optional LLM mode is explicit and stubbed.
- Debug logging setup is exercised where relevant.
