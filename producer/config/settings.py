import os
from dotenv import load_dotenv

load_dotenv()

# STOCK MARKET API INFORMATION

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
STOCK_API_URL = os.getenv("STOCK_API_URL")
STOCK_SYMBOLS = os.getenv("STOCK_SYMBOLS").split(",")
