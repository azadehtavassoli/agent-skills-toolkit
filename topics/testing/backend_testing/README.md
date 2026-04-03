# Backend Testing

## Purpose

This topic defines how to test backend behavior in a deterministic, production-oriented way.

It is designed for systems with:
- API routes
- services
- persistence/repositories
- workflow/graph orchestration
- workspace or tenant isolation
- policy enforcement

## Testing stack

Recommended:
- pytest
- pytest-asyncio
- httpx / FastAPI TestClient
- factory helpers or fixture builders
- mock or monkeypatch only where needed

## Required backend test layers

### 1. Unit tests
Use for:
- pure functions
- schema validation helpers
- small policy utilities
- routing helpers
- formatting helpers

### 2. Repository tests
Use for:
- query correctness
- workspace scoping
- filtering behavior
- upsert behavior
- transaction expectations

### 3. Service tests
Use for:
- orchestration logic
- policy enforcement
- fallback behavior
- structured error handling

### 4. API tests
Use for:
- request validation
- auth protection
- HTTP status correctness
- response schema correctness
- route-to-service integration

### 5. Graph tests
Use for:
- topology validation
- deterministic routing behavior
- failure handling
- state transitions
- bounded retry loops

### 6. Isolation tests
Mandatory when data is workspace- or tenant-scoped.
Test that user A / workspace A cannot see data from user B / workspace B.

## Required assertions

Backend tests should validate:
- happy path
- invalid input
- unauthorized access
- forbidden access
- empty result behavior
- error behavior
- isolation boundaries

## Anti-patterns

Do not:
- rely only on manual curl checks
- skip auth tests on protected routes
- assume workspace_id filtering exists without tests
- use real third-party systems in normal CI
- allow silent fallbacks without explicit assertions

## Batch completion rule

A backend feature is not complete unless:
- unit/service/API tests exist where appropriate
- isolation is tested if the feature is scoped
- CLI validation commands are documented
- batch status file is updated