from .rest_api_client import RestClient
from datetime import datetime
import time
from utils.logger import LOGGER
from utils.time_manager import StateManager
from config.settings import STOCK_SYMBOLS




def run_stocks():
    state = StateManager()
    client = RestClient()

    from_timestamp = state.get_state()["last_run_timestamp"]
    from_date = state.get_state()["last_run_date"]

    to_timestamp = int(time.time())
    to_date = datetime.utcnow().strftime("%Y-%m-%d")
    for symbol in STOCK_SYMBOLS:
        try:
            candles = {}
            LOGGER.info("Start fetch Candles")
            candles = client.get_candles(symbol=symbol,
                                            from_timestap=from_timestamp,
                                            to_timestamp=to_timestamp)

        except Exception as e:
            LOGGER.error(f"Fetch Failed: {e}")

        try:
            company_profile = {}
            LOGGER.info("Start fetch Company profile")
            company_profile = client.get_company_profile(symbol=symbol)                                                       
        except Exception as e:
            LOGGER.error(f"Failed to Fatch: {e}")

        try:
            earnings = {}
            LOGGER.info("Start fetch earning")
            earnings = client.get_earning(symbol=symbol)
        except Exception as e:
                LOGGER.error(f"Failed to fetch : {e}")

        try:
            finencial = {}
            LOGGER.info("start fetch finencial")
            finencial = client.get_finencial(symbol=symbol)
        except Exception as e:
                LOGGER.info(f"Failed to fetch: {e}")

        try:
            market_status = {}
            LOGGER.info("start fetch market status")
            market_status = client.get_market_status(symbol=symbol)
        except Exception as e:
            LOGGER.info(f"Failed to fetch: {e}")

        try:
            news = {}
            LOGGER.info("start fetch news")
            news = client.get_news(symbol=symbol,
                                    from_date=from_date,
                                    to_date=to_date)
        except Exception as e:
            LOGGER.info(f"Failed to fetch: {e}")
    return {
         "candles":candles,
         "company_profile":company_profile,
         "earnings":earnings,
         "finencial":finencial,
         "market_status":market_status,
         "news":news
         }