# Frontend Testing

## Purpose

This topic defines how frontend features must be tested in a production-grade, agent-friendly workflow.

## Recommended stack

- Vitest
- React Testing Library
- optional MSW for mocked API responses
- Playwright for real browser flows

## Testing layers

### Unit tests
Use for:
- formatting helpers
- client-side validation
- small hooks
- pure UI logic

### Component tests
Use for:
- reusable components
- widgets
- forms
- tables
- dialogs
- state-specific rendering

### Integration tests
Use for:
- page-level logic
- multi-component interaction
- mocked API-backed flows
- route-aware UI state changes

### E2E tests
Use Playwright for:
- real browser flows
- authenticated pages
- admin actions
- persistence confirmation
- navigation correctness

## Mandatory locator rules

Always prefer:
- getByRole
- getByLabelText / getByLabel
- getByText

Use `data-testid` only when semantic locators are not practical.

Do not use brittle CSS selectors unless unavoidable.

## Mandatory state contract

Every page/feature must explicitly handle:
- idle
- loading
- success
- error
- empty
- unauthorized if relevant

These states must be tested.

## Frontend completion rule

A frontend feature is not complete unless:
- UI is implemented
- all relevant states exist
- API integration works
- component/integration tests pass
- Playwright test exists for the feature flow
- no console errors appear in tested flows
- status batch file is updated