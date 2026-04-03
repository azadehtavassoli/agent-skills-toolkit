# Testing Topic

## Purpose

This topic defines the testing operating model for agent-built software.

It is intended for backend-first, production-oriented systems where correctness must be demonstrated through repeatable automated validation rather than manual inspection.

This topic covers:

- backend testing
- frontend testing
- Playwright end-to-end automation
- test data and fixtures
- CI test execution
- evidence and status reporting

## Core philosophy

A feature is not complete because code exists.
A feature is complete only when the relevant automated tests pass and evidence is recorded.

## Non-negotiable rules

1. No fixed sleeps in tests.
2. Prefer deterministic fixtures over live external dependencies.
3. Backend logic must be validated through unit, service, and API tests.
4. Frontend logic must be validated through component and integration tests.
5. Real browser user flows must be validated through Playwright for page-level features.
6. Every major batch must produce machine-runnable validation via CLI.
7. Every major batch must update its status file with:
   - what was implemented
   - what was tested
   - what passed
   - what remains risky

## Required testing layers

### Backend
- unit tests
- repository tests
- service tests
- API tests
- graph topology tests
- graph behavior tests
- workspace isolation tests

### Frontend
- unit tests
- component tests
- page integration tests
- Playwright E2E tests
- optional visual regression tests

## State coverage rule

Every user-facing feature must explicitly handle these states where applicable:

- idle
- loading
- success
- error
- empty
- unauthorized

Tests must validate these states.

## Evidence rule

A task is not done unless evidence exists.

Examples of valid evidence:
- pytest output
- vitest output
- Playwright HTML report
- screenshot
- trace file
- status batch file update

## CLI-first rule

All test flows must be executable via CLI commands.
Do not rely on IDE-only or browser-only manual validation.

## Recommended subtopics

- backend_testing
- frontend_testing
- playwright
- test_data_and_fixtures
- ci_test_execution