# Testing Agent Rules

## Purpose
These rules are mandatory for any coding agent working on testing-related changes.

## Global rules
1. A task is not complete because code exists. It is complete only when the required tests pass and evidence is recorded.
2. Do not use fixed sleeps in tests.
3. Prefer deterministic fixtures over live external dependencies.
4. Prefer CLI-runnable validation over manual-only validation.
5. Update the relevant `status_batch_XX.md` file for every batch.
6. Preserve backend-first architecture. Do not move backend policy logic into the frontend.

## Backend rules
- Add or update unit, service, API, and isolation tests where applicable.
- If a feature is workspace- or tenant-scoped, add isolation tests.
- Do not assume repository filters are correct without tests.

## Frontend rules
- A frontend feature is not complete unless component/integration tests exist.
- Every page-level feature must have at least one Playwright E2E test.
- All relevant states must be implemented and tested: idle, loading, success, error, empty, unauthorized.
- Use semantic locators first: `getByRole`, `getByLabel`, `getByText`.
- Use `data-testid` only when semantic locators are impractical.

## Playwright rules
- Use `storageState` or seeded sessions for most authenticated tests.
- Do not use real external OAuth in regular E2E or CI.
- Capture trace, screenshot, and report on failure.
- Assert no browser console errors in critical flows.

## Reporting rules
Every implementation report must include:
- files created/changed
- tests added/updated
- commands run
- pass/fail summary
- evidence paths
- known limitations
