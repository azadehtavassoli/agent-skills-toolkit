# Project Copilot Instructions (Template)

## Source of Truth
- Link or path to the single canonical design, spec, or repo section that defines project goals (replace this placeholder).

## Non-negotiables
- List the project-specific, mandatory constraints here (e.g., supported Python versions, required security controls).

## Core Standards
All repo core standards apply to this project. In particular, the following core standards are always enforced:

- `core/CODE_READABILITY.md` (Code Readability — module & function docstrings, comment guidance)
- `core/GLOBAL_RULES.md`
- `core/LOGGING_STANDARD.md`

Use this template to point reviewers to which core overlays are required for PR approval.

## Project-specific Guidance
- Short bullet list of conventions unique to this project (naming, small architecture notes).

## Review Checklist (paste into PR description)
- [ ] Follows Core Standards (see Core Standards section)
- [ ] Module and function docstrings present for changes (per CODE_READABILITY)
- [ ] High-signal comments added only where needed
