import io
from types import SimpleNamespace

from topics.document_intelligence.shared.structured_models import ConversionRequest
from topics.document_intelligence.shared import markitdown_wrapper


class FakeMarkItDown:
    def __init__(self, llm_client=None):
        self.llm_client = llm_client

    def convert_stream(self, stream, file_extension):
        assert isinstance(stream, io.BytesIO)
        assert file_extension == ".pdf"
        assert stream.read() == b"binary-pdf"
        return SimpleNamespace(text_content="# Parsed")


def test_binary_stream_conversion(monkeypatch, tmp_path):
    monkeypatch.setattr(markitdown_wrapper, "MarkItDown", FakeMarkItDown)

    req = ConversionRequest(extension=".pdf", content_bytes=b"binary-pdf")
    result = markitdown_wrapper.convert_document(
        req, log_file=str(tmp_path / "debug.log")
    )

    assert result.markdown == "# Parsed"
