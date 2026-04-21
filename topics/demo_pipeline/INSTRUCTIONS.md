# Demo Pipeline — INSTRUCTIONS

## Purpose
Use this topic when the task involves building, extending, or validating a deterministic demo generation system for the product.
This includes investor demos, YC demos, landing-page demos, social clips, scenario runners, seeded demo mode, Playwright-driven flows, and Remotion-based final rendering.

## Goal
Build a repeatable demo system that can:
- start from a structured scenario;
- prepare deterministic app state;
- execute the scenario through the real UI when appropriate;
- capture raw artifacts;
- render polished final outputs;
- validate the result end-to-end.

## Default architecture
Use a five-layer model:
1. scenario definition
2. seeded/demo-mode state preparation
3. Playwright execution
4. structured capture output
5. Remotion rendering and output profiles

## Hard rules
- Do not require live third-party OAuth for standard demo execution unless the connection flow itself is the demo objective.
- Keep demo behavior explicit and off by default in normal production operation.
- Validate all scenario inputs against a schema before execution.
- Prefer seeded or simulated connected state for stable demos.
- Keep scenario narrative separated from low-level UI execution steps.
- Add end-to-end validation before marking a batch complete.

## Required repository outputs
A non-trivial demo-pipeline task should generally produce or update:
- scenario schema and validator
- scenario examples/templates
- seed fixtures or seed loader
- Playwright runner or action library
- Remotion renderer or composition adapters
- docs/playbook updates
- end-to-end tests and validation commands

## Required validation
At minimum:
- schema validation test
- scenario execution smoke test
- seeded state preparation test
- output artifact existence/shape test
- rendered output validation if rendering is in scope

## Reporting requirements
Implementation reports must state:
- which scenario contracts were introduced or changed
- whether demo mode or seeded state was added/changed
- which scenarios were executed end-to-end
- what artifacts were produced
- whether any step still depends on manual polishing
