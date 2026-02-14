"""Structured models for document conversion.

Complies with:
- core/GLOBAL_RULES.md
- core/STRUCTURED_OUTPUT_STANDARD.md
"""

from pydantic import BaseModel, Field


class ConversionRequest(BaseModel):
    extension: str = Field(..., description="File extension including leading dot, e.g. .pdf")
    content_bytes: bytes = Field(..., description="Binary document payload")
    enable_visual_mode: bool = Field(default=False)
    llm_model: str | None = Field(default=None)


class ConversionResult(BaseModel):
    markdown: str
    metadata: dict
