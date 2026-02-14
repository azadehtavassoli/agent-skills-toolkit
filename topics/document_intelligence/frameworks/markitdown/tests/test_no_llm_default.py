from types import SimpleNamespace

from topics.document_intelligence.shared.structured_models import ConversionRequest
from topics.document_intelligence.shared import markitdown_wrapper


class FakeMarkItDown:
    seen_llm_client = object()

    def __init__(self, llm_client=None):
        FakeMarkItDown.seen_llm_client = llm_client

    def convert_stream(self, stream, file_extension):
        return SimpleNamespace(text_content="content")


def test_no_llm_default(monkeypatch, tmp_path):
    monkeypatch.setattr(markitdown_wrapper, "MarkItDown", FakeMarkItDown)

    req = ConversionRequest(extension=".txt", content_bytes=b"hello", enable_visual_mode=False)
    _ = markitdown_wrapper.convert_document(req, log_file=str(tmp_path / "debug.log"))

    assert FakeMarkItDown.seen_llm_client is None
