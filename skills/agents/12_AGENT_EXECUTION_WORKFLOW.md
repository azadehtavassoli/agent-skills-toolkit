# Skill: AGENT_EXECUTION_WORKFLOW

## Purpose
Define the actionable steps in agent execution: planning, step execution, evaluation, fallback, and stopping.

## When to use
- During agent implementation or prompt design
- When coordinating multiple tools

## Hard Rules (MUST)
1. **Step execution is atomic.**
   - Each action is standalone, with clear inputs/outputs.
2. **Monitor and evaluate intermediate outputs.**
3. **Define fallback on failure.**
   - If a step fails, agent must retry or bail gracefully.
4. **Tool results are validated before use.**

## Workflow
1. Plan next step based on current state.
2. Invoke a tool or reason.
3. Validate outcomes.
4. Decide next action.
5. Stop if goal reached or max steps exceeded.

## Output Checklist
- [ ] Atomic steps
- [ ] Validation of outputs
- [ ] Explicit fallback logic
- [ ] Clear termination conditions
