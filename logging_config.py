import logging
from logging.handlers import RotatingFileHandler


def setup_logging(log_level, log_file):
    handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=3)
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[handler, logging.StreamHandler()],
    )
    logger = logging.getLogger(__name__)
    return logger
