# Playwright Instructions

## When to use
Use this topic for:
- page-level user workflows
- authenticated browser tests
- smoke tests
- critical admin flows
- visual regression
- browser-based evidence generation

## Core strategy
- most tests should bypass login using `storageState`, seeded cookies, or test session fixtures
- only a small number of tests should cover real in-app login UI
- external OAuth should run only in staging/nightly and controlled environments

## Hard constraints
- no fixed sleeps
- no brittle nth-child selectors
- prefer `getByRole`, `getByLabel`, `getByText`
- use `data-testid` only when necessary
- capture trace on failure
- capture screenshot on failure
- assert no console errors in critical paths

## Minimum E2E scenarios per page-level feature
- page load success
- core user action
- UI state change
- API interaction reflected in UI
- error handling
- unauthorized handling if relevant

## Required evidence
- Playwright command used
- pass/fail summary
- HTML report path
- trace path
- screenshot path if any
