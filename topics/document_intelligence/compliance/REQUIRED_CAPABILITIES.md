# Required Capabilities: Document Intelligence

This topic must satisfy the following capabilities under:
- `core/GLOBAL_RULES.md`
- `core/LOGGING_STANDARD.md`
- `core/TESTING_STANDARD.md`
- `core/STRUCTURED_OUTPUT_STANDARD.md`

## Capability checklist
1. **Binary stream conversion**
   - Uses `io.BytesIO` and `MarkItDown.convert_stream`.
2. **Deterministic default mode**
   - No LLM required in default path.
3. **Optional LLM integration mode**
   - Explicitly enabled for visual interpretation.
4. **Logging compliance**
   - Debug logs written to file.
5. **Structured output compliance**
   - Pydantic `BaseModel` for requests/responses.
6. **Test coverage compliance**
   - Includes tests for deterministic/default mode, optional LLM stub mode, and output structure contracts.
