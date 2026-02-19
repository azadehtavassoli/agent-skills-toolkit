# A2A SERVER TOPIC SKILL

## Purpose
Implement Agent2Agent (A2A) servers with the official Google-maintained `a2a-sdk` using explicit request handling, task state, and deterministic execution contracts.

## When to Use
- Creating a new A2A-compatible server
- Exposing agent capabilities through an A2A Agent Card
- Implementing executor/request handler patterns for A2A workflows

## Hard MUST Rules
1. Use official `a2a-sdk` server modules for handlers, tasks, and app wiring.
2. Keep executor logic deterministic for fixed inputs and context.
3. Define a complete `AgentCard` with explicit skills/capabilities.
4. Use explicit task storage and request handler wiring.
5. Keep transport/runtime setup explicit and testable.
6. Cover execution and error paths with deterministic tests.

## Workflow
1. Define agent card metadata and skill inventory.
2. Implement `AgentExecutor` behavior for core workflows.
3. Wire `DefaultRequestHandler`, task store, and Starlette app.
4. Add deterministic tests for execution and protocol responses.

## Output Checklist
- [ ] `AgentCard` is complete and valid
- [ ] Executor implementation exists
- [ ] Request handler + task store wiring is explicit
- [ ] Server app template is reusable
- [ ] Test plan covers success and failure paths
