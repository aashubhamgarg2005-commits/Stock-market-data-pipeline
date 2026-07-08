from api.base_client import BaseClient
from config.settings import (STOCK_API_KEY,
                             STOCK_API_URL)

class FinhubClient(BaseClient):
    def __init__(self):
        super().__init__(STOCK_API_URL,
                         STOCK_API_KEY)

    def get_stock_quote(self,symbol):
        return self.get_request(
            endpoint="quote",
            params={
                "symbol":symbol
            }
        )