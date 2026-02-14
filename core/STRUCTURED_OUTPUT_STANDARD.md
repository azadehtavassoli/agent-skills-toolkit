# Structured Output Standard

## Pydantic requirement
1. Structured outputs MUST use `pydantic.BaseModel`.
2. Public conversion interfaces MUST return typed models, not unstructured dictionaries.
3. Metadata fields MUST be explicit and documented.

## Validation guidance
- Validate all required fields at model boundaries.
- Keep output shapes stable for downstream automation.
