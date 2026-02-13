# Skill: LANGCHAIN_MEMORY_AND_EVALUATION

## Purpose
Provide structured patterns for memory usage and evaluation of agentic systems, including short-term and long-term memory scopes.

## When to use
- Tracking conversational history
- Persisting state across interactions
- Evaluating behavior via structured traces

## Hard Rules (MUST)
1. **Memory must be explicit.**
   Avoid silent or implicit state retention. :contentReference[oaicite:5]{index=5}
2. **Use persistence as needed.**
   Long-term memories require external storage, not ephemeral context. :contentReference[oaicite:6]{index=6}
3. **Evaluate behavior via traces.**
   Use LangSmith or equivalent for trajectory evaluation.

## Workflow
1. Decide memory scope (session vs persistent).
2. Attach memory constructs (graphs, indices).
3. Use evaluator or tracer to record runs.
4. Analyze traces with metrics.

## Output Checklist
- [ ] Memory configured
- [ ] Traces recorded
- [ ] Evaluation results documented
