# Skill: A2A_CLIENT_IMPLEMENTATION

## Purpose
Provide a reusable A2A client implementation pattern using current `a2a-sdk` client primitives and explicit handling of streamed response events.

## Version Baseline
- SDK package: `a2a-sdk`
- Stable baseline verified: `0.3.23` (PyPI, February 17, 2026)
- API status note: legacy `A2AClient` is deprecated in docs; use factory-based clients for new code

## When to Use
- Implementing A2A client adapters
- Integrating with local or hosted A2A agents
- Refactoring legacy A2A client code to current API flow

## Hard Rules (MUST)
1. Use `ClientFactory.connect(...)` with explicit `ClientConfig`.
2. Create messages with official helper builders.
3. Handle stream events without dropping intermediate updates.
4. Surface protocol and transport errors explicitly.
5. Keep endpoint and auth configuration externalized.

## Workflow
1. Configure client behavior with `ClientConfig`.
2. Connect to the agent URL with `ClientFactory`.
3. Send a message using helper-built message object.
4. Iterate over responses and handle tuple/non-tuple stream variants.
5. Validate outputs and failures in deterministic tests.

## Output Checklist
- [ ] Uses modern `ClientFactory` flow
- [ ] Handles streaming events explicitly
- [ ] Handles final responses explicitly
- [ ] Error paths are surfaced and logged
- [ ] Test plan includes transport/streaming scenarios
