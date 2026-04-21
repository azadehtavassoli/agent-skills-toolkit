# Scenario Schema Guidance

## Purpose
Use a structured scenario contract instead of hardcoding flows in Playwright test files.

## Recommended model
Scenario package:
- `brief.md`
- `scenario.json`
- optional `seed.json`
- optional `captions.json`
- optional `voiceover.md`

## scenario.json fields
Recommended top-level fields:
- `id`
- `title`
- `audience`
- `objective`
- `coreMessage`
- `startUrl`
- `viewport`
- `seedProfile`
- `recording`
- `steps`
- `captions`
- `highlights`
- `outputs`

## Step contract
Each step should include:
- `id`
- `type`
- step-specific fields

Supported step types should be explicit and versioned.
Do not allow arbitrary executable blobs in scenario config.

## Validation rules
- no duplicate step ids
- all step references must resolve
- outputs must declare profile/format/aspect ratio
- selectors/text assertions must be non-empty when required
- scenario id and folder name should match
