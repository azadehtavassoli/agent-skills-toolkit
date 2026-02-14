# Skill: SETTINGS_AND_ENVIRONMENT

## Purpose
Enforce consistent and testable configuration management through typed settings objects. Avoid hardcoded values and make configuration overrideable in tests/CI.

## When to use
- Application startup
- Injecting settings into services
- Test environments

## Hard Rules (MUST)
1. **Use Pydantic Settings for config.**
   - Pull from env vars, `.env`, or secret store. :contentReference[oaicite:4]{index=4}
2. **Do not hardcode secrets or environment config.**
3. **Make settings injectable via DI.**
4. **Use caching for settings to avoid overhead.**

## Soft Preferences (SHOULD)
- Group related config (DB, auth, API keys) logically.
- Use strict type annotations.

## Anti-patterns
- Globals with hardcoded values.
- Reading env within functions directly.

## Workflow
1. Define Settings class with required attributes.
2. Read from `env_file` and environment.
3. Provide via `Depends()` to services.
4. Override in tests using `dependency_overrides`.

## Output Checklist
- [ ] Settings declared via typed object
- [ ] No hardcoded secrets
- [ ] DI configured for settings
- [ ] Overrides exist for tests
