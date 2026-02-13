# Skill: GLOBAL_ENGINEERING_RULES

## Purpose
Define absolute engineering guardrails for agentic code generation. These rules apply everywhere and should never be violated by any AI coding agent.

## When to use
- Every code generation session
- Dependency management
- Architecture decisions
- Tests and QA
- Security policy alignment

## Hard Rules (MUST)
1. **Deterministic outputs.** Every task must produce fully reproducible code with no random/unbounded decisions.
2. **Never invent APIs.** Do not use classes/functions that don’t exist in pinned package versions.
3. **No silent failures.** Code must always handle errors explicitly; never assume an exception won’t happen.
4. **Tool calls must be explicit.** Any call to external APIs, DBs, or systems must be clearly declared.
5. **Avoid hallucination.** Do not speculate about behavior, versions, or outcomes without explicit evidence.
6. **No partial code.** Only complete, runnable functions/classes with imports and tests.

## Soft Preferences (SHOULD)
- Prefer composable modules over monolithic code.
- Prefer minimal external dependencies.
- Prefer modern language idioms consistent with latest stable practices.

## Anti-patterns
- Generating pseudo-code or TODO stubs.
- Copying patterns from blogs without version alignment.
- Mixing async + sync without rationale.

## Output Checklist
- [ ] Code compiles/runs
- [ ] Imports match declared dependencies
- [ ] No deprecated API usage
- [ ] Clear and complete error handling
- [ ] Explicit tool/API integration

## Notes
Use this as the highest-priority policy the agent must never violate.
