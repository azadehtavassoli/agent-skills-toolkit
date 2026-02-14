import logging
import sys
from logging.handlers import TimedRotatingFileHandler
from pythonjsonlogger import jsonlogger

from app.settings import get_settings

def setup_logging():
    """
    Configure structured logging for FastAPI with:
    - Debug level (configurable)
    - File output with rotation
    - JSON structured logs
    """

    settings = get_settings()

    # Root logger
    logger = logging.getLogger()
    logger.setLevel(settings.LOG_LEVEL)  # e.g., "DEBUG"

    # JSON formatter for structured logs
    json_formatter = jsonlogger.JsonFormatter(
        '%(asctime)s %(levelname)s %(name)s %(message)s'
    )

    # File handler (rotates daily, keeps 7 days)
    file_handler = TimedRotatingFileHandler(
        filename=settings.LOG_FILE_PATH,
        when="midnight",
        interval=1,
        backupCount=settings.LOG_BACKUP_COUNT
    )
    file_handler.setFormatter(json_formatter)
    file_handler.setLevel(settings.LOG_LEVEL)

    # Console handler (optional)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(json_formatter)
    console_handler.setLevel(settings.LOG_LEVEL)

    # Attach handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Prevent duplicated logging from Uvicorn
    logging.getLogger("uvicorn.error").handlers = [file_handler]
    logging.getLogger("uvicorn.access").handlers = [file_handler]
