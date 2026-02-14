# AGENT TOPIC SKILL

## Purpose
Define agent systems as deterministic execution engines with explicit control, observability, and schema-validated interfaces.

## When to Use
- Building single-agent or multi-agent systems
- Designing tool-enabled execution workflows
- Implementing framework adapters for agent runtimes

## Hard MUST Rules
1. Agent execution MUST be deterministic under fixed inputs/config.
2. LLM is an optional component; business logic MUST remain executable with stubs.
3. Tool routing MUST be explicit, inspectable, and testable.
4. Debug-level file logging is mandatory for all agent runs.
5. Structured output via Pydantic models is mandatory.
6. Memory policy (scope, retention, eviction) MUST be explicitly defined.

## Workflow
1. Define typed input/output models.
2. Define routing policy and tool registry.
3. Implement framework adapter.
4. Attach logging adapter and run tracing.
5. Validate with deterministic tests.

## Output Checklist
- [ ] Typed I/O models defined
- [ ] Routing policy implemented and tested
- [ ] Logging configured per standard
- [ ] Memory policy documented
- [ ] Deterministic test coverage complete
