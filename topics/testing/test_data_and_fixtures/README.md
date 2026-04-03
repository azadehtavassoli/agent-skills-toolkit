# Test Data and Fixtures

## Purpose

Tests must use deterministic data and isolated state.

## Rules

1. Prefer seeded local test users over ad hoc accounts.
2. Prefer seeded workspaces over dynamic global shared state.
3. Use dedicated test sessions or storageState for frontend E2E.
4. Reset mutable state between tests where practical.
5. Do not depend on live external systems in normal CI.

## Recommended fixture categories

### Backend
- test users
- test workspaces
- auth headers
- seeded connections
- seeded quota policies
- seeded usage events

### Frontend
- storageState admin
- storageState regular user
- unauthorized session fixture
- mocked API responses for component/integration tests

## Naming guidance

Examples:
- `admin_user`
- `viewer_user`
- `workspace_alpha`
- `workspace_beta`
- `vip_policy_fixture`

## Isolation rule

A test must not depend on the outcome of another test.
If a feature is workspace-scoped, fixtures must make workspace boundaries explicit.