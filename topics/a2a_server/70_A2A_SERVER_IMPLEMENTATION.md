# Skill: A2A_SERVER_IMPLEMENTATION

## Purpose
Provide a reusable implementation pattern for A2A servers using the latest stable `a2a-sdk` primitives for executor logic, request handling, and application hosting.

## Version Baseline
- SDK package: `a2a-sdk`
- Stable baseline verified: `0.3.23` (PyPI, February 17, 2026)

## When to Use
- Building A2A server entrypoints
- Defining agent cards and skills
- Implementing executor and request lifecycle behavior

## Hard Rules (MUST)
1. Use `A2AStarletteApplication` for server app construction.
2. Use `DefaultRequestHandler` with an explicit `AgentExecutor`.
3. Use explicit task storage (`InMemoryTaskStore` or durable replacement).
4. Keep agent skill metadata explicit and discoverable through `AgentCard`.
5. Implement cancellation/error behavior explicitly.

## Workflow
1. Define `AgentCard` and `AgentSkill` metadata.
2. Implement executor methods (`execute`, `cancel`).
3. Wire request handler and task store.
4. Build app and run with explicit host/port config.
5. Add deterministic tests for protocol and execution behavior.

## Output Checklist
- [ ] Agent card and skills are defined
- [ ] Executor class is implemented
- [ ] Request handler and task store are wired
- [ ] Runnable app template exists
- [ ] Test plan includes deterministic protocol checks
