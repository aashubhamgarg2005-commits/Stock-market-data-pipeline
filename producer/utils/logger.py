import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR,exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR,"stock_pipeline.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

LOGGER = logging.getLogger("stock_pipeline")