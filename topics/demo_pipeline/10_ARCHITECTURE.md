# Demo Pipeline Architecture

## Objective
Create a deterministic system for generating repeatable, high-quality product demos.

## Layered model
1. Human brief
2. Machine scenario
3. Seed/bootstrap state
4. Playwright operator
5. Artifact manifest
6. Remotion render profiles

## Recommended contracts
### Human layer
`brief.md`
- goal
- audience
- message
- story
- hero moment
- constraints

### Machine layer
`scenario.json`
- id/title
- start URL
- viewport
- seed profile
- step list
- capture directives
- captions/highlights
- output profiles

### Seed layer
`seed.json` or seed script
- workspace
- users
- connected-state fixtures
- source data/messages/documents
- expected answerable state

### Capture layer
`timeline.json`
- step timing
- artifact names
- key milestones

### Render layer
profile config
- aspect ratio
- intro/outro settings
- captions enabled/disabled
- highlight style

## Preferred runtime modes
- local deterministic
- shared demo/staging deterministic
- optional production-proof mode for very targeted flows
