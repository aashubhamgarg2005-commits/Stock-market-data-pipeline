import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "stock_pipeline.log")

# Logger
LOGGER = logging.getLogger("stock_pipeline")
LOGGER.setLevel(logging.INFO)

# Prevent duplicate logs
LOGGER.handlers.clear()

# Log format
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s"
)

# File Handler (5 MB per file, keep last 5 backups)
file_handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=5 * 1024 * 1024,
    backupCount=5,
    encoding="utf-8"
)
file_handler.setFormatter(formatter)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

LOGGER.addHandler(file_handler)
LOGGER.addHandler(console_handler)

LOGGER.propagate = False