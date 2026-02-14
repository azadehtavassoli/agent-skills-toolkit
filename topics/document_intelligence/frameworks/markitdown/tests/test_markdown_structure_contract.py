from types import SimpleNamespace

from topics.document_intelligence.shared.structured_models import (
    ConversionRequest,
    ConversionResult,
)
from topics.document_intelligence.shared import markitdown_wrapper


class FakeMarkItDown:
    def __init__(self, llm_client=None):
        self.llm_client = llm_client

    def convert_stream(self, stream, file_extension):
        return SimpleNamespace(text_content="# Title\n\nBody")


def test_markdown_structure_contract(monkeypatch, tmp_path):
    monkeypatch.setattr(markitdown_wrapper, "MarkItDown", FakeMarkItDown)

    req = ConversionRequest(extension=".docx", content_bytes=b"doc")
    result = markitdown_wrapper.convert_document(req, log_file=str(tmp_path / "debug.log"))

    assert isinstance(result, ConversionResult)
    assert isinstance(result.markdown, str)
    assert "extension" in result.metadata
    assert result.markdown.startswith("#")
