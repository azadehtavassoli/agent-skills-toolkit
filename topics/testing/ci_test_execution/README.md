# CI Test Execution

## Purpose

Define what test layers run in CI and when.

## Pull Request / Commit pipeline

Run:
1. typecheck
2. lint
3. backend unit/service/API tests relevant to changed area
4. frontend component/integration tests
5. Playwright smoke suite

Retain artifacts on failure:
- Playwright report
- screenshot
- trace
- video if enabled

## Merge to main

Run:
1. full backend test suite or expanded changed-area suite
2. full frontend component/integration suite
3. Playwright critical suite
4. optional visual regression

## Nightly

Run:
1. full Playwright suite
2. visual regression suite
3. optional staging-backed auth/OAuth checks
4. long-running or expensive scenarios

## Required CLI commands

Examples:
- `pytest backend/tests -v`
- `npm run typecheck`
- `npm run test:component`
- `npm run test:e2e:smoke`
- `npm run test:e2e:critical`

## Reporting rule

Every batch must document:
- commands run
- pass/fail summary
- artifacts produced
- known blockers