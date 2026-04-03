# Testing Checklists

## Backend feature completion checklist
- [ ] unit tests added where needed
- [ ] service tests added where needed
- [ ] API tests added for public route changes
- [ ] auth/permission tests added
- [ ] workspace/tenant isolation tested if applicable
- [ ] CLI validation command documented
- [ ] status batch file updated

## Frontend feature completion checklist
- [ ] UI implemented
- [ ] idle state handled
- [ ] loading state handled
- [ ] success state handled
- [ ] error state handled
- [ ] empty state handled
- [ ] unauthorized state handled if applicable
- [ ] component/integration tests added
- [ ] Playwright E2E added
- [ ] no-console-error assertion added to critical path
- [ ] build + typecheck pass
- [ ] status batch file updated

## Playwright readiness checklist
- [ ] semantic locators available
- [ ] auth fixture or storageState available
- [ ] test data deterministic
- [ ] no fixed sleeps
- [ ] traces retained on failure
- [ ] screenshots retained on failure
- [ ] smoke and critical grouping defined

## CI readiness checklist
- [ ] typecheck command exists
- [ ] component test command exists
- [ ] Playwright smoke command exists
- [ ] Playwright critical/full command exists
- [ ] artifacts uploaded on failure
- [ ] nightly/full strategy defined
