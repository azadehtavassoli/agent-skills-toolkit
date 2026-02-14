"""Template conversion entrypoint for MarkItDown."""

from topics.document_intelligence.shared.markitdown_wrapper import convert_document
from topics.document_intelligence.shared.structured_models import (
    ConversionRequest,
    ConversionResult,
)


def convert_bytes_to_markdown(
    *,
    extension: str,
    content_bytes: bytes,
    enable_visual_mode: bool = False,
    llm_model: str | None = None,
    llm_client=None,
    log_file: str = "logs/document_intelligence/markitdown_debug.log",
) -> ConversionResult:
    req = ConversionRequest(
        extension=extension,
        content_bytes=content_bytes,
        enable_visual_mode=enable_visual_mode,
        llm_model=llm_model,
    )
    return convert_document(req, llm_client=llm_client, log_file=log_file)
