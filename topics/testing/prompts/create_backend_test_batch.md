# Prompt Template — Create Backend Test Batch

You are implementing a backend batch in a production-grade system.

Follow these rules:
1. Preserve backend-first architecture.
2. Add the correct automated tests for the scope:
   - unit
   - service
   - API
   - graph
   - isolation
3. If data is workspace- or tenant-scoped, add explicit isolation tests.
4. All validation must be runnable via CLI.
5. Update the batch status file before finishing.

Return:
- files changed
- tests added
- commands run
- pass/fail summary
- known risks
- exact status file update
