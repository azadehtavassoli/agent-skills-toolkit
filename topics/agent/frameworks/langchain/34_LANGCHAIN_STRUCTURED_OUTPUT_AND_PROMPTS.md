# Skill: LANGCHAIN_STRUCTURED_OUTPUT_AND_PROMPTS

## Purpose
Define how to enforce structured agent outputs and schema-aware prompts so downstream systems can parse and consume results reliably.

## When to use
- Any time agent returns structured data
- Integrating agent results into systems
- When outputs drive workflows or state machines

## Hard Rules (MUST)
1. **Always use response schema types.**
   Passing a Pydantic model yields deterministic outputs. :contentReference[oaicite:9]{index=9}
2. **Prefer ProviderStrategy when model supports it.** :contentReference[oaicite:10]{index=10}
3. **Fallback to ToolStrategy when needed.**

## Workflow
1. Define output schema.
2. Pass it to `response_format`.
3. Validate structured_response.
4. Store or route output programmatically.

## Output Checklist
- [ ] Output schema chosen
- [ ] Output validated
- [ ] Response stored if needed
