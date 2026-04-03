# Backend Testing Instructions

## When to use
Use this topic whenever the task changes:
- API routes
- services
- repositories
- workflow graphs
- auth or permission logic
- tenant/workspace boundaries
- quota, policy, or retention enforcement

## Required deliverables
- test coverage proportional to the change
- updated or new pytest files
- CLI-runnable commands for validation
- updated status file
- implementation report

## Required test types
Choose all that apply:
- unit tests
- repository tests
- service tests
- API tests
- graph topology tests
- graph behavior tests
- isolation tests

## Hard constraints
- do not rely on manual curl checks only
- do not skip auth/permission tests for protected routes
- do not skip isolation tests for scoped data
- do not use real third-party systems in normal CI unless the task explicitly requires it

## Evidence required
- executed pytest command(s)
- pass/fail summary
- relevant logs or output
- status file update

## Report back format
- what changed
- what tests were added
- what commands were run
- whether all tests passed
- remaining risks
