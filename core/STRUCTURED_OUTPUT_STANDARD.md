# STRUCTURED OUTPUT STANDARD

## Core Requirements
- All structured outputs MUST use Pydantic `BaseModel` definitions.
- Raw `dict` outputs are prohibited for public interfaces.
- Schema validation is mandatory at boundaries.
- Models MUST be explicitly named, versioned when needed, and documented.

## Enforcement
- Framework adapters MUST expose typed request and response models.
- Parsing failures MUST return explicit typed errors.
- Tests MUST validate successful and failing schema paths.
