# Skill: AGENT_ARCHITECTURE

## Purpose
Define foundational patterns used in agentic systems: agent goals, context management, reasoning loops, tool invocation, and termination conditions.

## When to use
- Designing any autonomous AI agent or agent workflow
- Decomposing complex tasks into actionable steps
- Ensuring coherence and safety in multi-step decisions

## Hard Rules (MUST)
1. **Every agent has a clear goal.**
   - Define the goal in unambiguous terms.
2. **Context must be explicit and scoped.**
   - Only include information the agent needs at each step.
3. **Agent loops follow: observe → reason → act → evaluate → stop.**
4. **Stop conditions must be explicit.**
   - Avoid infinite loops; set iteration limits or goal checks.
5. **Tools must be declared before use.**
   - Each invocation must state which tool & inputs first.

## Soft Preferences (SHOULD)
- Prefer modular reasoning steps over monolithic prompts.
- Prefer step annotations to clarify decisions.

## Anti-patterns
- Long, unfocused context windows with irrelevant data.
- Implicit tool use not defined in skill patterns.

## Workflow
1. Define agent goal with examples.
2. Structure context into chunks relevant to each step.
3. Design tool invocation interfaces and contracts.
4. Define termination criteria early.
5. Validate through evaluation patterns.

## Output Checklist
- [ ] Clear goal definition
- [ ] Explicit context scoping
- [ ] Defined reasoning loop structure
- [ ] Termination conditions stated
- [ ] All tools declared
