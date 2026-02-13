# Skill: REVIEW_CHECKLIST

## Purpose
Define an agent-interpretation checklist to ensure code quality before committing/merging. Agents generate this checklist and verify it automatically.

## When to use
- After code generation
- Before CI runs
- During context switching sessions

## Hard Rules (MUST)
1. **Verify dependency versions.**
2. **Run full test suite.**
3. **Ensure no banned imports.**
4. **Check output schema matches expected.**
5. **Confirm error handling covers edge cases.**

## Soft Preferences (SHOULD)
- Check for comments explaining intent.
- Confirm logging on failure paths.
- Validate external tool output formats.

## Anti-patterns
- Ignoring tests with annotation “TODO fix later.”
- Soft skipping critical checks.
- Assuming defaults without validation.

## Workflow
1. List all modified/new code items.
2. For each item, apply the rules.
3. Flag any violation.
4. If clear, finalize commit; else generate fixes.

## Output Checklist (Agent-actionable)
- [ ] Versions aligned
- [ ] Tests passed
- [ ] No banned imports
- [ ] Outputs schema verified
- [ ] Error handling complete

## Notes
This checklist defines what the agent *must* present before concluding a task.
