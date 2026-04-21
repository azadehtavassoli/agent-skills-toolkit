# Demo Pipeline End-to-End Validation

## Goal
Prove that the full pipeline works from scenario definition to final output artifact.

## Minimum validation matrix
1. Scenario schema validation
2. Seed/bootstrap validation
3. Playwright run validation
4. Raw artifact validation
5. Remotion render validation
6. Command-level smoke validation for the documented CLI commands

## Example validation expectations
- scenario loads successfully
- seed step completes without errors
- Playwright run reaches hero moment
- output directory contains manifest/timeline/raw artifacts
- render command produces the expected MP4 for at least one profile

## Definition of done
A demo batch is not done if it only compiles.
It must execute end-to-end and produce verified artifacts.
