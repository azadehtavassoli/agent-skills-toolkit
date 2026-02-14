# Integration Instructions: MarkItDown

All implementation templates in this topic MUST comply with:
- `core/GLOBAL_RULES.md`
- `core/LOGGING_STANDARD.md`
- `core/TESTING_STANDARD.md`
- `core/STRUCTURED_OUTPUT_STANDARD.md`

## Copilot/ChatGPT integration guidance
1. Implement a dedicated wrapper function that accepts typed Pydantic request models.
2. Convert incoming document bytes via `io.BytesIO` and call `MarkItDown.convert_stream(...)`.
3. Return structured Pydantic response objects with markdown and metadata.
4. Emit debug logs to file for mode and conversion lifecycle.

## Safe defaults
- Default mode is deterministic and does not pass an LLM client.
- LLM/visual mode must be explicitly enabled (`enable_visual_mode=True`).
- Do not silently infer or auto-enable visual mode.

## Optional visual interpretation mode
- Require both `enable_visual_mode=True` and a provided `llm_client`.
- Keep mode-specific metadata in the response.
- In tests, use a fake `llm_client`; never call real models.

## Required testing patterns
- Unit test binary stream conversion path (`BytesIO` + `convert_stream`).
- Unit test default mode excludes LLM usage.
- Unit test optional visual mode is explicit and stubbed.
- Contract test output markdown shape and metadata keys.
