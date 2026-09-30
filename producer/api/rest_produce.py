from .rest_api_client import RestClient
from .alphavintage_client import AlphavantageClient
from datetime import datetime
import time
from producer.utils.logger import LOGGER
from producer.utils.time_manager import StateManager
from producer.config.settings import STOCK_SYMBOLS




def run_stocks():
    state = StateManager()
    client = RestClient()
    alphaclient = AlphavantageClient()

    from_timestamp = state.get_state()["last_run_timestamp"]
    from_date = state.get_state()["last_run_date"]

    to_timestamp = int(time.time())
    to_date = datetime.utcnow().strftime("%Y-%m-%d")
    result = {
    "candles": [],
    "company_profile": [],
    "earnings": [],
    "financial": [],
    "market_status": [],
    "news": []
}
    for symbol in STOCK_SYMBOLS:
        try:
            candles = {}
            LOGGER.info("Start fetch Candles")
            candles = alphaclient.get_candles_data(symbol=symbol)
            result["candles"].append(candles)

        except Exception as e:
            LOGGER.error(f"Fetch Failed: {e}")

        try:
            company_profile = {}
            LOGGER.info("Start fetch Company profile")
            company_profile = client.get_company_profile(symbol=symbol) 
            result["company_profile"].append(company_profile)                                                      
        except Exception as e:
            LOGGER.error(f"Failed to Fatch: {e}")

        try:
            earnings = {}
            LOGGER.info("Start fetch earning")
            earnings = client.get_earning(symbol=symbol)
            if isinstance(earnings,list):
                 result["earnings"].extend(earnings)
            elif earnings:
                 result["earnings"].append(earnings)
        except Exception as e:
                LOGGER.error(f"Failed to fetch : {e}")

        try:
            financial = {}
            LOGGER.info("start fetch finencial")
            financial = client.get_finencial(symbol=symbol)
            result["financial"].append(financial)
        except Exception as e:
                LOGGER.info(f"Failed to fetch: {e}")

        try:
            market_status = {}
            LOGGER.info("start fetch market status")
            market_status = client.get_market_status(exchange = "US")
            result["market_status"].append(market_status)
        except Exception as e:
            LOGGER.info(f"Failed to fetch: {e}")

        try:
            news = {}
            LOGGER.info("start fetch news")
            news = client.get_news(symbol=symbol,
                                    from_date=from_date,
                                    to_date=to_date)
            if isinstance(news, list):
                result["news"].extend(news)
            elif news:
                result["news"].append(news)
        except Exception as e:
            LOGGER.info(f"Failed to fetch: {e}")

        
            
    return result