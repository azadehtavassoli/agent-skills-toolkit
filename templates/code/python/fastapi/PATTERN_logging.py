import logging
from fastapi import Depends

def get_logger():
    """
    Logger factory that can be injected.
    """
    logger = logging.getLogger("fastapi_app")
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        )
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
    return logger
