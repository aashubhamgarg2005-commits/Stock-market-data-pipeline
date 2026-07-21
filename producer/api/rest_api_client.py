from .base_client import BaseClient
from config.settings import STOCK_API_URL,STOCK_API_KEY
from config.settings import (STOCK_CANDLES,
                             STOCK_COMPANY_PROFILE,
                             STOCK_EARNINGS,
                             STOCK_FINENCIAL,
                             STOCK_MARKET_STETUS,
                             STOCK_NEWS,
                                            )
from utils.logger import LOGGER

class RestClient(BaseClient):
    def __init__(self):
        self.candles = STOCK_CANDLES
        self.company_profile = STOCK_COMPANY_PROFILE
        self.earnings = STOCK_EARNINGS
        self.finencial = STOCK_FINENCIAL
        self.market_status = STOCK_MARKET_STETUS
        self.news = STOCK_NEWS
        super().__init__(base_url= STOCK_API_URL,
                         api_key=STOCK_API_KEY,
                         )

    def get_candles(self,symbol,from_timestap,to_timestamp):
        return self.get_request(self.candles,
                                 {"symbol":symbol,
                                  "resolution":"D",
                                  "from":from_timestap,
                                  "to":to_timestamp})

    def get_company_profile(self,symbol):
            return self.get_request(self.company_profile, {"symbol":symbol})

    def get_earning(self,symbol):
            return self.get_request(self.earnings, {"symbol":symbol})

    def get_finencial(self,symbol):
            return self.get_request(self.finencial,
                                     {"symbol":symbol,
                                      "statement":"ic",
                                      "freq":"annual"})

    def get_market_status(self,symbol):
            return self.get_request(self.market_status, {"symbol":symbol})

    def get_news(self,symbol,from_date,to_date):
            return self.get_request(self.news,
                                     {"symbol":symbol,
                                      "from":from_date,
                                      "to":to_date})

