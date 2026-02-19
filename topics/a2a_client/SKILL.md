# A2A CLIENT TOPIC SKILL

## Purpose
Implement Agent2Agent (A2A) clients with the official Google-maintained `a2a-sdk`, using modern client factory APIs and deterministic message handling.

## When to Use
- Building clients that connect to A2A-compatible agents
- Sending task/message requests to local or remote A2A servers
- Creating reusable A2A client adapters in Python

## Hard MUST Rules
1. Use official `a2a-sdk` client APIs (`ClientFactory`, `ClientConfig`, helper builders).
2. Prefer modern client flow over deprecated APIs where possible.
3. Keep transport/streaming configuration explicit.
4. Handle stream and non-stream responses explicitly.
5. Keep failure handling explicit for card resolution, connect, and message exchange.
6. Add deterministic tests with stubbed agents in CI.

## Workflow
1. Create `ClientConfig` with explicit transport/streaming behavior.
2. Connect through `ClientFactory`.
3. Build typed message objects with official helpers.
4. Consume response stream deterministically and surface failures.

## Output Checklist
- [ ] Client creation uses `ClientFactory`
- [ ] Message payload uses official helper APIs
- [ ] Streaming event handling path is explicit
- [ ] Error paths are handled and logged
- [ ] Test plan covers transport and response variants
