from data_produce import (run_company_profile,
                          run_earning,
                          run_finencials,
                          run_market_status,
                          run_quote_producer,
                          run_stock_candles,
                          run_stock_news)
from utils.logger import LOGGER
from config.settings import STOCK_SYMBOLS
# fetch quote data
try:
    LOGGER.info("Produce Quote data")
    run_quote_producer(STOCK_SYMBOLS=STOCK_SYMBOLS)
except Exception as e:
    LOGGER.error(f"Quote Produce Failed: {e}")

# fetch company profile data
try:
    LOGGER.info("Produce Company Profile data")
    run_company_profile(STOCK_SYMBOLS=STOCK_SYMBOLS)
except Exception as e:
    LOGGER.error(f"Comany Data Failed: {e}")

# fetch Earning data
try:
    LOGGER.info("Produce Earning data")
    run_earning(STOCK_SYMBOLS=STOCK_SYMBOLS)
except Exception as e:
    LOGGER.error(f"Earning data Failed: {e}")

# fetch finencial data
try:
    LOGGER.info("Produce finencial data")
    run_finencials(STOCK_SYMBOLS=STOCK_SYMBOLS)
except Exception as e:
    LOGGER.error(f"Fainencial Data Failed: {e}")

# fetch Market Data
try:
    LOGGER.info("Produce Market Stetus Data")
    run_market_status(STOCK_SYMBOLS=STOCK_SYMBOLS)
except Exception as e:
    LOGGER.error(f"Market Status Data Failed: {e}")

# fetch candles data
try:
    LOGGER.info("Produce Stock candles data")
    run_stock_candles(STOCK_SYMBOLS=STOCK_SYMBOLS)
except Exception as e:
    LOGGER.error(f"Stock Candles Data Failed: {e}")

# fetch srock news data
try:
    LOGGER.info("Produce Stock News Data")
    run_stock_news(STOCK_SYMBOLS=STOCK_SYMBOLS)
except Exception as e:
    LOGGER.error(f"Stock News Data Failed: {e}")