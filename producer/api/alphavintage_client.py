from .base_client import BaseClient
from producer.config.settings import ALPHAVANTAGE_API_KEY,ALPHAVANTAGE_API_URL
from producer.config.settings import STOCK_CANDLES


class AlphavantageClient(BaseClient):
    def __init__(self):
        self.api_key = ALPHAVANTAGE_API_KEY
        self.candles = STOCK_CANDLES
        super().__init__(base_url=ALPHAVANTAGE_API_URL,
                         api_key=ALPHAVANTAGE_API_KEY )

    def get_candles_data(self,symbol):
        return self.get_request(self.candles,{"function":"TIME_SERIES_DAILY",
                                "symbol":symbol,
                                "outputsize":"compact"
                                },auth_params="apikey")
