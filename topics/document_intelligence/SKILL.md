# Document Intelligence Skill

## Purpose
Convert unstructured documents into LLM-ready Markdown using MarkItDown, with deterministic defaults and governance-compliant wrappers.

References:
- `core/GLOBAL_RULES.md`
- `core/LOGGING_STANDARD.md`
- `core/TESTING_STANDARD.md`
- `core/STRUCTURED_OUTPUT_STANDARD.md`

## When to use
- You need a standard document-to-Markdown conversion path.
- You need deterministic conversion that does not require an LLM by default.
- You need optional visual/LLM interpretation mode behind an explicit flag.

## Hard MUST rules
1. Use binary streams only (`io.BytesIO` + `convert_stream`).
2. Default conversion mode MUST NOT require an LLM.
3. Visual/LLM interpretation mode MUST be explicit and optional.
4. All wrappers MUST write debug logs to file.
5. All typed outputs MUST use `pydantic.BaseModel`.
6. Tests MUST use stubs/fakes for LLM and framework integrations.

## Workflow
1. Validate request payload into a Pydantic request model.
2. Build a binary stream from `content_bytes`.
3. Instantiate MarkItDown in deterministic mode by default.
4. Enable optional visual mode only when requested and explicitly wired with an `llm_client`.
5. Convert with `convert_stream`.
6. Return a Pydantic result model and emit debug log events.

## Output checklist
- [ ] Binary-stream conversion implemented.
- [ ] Pydantic input/output models present.
- [ ] Debug file logging enabled.
- [ ] No-LLM default behavior documented and tested.
- [ ] Optional visual mode documented and stub-tested.
- [ ] Markdown structure contract test included.
