# Skill: ERROR_RESPONSES_AND_LOGGING

## Purpose
Ensure consistent error handling and structured logging across all FastAPI routes, middleware, and services. Prevent leaks of internal state and encourage observable systems.

## When to use
- Returning errors to clients
- During exception handling
- Recording request/response activity

## Hard Rules (MUST)
1. **Standardize error response schema.**
   - Always return HTTP status code + structured JSON: `{ code, message, details? }`.
2. **Use custom exceptions for domain logic.**
   - Do not raise raw framework or database errors to clients. :contentReference[oaicite:2]{index=2}
3. **Register global handlers.**
   - Catch domain exceptions and map to HTTP responses in one place.
4. **Log errors with context and stack info.**
   - Include path, method, params, error type.
5. **Structured logging only (JSON or similar).**
   - Avoid free-form strings in logs.

## Soft Preferences (SHOULD)
- Use `HTTPException` for expected HTTP status errors. :contentReference[oaicite:3]{index=3}
- Use middleware for request/response logging.
- Mask sensitive fields in logs (tokens, passwords).

## Anti-patterns
- Logging only, no structured context.
- Returning untyped error messages to clients.
- Raising internal exceptions outside handlers.

## Workflow
1. Define base application exception types.
2. Register exception handlers in app startup.
3. Wrap service layer errors into domain exceptions.
4. Log with structured format before returning response.

## Output Checklist
- [ ] Custom exception types defined
- [ ] Global exception handlers registered
- [ ] Errors logged with context
- [ ] Clients receive structured error schema
