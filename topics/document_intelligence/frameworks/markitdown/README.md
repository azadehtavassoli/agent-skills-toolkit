# MarkItDown Framework Topic

This framework provides templates for converting binary documents into markdown using `MarkItDown.convert_stream` and `io.BytesIO` only.

## Governance alignment
- `core/GLOBAL_RULES.md`
- `core/LOGGING_STANDARD.md`
- `core/TESTING_STANDARD.md`
- `core/STRUCTURED_OUTPUT_STANDARD.md`

## Included templates
- `templates/config.py`: Pydantic configuration model.
- `templates/converter.py`: high-level conversion entrypoint.
- `templates/cli.py`: CLI scaffold for byte-stream conversion.

## Included tests
- `test_binary_stream_conversion.py`
- `test_no_llm_default.py`
- `test_visual_mode_stubbed.py`
- `test_markdown_structure_contract.py`
