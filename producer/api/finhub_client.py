from datetime import datetime, timedelta

from api.base_client import BaseClient
from config.settings import (STOCK_API_KEY,
                             STOCK_API_URL)
from config.settings import (STOCK_QUOTES,
                             STOCK_CANDLES,
                             STOCK_COMPANY_PROFILE,
                             STOCK_EARNINGS,
                             STOCK_FINENCIAL,
                             STOCK_MARKET_STETUS,
                             STOCK_NEWS)

class FinhubClient(BaseClient):
    def __init__(self):
        self.quotes = STOCK_QUOTES
        self.candles = STOCK_CANDLES
        self.company_profile = STOCK_COMPANY_PROFILE
        self.earning = STOCK_EARNINGS
        self.finencial = STOCK_FINENCIAL
        self.market_stetus = STOCK_MARKET_STETUS
        self.news = STOCK_NEWS
        super().__init__(STOCK_API_URL,
                         STOCK_API_KEY)

    def _default_unix_range(self, days=30):
        end = datetime.utcnow()
        start = end - timedelta(days=days)
        return int(start.timestamp()), int(end.timestamp())

    def _default_iso_range(self, days=7):
        end = datetime.utcnow().date()
        start = end - timedelta(days=days)
        return start.isoformat(), end.isoformat()

    def _to_unix_timestamp(self, value):
        if isinstance(value, datetime):
            return int(value.timestamp())
        if isinstance(value, str):
            try:
                parsed = datetime.fromisoformat(value)
            except ValueError:
                parsed = datetime.strptime(value, "%Y-%m-%d")
            return int(parsed.timestamp())
        return int(value)

    def get_stock_quote(self, symbol):
        return self.get_request(
            endpoint=self.quotes,
            params={
                "symbol": symbol
            }
        )

    def get_stock_candles(self, symbol, resolution="D", from_timestamp=None, to_timestamp=None):
        if from_timestamp is None or to_timestamp is None:
            from_timestamp, to_timestamp = self._default_unix_range(days=30)
        else:
            from_timestamp = self._to_unix_timestamp(from_timestamp)
            to_timestamp = self._to_unix_timestamp(to_timestamp)

        return self.get_request(
            endpoint=self.candles,
            params={
                "symbol": symbol,
                "resolution": resolution,
                "from": from_timestamp,
                "to": to_timestamp
            }
        )

    def get_stock_company_profile(self, symbol):
        return self.get_request(
            endpoint=self.company_profile,
            params={
                "symbol": symbol
            }
        )

    def get_stock_earning(self, symbol):
        return self.get_request(
            endpoint=self.earning,
            params={
                "symbol": symbol
            }
        )

    def get_stock_finencial(self, symbol):
        return self.get_request(
            endpoint=self.finencial,
            params={
                "symbol": symbol
            }
        )

    def get_stock_market_stetus(self, symbol=None):
        return self.get_request(
            endpoint=self.market_stetus
        )

    def get_stock_news(self, symbol, from_date=None, to_date=None):
        if from_date is None or to_date is None:
            from_date, to_date = self._default_iso_range(days=7)

        return self.get_request(
            endpoint=self.news,
            params={
                "symbol": symbol,
                "from": from_date,
                "to": to_date
            }
        )