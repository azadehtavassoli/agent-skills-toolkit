# VERSIONING POLICY

## Topic Versioning
- Each topic (`topics/<name>`) MUST follow semantic versioning.
- Breaking changes require major version increments.

## Framework Adapter Versioning
- Framework adapters under `topics/*/frameworks/*` MUST maintain independent semantic versions.
- Adapter version changes MUST map to compatible topic versions.

## Backward Compatibility
- Minor and patch releases MUST preserve existing public contracts.
- Any compatibility exceptions MUST be documented with migration notes.

## Deprecation Policy
- Deprecated interfaces MUST be announced with replacement guidance.
- Deprecations MUST include removal timeline and target version.
- Deprecated paths MUST remain test-covered until removal.
