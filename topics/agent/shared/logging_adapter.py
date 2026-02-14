"""Topic logging adapter enforcing core logging standards."""

from __future__ import annotations

import json
import logging
from datetime import datetime, UTC
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Any


DEFAULT_MAX_BYTES = 10 * 1024 * 1024
DEFAULT_BACKUP_COUNT = 5


def build_topic_logger(
    topic: str,
    component: str,
    log_dir: str = "logs",
    max_bytes: int = DEFAULT_MAX_BYTES,
    backup_count: int = DEFAULT_BACKUP_COUNT,
) -> logging.Logger:
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    date_part = datetime.now(UTC).strftime("%Y%m%d")
    log_file = Path(log_dir) / f"{topic}_{component}_{date_part}.log"

    logger = logging.getLogger(f"{topic}.{component}")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(handler)
    return logger


def log_event(logger: logging.Logger, **payload: Any) -> None:
    payload.setdefault("timestamp", datetime.now(UTC).isoformat())
    logger.debug(json.dumps(payload, ensure_ascii=False))
