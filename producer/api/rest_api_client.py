from .base_client import BaseClient
from producer.config.settings import STOCK_API_URL,STOCK_API_KEY
from producer.config.settings import (
                             STOCK_COMPANY_PROFILE,
                             STOCK_EARNINGS,
                             STOCK_FINENCIAL,
                             STOCK_MARKET_STETUS,
                             STOCK_NEWS,
                                            )
from producer.utils.logger import LOGGER

class RestClient(BaseClient):
    def __init__(self):
        self.company_profile = STOCK_COMPANY_PROFILE
        self.earnings = STOCK_EARNINGS
        self.finencial = STOCK_FINENCIAL
        self.market_status = STOCK_MARKET_STETUS
        self.news = STOCK_NEWS
        super().__init__(base_url= STOCK_API_URL,
                         api_key=STOCK_API_KEY,
                         )

    def get_company_profile(self,symbol):
            return self.get_request(self.company_profile, {"symbol":symbol},auth_params="token")

    def get_earning(self,symbol):
            return self.get_request(self.earnings, {"symbol":symbol},auth_params="token")

    def get_finencial(self,symbol):
            return self.get_request(self.finencial,
                                     {"symbol":symbol,
                                      "statement":"ic",
                                      "freq":"annual"},auth_params="token")

    def get_market_status(self,exchange):
            return self.get_request(self.market_status, {"exchange":exchange},auth_params="token")

    def get_news(self,symbol,from_date,to_date):
            return self.get_request(self.news,
                                     {"symbol":symbol,
                                      "from":from_date,
                                      "to":to_date},auth_params="token")

