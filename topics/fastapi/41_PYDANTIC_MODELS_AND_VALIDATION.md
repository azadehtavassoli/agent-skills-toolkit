# Skill: PYDANTIC_MODELS_AND_VALIDATION

## Purpose
Produce clean, strict, and reliable Pydantic models for input/output schemas, settings, and validation logic. Avoid silent coercion and inconsistent data shapes.

## When to use
- Defining request/response contracts
- Handling configuration/settings
- Writing validators for business rules

## Hard Rules (MUST)
1. **Use Pydantic v2 BaseModel/Settings** for all data contracts.  
2. **Strict validation by default.**  
   - Disallow extra fields unless explicitly permitted.
3. **Avoid silent type coercion.**  
   - Accept only explicit type transformations.
4. **Define domain invariants with custom validators.**  
   - Use `@model_validator` for cross-field logic.  
5. **Error messages must be clear and structured.**  
   - Include field path and rule details. :contentReference[oaicite:1]{index=1}

## Soft Preferences (SHOULD)
- Prefer field descriptions for auto API docs.
- Use standard naming conventions consistent with API consumers (snake_case for Python).

## Anti-patterns
- Overly loose models that accept arbitrary data.
- Ignoring validation errors by catching and suppressing them.

## Workflow
1. Create BaseModel for each API contract.
2. Add `ConfigDict` with strict settings.
3. Write custom validators for invariants.
4. Use same models in tests to validate behavior.

## Output Checklist
- [ ] All I/O schemas defined via Pydantic
- [ ] Strict mode enabled (no unwanted extras)
- [ ] Validators cover key domain rules
- [ ] Clear error messages on invalid input
