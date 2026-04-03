# Prompt Template — Create Frontend Test Batch

You are implementing a frontend/admin UI batch in a production-grade system.

Requirements:
1. Implement the UI.
2. Implement all relevant states:
   - idle
   - loading
   - success
   - error
   - empty
   - unauthorized if relevant
3. Add component/integration tests.
4. Add Playwright E2E for the page-level flow.
5. Use semantic locators.
6. Ensure validation is runnable via CLI.
7. Update the batch status file before finishing.

Return:
- files changed
- UI states covered
- tests added
- commands run
- pass/fail summary
- evidence paths
- exact status file update
