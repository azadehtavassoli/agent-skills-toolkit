# Skill: LANGCHAIN_MIDDLEWARE_AND_CONTROL

## Purpose
Define how to attach control logic and monitoring hooks during agent execution using LangChain’s middleware constructs.

## When to use
- To balance context size
- To add retry/fallback logic
- To sanitize inputs/outputs
- To add human-in-the-loop controls

## Hard Rules (MUST)
1. **Middleware controls agent loops.**
   Attach each concern as middleware. :contentReference[oaicite:7]{index=7}
2. **Summarization middleware for context management.**
3. **Human-approval middleware for high-risk steps.** :contentReference[oaicite:8]{index=8}
4. **Never mix core logic with middleware concerns.**

## Workflow
1. Choose concerns (summarization, guardrails, tracing).
2. Attach middleware when creating agent.
3. Validate middleware interactions.
4. Analyze behavior via logs or evaluation.

## Output Checklist
- [ ] Middleware configured
- [ ] Logging present
- [ ] Guardrails effective
