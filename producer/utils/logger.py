import logging
import os
from logging.handlers import RotatingFileHandler

# ==========================
# Log Directory
# ==========================
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "stock_pipeline.log")

# ==========================
# Logger
# ==========================
LOGGER = logging.getLogger("stock_pipeline")
LOGGER.setLevel(logging.INFO)

# Prevent duplicate handlers
if LOGGER.hasHandlers():
    LOGGER.handlers.clear()

# ==========================
# Formatter
# ==========================
formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# ==========================
# Console Handler
# ==========================
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# ==========================
# File Handler
# ==========================
file_handler = RotatingFileHandler(
    filename=LOG_FILE,
    mode="a",
    maxBytes=5 * 1024 * 1024,  # 5 MB
    backupCount=5,
    encoding="utf-8"
)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# ==========================
# Add Handlers
# ==========================
LOGGER.addHandler(console_handler)
LOGGER.addHandler(file_handler)

# Stop propagating to root logger
LOGGER.propagate = False