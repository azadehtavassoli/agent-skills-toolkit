# Skill: LANGCHAIN_TOOL_CALLING_PATTERNS

## Purpose
Ensure agentic code uses consistent, explicit tool calling conventions supported by LangChain. Tools are first-class citizens and integral to structured reasoning.

## When to use
- Any time an agent needs external data or actions
- When parsing model output into structured actions
- Building interfaces between model outputs and world effects

## Hard Rules (MUST)
1. **Declare all tools explicitly in agent definition.** :contentReference[oaicite:4]{index=4}
2. **Use valid input/output type definitions.**
3. **Agent must choose tools before invocation.**
4. **Validate the tool’s response before using it.**

## Workflow
1. Define each tool using `@tool` or equivalent factory.
2. Annotate inputs/outputs for clarity.
3. Add tools in `create_agent(..., tools=[...])`.
4. Structure agent logic to reason about tool use.
5. Validate tool results before downstream logic.

## Output Checklist
- [ ] Tools listed in agent setup
- [ ] Inputs/outputs defined
- [ ] Validation step after tool call
