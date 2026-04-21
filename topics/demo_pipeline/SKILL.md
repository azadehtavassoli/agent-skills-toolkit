# Demo Pipeline — SKILL

## What this skill is for
Use this skill to implement a long-term, maintainable demo pipeline for product demos.
The aim is to create a reusable machine for demos, not a one-off screen recording.

## Canonical design
A good demo pipeline has these responsibilities:

### 1. Scenario definition
A scenario defines:
- objective
- audience
- core message
- preconditions
- interaction steps
- hero moment
- output profiles

Use:
- `brief.md` for human-readable story and intent
- `scenario.json` for machine-readable execution

### 2. Seeded/demo-mode state
Use one of these modes:
- real mode
- seeded mode
- mock-assisted mode

Default to seeded mode for investor/social demos.
This gives stable results without forcing live third-party auth on every run.

### 3. Playwright execution
Playwright is the deterministic operator.
It should:
- log in or bootstrap state
- navigate the app
- perform actions
- wait for stable UI conditions
- capture screenshots/video/events
- emit structured run metadata

### 4. Structured capture
Do not rely only on a raw video file.
Also emit:
- timeline metadata
- step artifacts
- key screenshots
- scenario run manifest

### 5. Remotion rendering
Remotion should:
- read scenario metadata and raw artifacts
- add titles/captions/highlights
- produce profile-specific outputs
- keep styling reusable and parameterized

## Preferred directory structure
```text
.github/agent-skills-toolkit/topics/demo_pipeline/
demo/
  scenarios/
  seeds/
  playwright/
  remotion/
  output/
  scripts/
```

## Scenario structure guidance
Recommended scenario package:
```text
demo/scenarios/<scenario-id>/
  brief.md
  scenario.json
  seed.json
  captions.json
  voiceover.md
```

## Implementation sequencing
### Phase 1 — foundation
- scenario schema
- scenario validator
- seed loader
- Playwright runner scaffold
- output manifest contract

### Phase 2 — deterministic app support
- demo mode hooks
- seeded connected state
- stable selectors
- fixed viewport and timing defaults

### Phase 3 — render layer
- Remotion root
- reusable overlays
- one composition profile
- render command

### Phase 4 — profile expansion
- investor landscape
- landing-page short
- social vertical
- optional YC-specific profile

## Testing expectations
Minimum test layers:
- unit tests for scenario parsing/validation
- integration tests for seed loading
- Playwright scenario test
- render smoke test
- end-to-end test that proves the pipeline produces output artifacts

## Common mistakes to avoid
- coupling demo execution to live OAuth
- burying scenario logic inside test code only
- lacking typed schema validation
- making the pipeline depend on one-off manual UI conditions
- leaving captions/highlights hardcoded in renderer without scenario metadata
- treating raw Playwright video as final polished output
