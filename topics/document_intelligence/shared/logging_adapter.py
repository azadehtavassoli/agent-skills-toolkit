"""File-based debug logging adapter.

Complies with:
- core/GLOBAL_RULES.md
- core/LOGGING_STANDARD.md
"""

from __future__ import annotations

import logging
from pathlib import Path


def get_debug_file_logger(name: str, log_file: str) -> logging.Logger:
    """Create or reuse a logger that writes debug logs to a file."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    target = Path(log_file)
    target.parent.mkdir(parents=True, exist_ok=True)

    resolved = str(target.resolve())
    exists = any(
        isinstance(handler, logging.FileHandler)
        and getattr(handler, "baseFilename", None) == resolved
        for handler in logger.handlers
    )

    if not exists:
        file_handler = logging.FileHandler(target, encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        )
        logger.addHandler(file_handler)

    return logger
