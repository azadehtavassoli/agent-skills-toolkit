# GLOBAL RULES

## Deterministic Execution
- All agent workflows MUST be deterministic for identical inputs, configuration, and seeded randomness.
- Any nondeterministic behavior MUST be explicitly controlled and documented.

## No Hidden LLM Calls
- All LLM invocations MUST be explicit in code paths and configuration.
- Implicit provider calls, telemetry prompts, or hidden retries are prohibited.

## Explicit Tool Routing
- Tool selection MUST be observable and logged per step.
- Routing policy MUST be defined in code and testable.

## No Silent Fallbacks
- Silent fallback behavior is prohibited.
- Fallbacks MUST be explicit, logged, and surfaced in outputs.

## Explicit Memory Handling
- Memory use MUST be declared, bounded, and serialized through typed schemas.
- Memory read/write operations MUST be auditable.

## Framework-Agnostic Shared Logic
- Shared topic logic MUST NOT depend on a single framework runtime.
- Framework-specific behavior MUST be isolated in adapter/framework folders.
