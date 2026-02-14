"""MarkItDown wrapper using deterministic defaults and structured outputs.

Complies with:
- core/GLOBAL_RULES.md
- core/LOGGING_STANDARD.md
- core/TESTING_STANDARD.md
- core/STRUCTURED_OUTPUT_STANDARD.md
"""

from __future__ import annotations

import io

from markitdown import MarkItDown

from .logging_adapter import get_debug_file_logger
from .structured_models import ConversionRequest, ConversionResult


def convert_document(
    req: ConversionRequest,
    *,
    llm_client=None,
    log_file: str = "logs/document_intelligence/markitdown_debug.log",
) -> ConversionResult:
    """Convert document bytes to markdown via binary stream conversion only."""
    logger = get_debug_file_logger("document_intelligence.markitdown", log_file)
    logger.debug(
        "conversion_started extension=%s enable_visual_mode=%s llm_model=%s",
        req.extension,
        req.enable_visual_mode,
        req.llm_model,
    )

    stream = io.BytesIO(req.content_bytes)
    md = MarkItDown(llm_client=llm_client) if req.enable_visual_mode else MarkItDown()
    result = md.convert_stream(stream, file_extension=req.extension)

    metadata = {
        "extension": req.extension,
        "visual_mode": req.enable_visual_mode,
        "llm_model": req.llm_model,
    }

    logger.debug(
        "conversion_finished extension=%s markdown_length=%s",
        req.extension,
        len(result.text_content),
    )

    return ConversionResult(markdown=result.text_content, metadata=metadata)
