# Global Rules

These rules are deterministic and apply to all topic and framework assets in this repository.

## Deterministic engineering requirements
1. Default behavior MUST be deterministic and reproducible.
2. Optional non-deterministic features (such as LLM interpretation) MUST be opt-in and clearly isolated.
3. All interfaces SHOULD define typed inputs and outputs.
4. All new templates MUST cite and follow:
   - `core/LOGGING_STANDARD.md`
   - `core/TESTING_STANDARD.md`
   - `core/STRUCTURED_OUTPUT_STANDARD.md`

## Governance requirements
- Document topic capabilities in a compliance checklist before implementation templates.
- Keep framework instructions aligned to topic-level hard rules.
- Validate requirements through tests and contract checks.
