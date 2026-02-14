# Skill: TESTING_POLICY

## Purpose
Define essential test requirements for reliable LLM agent code generation. Agents must drive testing coverage proactively.

## When to use
- After generating any non-trivial code (>2 LOC)
- Before merges
- After refactors
- For critical logic paths and integrations

## Hard Rules (MUST)
1. **Every new feature must include tests.**
   - Unit tests for logic
   - Integration tests for external dependencies
2. **Tests must be runnable with CI.**
   - No manual steps
   - No hidden environment assumptions
3. **Test outputs must be deterministic.**
   - Seed randomness
   - Mock external dependencies
4. **Test failures must be explicit.**
   - No “expected failures.”
   - Every failure must indicate a fix.

## Soft Preferences (SHOULD)
- Prefer property-based tests for complex logic.
- Prefer snapshot tests only where deterministic.

## Anti-patterns
- Tests that depend on ephemeral network access.
- Tests that implicitly assume state.
- Only testing “happy path.”

## Workflow
1. Identify new logic paths from code generation.
2. Write unit tests with clear assertions.
3. Add integration tests for tool calls (mock external APIs).
4. Run locally and in CI.
5. Verify coverage thresholds.

## Output Checklist
- [ ] All new functions have tests
- [ ] Tests pass locally and in CI
- [ ] Determinism enforced in tests
- [ ] Mocks used for external systems

## Notes
Tests anchor the correctness contract for generated code.
