"""CLI template for binary-stream MarkItDown conversion."""

from __future__ import annotations

import argparse
from pathlib import Path

from .converter import convert_bytes_to_markdown


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Convert document bytes to markdown")
    parser.add_argument("input_file", help="Path to input document")
    parser.add_argument("--extension", required=True, help="File extension, e.g. .pdf")
    parser.add_argument("--output", required=True, help="Output markdown path")
    parser.add_argument("--visual-mode", action="store_true", help="Enable optional visual mode")
    parser.add_argument(
        "--debug-log",
        default="logs/document_intelligence/markitdown_debug.log",
        help="Debug log file path",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    content = Path(args.input_file).read_bytes()

    result = convert_bytes_to_markdown(
        extension=args.extension,
        content_bytes=content,
        enable_visual_mode=args.visual_mode,
        llm_client=None,
        log_file=args.debug_log,
    )

    Path(args.output).write_text(result.markdown, encoding="utf-8")


if __name__ == "__main__":
    main()
