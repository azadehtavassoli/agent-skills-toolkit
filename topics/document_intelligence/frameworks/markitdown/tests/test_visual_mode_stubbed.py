from types import SimpleNamespace

from topics.document_intelligence.shared.structured_models import ConversionRequest
from topics.document_intelligence.shared import markitdown_wrapper


class FakeMarkItDown:
    seen_llm_client = None

    def __init__(self, llm_client=None):
        FakeMarkItDown.seen_llm_client = llm_client

    def convert_stream(self, stream, file_extension):
        return SimpleNamespace(text_content="visual content")


def test_visual_mode_stubbed(monkeypatch, tmp_path):
    monkeypatch.setattr(markitdown_wrapper, "MarkItDown", FakeMarkItDown)

    fake_client = object()
    req = ConversionRequest(
        extension=".png",
        content_bytes=b"img",
        enable_visual_mode=True,
        llm_model="stubbed-model",
    )
    result = markitdown_wrapper.convert_document(
        req,
        llm_client=fake_client,
        log_file=str(tmp_path / "debug.log"),
    )

    assert FakeMarkItDown.seen_llm_client is fake_client
    assert result.metadata["visual_mode"] is True
    assert result.metadata["llm_model"] == "stubbed-model"
