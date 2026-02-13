# Skill: LANGCHAIN_AGENT_FRAMEWORK

## Purpose
Define how to construct, configure, and execute modern LangChain agents using current (≥ v1.0) APIs and runtime semantics.

## When to use
- Creating agents with decision logic that can call tools
- Integrating external functions into agent reasoning
- Choosing appropriate agent patterns for tasks

## Hard Rules (MUST)
1. **Use standard `create_agent` APIs with structured output support.**
   Prefer passing schemas/types to `response_format`. :contentReference[oaicite:1]{index=1}
2. **Initialize all tools explicitly.**
   Tools must be decorated or wrapped with explicit signatures. :contentReference[oaicite:2]{index=2}
3. **Structured output is default.**
   When model supports native structured output, rely on it; fallback to tool-based strategy when not. :contentReference[oaicite:3]{index=3}
4. **Agent iterations must terminate.**
   Define clear stop conditions (final output or step limit).
5. **No deprecated constructs.**
   Avoid older APIs (explicitly disallowed).

## Workflow
1. Collect model and tools.
2. Define output schema type.
3. Create agent using current `create_agent(...)`.
4. Validate tool attaching and schema.
5. Invoke agent with structured inputs.

## Output Checklist
- [ ] Agent created with up-to-date APIs
- [ ] Tools explicitly listed
- [ ] Response format set
- [ ] Stop conditions defined
