# Skill: VERSIONING_POLICY

## Purpose
Prevent AI coding agents from generating code that depends on the wrong library versions, deprecated APIs, or unpinned dependencies. Ensure outputs are reproducible and compatible with the project’s declared environment.

## When to use
- Any time adding/changing dependencies
- Any time generating code that uses third-party libraries/frameworks
- Any time refactoring code across major versions
- Any time tests fail due to import/API mismatches

## Inputs
- Project dependency manifest (one or more):
  - `pyproject.toml` (preferred), `poetry.lock`, `uv.lock`
  - `requirements.txt`, `requirements.lock`
  - `package.json`, `pnpm-lock.yaml`, `yarn.lock`, `package-lock.json`
  - `go.mod`, `Cargo.toml`, etc. (as applicable)
- Runtime constraints:
  - language/runtime version (e.g., Python/Node/Java)
  - target deployment platform (local, container, serverless)

## Hard rules (MUST)
1. **Never assume versions.** Always align code with the project’s declared dependency versions.
2. **Prefer lockfiles.** If a lockfile exists, treat it as source-of-truth over loose manifests.
3. **No “latest” language.** Do not say “use latest version” in code or docs. Use explicit version constraints.
4. **No deprecated APIs.**
   - If an API is deprecated or removed in the pinned version range, do not use it.
   - If unsure, require verification via official docs or local introspection (see Workflow).
5. **Pin or constrain dependencies.**
   - For applications: pin exact versions (or use a lockfile).
   - For libraries: use compatible ranges and test against supported versions.
6. **If code requires a newer API:** update the version constraints + document the change + add tests.
7. **No silent breaking changes.** Any dependency upgrade that can affect runtime behavior must be called out in CHANGELOG/PR description.

## Soft preferences (SHOULD)
- Prefer stable, maintained major versions.
- Prefer official migration guides when upgrading across major versions.
- Prefer minimal, incremental upgrades over large jumps.
- Prefer feature detection / compatibility layers when supporting multiple versions.

## Workflow (step-by-step)
1. **Locate the source of truth**
   - Identify the dependency file(s) and lockfile(s).
   - Record the exact versions that matter for the code you’re about to write.
2. **Confirm API availability**
   - Prefer one of:
     - Official documentation for that exact major/minor version
     - Local introspection / type hints / IDE autocomplete
     - Existing imports/usages in the repo
3. **Generate code aligned to pinned versions**
   - Use only imports and APIs available in those versions.
4. **If mismatch happens (import error / attribute error)**
   - Do not “guess and patch”.
   - Re-check pinned versions and adjust code to match.
   - If the project truly needs the newer API:
     - Update constraints/lockfile
     - Add/adjust tests
     - Document the upgrade
5. **Add a verification step**
   - Add/extend tests to cover the new behavior.
   - Ensure CI or local tests validate against the intended environment.

## Common failure modes (Anti-patterns)
- Using APIs from blog posts/tutorials without checking versions.
- Writing code that compiles only on your machine due to unpinned deps.
- “Fixing” errors by changing random imports until it works.
- Mixing patterns across major versions (Franken-code).
- Suggesting “pip install -U <pkg>” as the default fix.

## Output checklist
- [ ] Code uses only APIs available in the project’s declared versions
- [ ] Dependencies are pinned or locked appropriately
- [ ] Any upgrades are explicit and documented
- [ ] Tests cover the change and pass in the target environment
- [ ] No deprecation warnings introduced (or they’re explicitly handled)

## Notes for integration
Project-specific version details MUST live in the target project repo (e.g., `PROJECT_ADAPTER.md`). This skill remains project-agnostic and defines the policy and process only.
