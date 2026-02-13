# Skill: LANGCHAIN_MULTI_AGENT_AND_ORCHESTRATION

## Purpose
Provide structured practices for coordinating multiple agents or agent steps into a workflow using LangChain and its runtime abstractions (such as LangGraph).

## When to use
- Complex decision processes
- Long-running sequences
- Conditional agent handoffs

## Hard Rules (MUST)
1. **Define each agent role clearly.**
2. **Use orchestrators for workflow execution.** :contentReference[oaicite:11]{index=11}
3. **Define handoff data schemas.**
4. **Terminate workflows explicitly.**

## Workflow
1. Decompose task into agent sub-tasks.
2. Set role, schema, and handoff rules.
3. Create workflow graph.
4. Validate execution.

## Output Checklist
- [ ] Roles defined
- [ ] Handoff schema present
- [ ] Workflow termination conditions
