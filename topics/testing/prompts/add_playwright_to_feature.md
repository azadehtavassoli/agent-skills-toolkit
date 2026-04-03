# Prompt Template — Add Playwright to Feature

Add Playwright coverage for an existing page-level feature.

Requirements:
- prefer semantic locators
- use storageState or seeded auth for most tests
- include success path
- include error path
- include unauthorized path if relevant
- assert no console errors in the critical path
- generate CLI-runnable commands
- update status file

Return:
- spec files added
- fixtures/storageState used
- scenarios covered
- commands run
- evidence paths
