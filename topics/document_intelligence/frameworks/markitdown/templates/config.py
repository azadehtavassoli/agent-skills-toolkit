"""Template config for MarkItDown conversion.

Complies with core standards under `core/`.
"""

from pydantic import BaseModel


class MarkItDownConfig(BaseModel):
    debug_log_file: str = "logs/document_intelligence/markitdown_debug.log"
    enable_visual_mode: bool = False
    llm_model: str | None = None
