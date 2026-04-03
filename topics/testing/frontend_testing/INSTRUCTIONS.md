# Frontend Testing Instructions

## When to use
Use this topic whenever the task changes:
- React components
- pages
- stateful UI flows
- settings/admin screens
- API integration in the frontend
- route protection and unauthorized states

## Required deliverables
- UI implementation
- explicit state handling
- component/integration tests
- Playwright E2E for page-level features
- status file update
- implementation report

## Mandatory UI states
Every feature must explicitly handle and test:
- idle
- loading
- success
- error
- empty
- unauthorized if relevant

## Hard constraints
- do not ship a page without tests
- do not use fragile CSS selectors where semantic locators are available
- do not rely on manual browser checking as completion evidence
- do not leave console errors untested in critical flows

## Testing expectations
- use Vitest + React Testing Library for component/integration tests
- use Playwright for real browser flows
- mock unstable APIs in component/integration tests when needed
- keep browser E2E deterministic

## Evidence required
- executed test commands
- pass/fail summary
- Playwright report path if applicable
- trace/screenshot paths on failure
- status file update
