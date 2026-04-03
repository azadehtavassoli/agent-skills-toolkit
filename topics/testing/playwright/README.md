# Playwright

## Purpose

This topic defines how to implement and run deterministic browser automation for production-grade UI validation.

## Scope

Use Playwright for:
- end-to-end testing
- smoke tests
- critical path validation
- auth/session-aware testing
- visual regression
- browser evidence generation

## Required folder structure

frontend/tests/
- e2e/
- auth/
- smoke/
- critical/

## Core rules

1. No fixed sleeps.
2. Use semantic locators first.
3. Use storageState for most authenticated flows.
4. Avoid real external OAuth in normal CI.
5. Capture traces on failure.
6. Capture screenshots on failure.
7. Prefer deterministic test data.

## Locator rules

Prefer:
- page.getByRole()
- page.getByLabel()
- page.getByText()

Use `data-testid` only when necessary.

## Minimum scenarios per page-level feature

- page loads successfully
- core user action works
- state change is visible
- API-backed behavior is reflected in UI
- error path works
- unauthorized path works if relevant

## Required evidence

On failure retain:
- trace
- screenshot
- video if enabled

On success, report:
- test commands
- passed scenarios
- known limitations