# Skill: MULTI_AGENT_DESIGN

## Purpose
Guide the design of multi-agent systems that decompose complex workflows into specialized roles with reliable coordination and communication.

## When to use
- Tasks require parallelism, specialized sub-tasks, or iterative refinement.
- Workflows are too large for one agent context alone.

## Hard Rules (MUST)
1. **Assign clear agent roles.**
   - Each agent must have a unique responsibility.
2. **Define communication contracts.**
   - Agents pass structured data (not free text) between steps.
3. **Define orchestration workflow.**
   - Sequence of agent invocations must be explicit.
4. **Ensure termination at workflow end.**
   - No agent runs past its design scope.

## Soft Preferences (SHOULD)
- Use a supervisor or router to manage agent handoffs.
- Keep agent contexts minimal per task.

## Anti-patterns
- Agents sharing large unscoped context blobs.
- Unbounded agent calls without clear end.

## Workflow
1. List sub-tasks for the broader objective.
2. Assign roles to agents.
3. Define data schemas passed between agents.
4. Define the orchestration mechanism.
5. Evaluate end-to-end workflow via concrete examples.

## Output Checklist
- [ ] Agent roles defined
- [ ] Communication contract schemas
- [ ] Orchestration sequence
- [ ] Termination criteria
