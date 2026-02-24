import structlog
import logging
from logging.handlers import RotatingFileHandler

def configure_logger(log_path: str):
    # Standard handler for rotation
    file_handler = RotatingFileHandler(
        log_path, maxBytes=10*1024*1024, backupCount=5
    )
    
    structlog.configure(
        processors=[
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso", utc=True),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            # THE KEY: Human-readable Key-Value Renderer
            structlog.processors.KeyValueRenderer(sort_keys=True),
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
    
    # Root logging config to catch everything
    logging.basicConfig(
        format="%(message)s",
        level=logging.DEBUG,
        handlers=[file_handler, logging.StreamHandler()]
    )

log = structlog.get_logger()