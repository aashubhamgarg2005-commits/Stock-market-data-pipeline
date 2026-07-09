from api.finhub_client import FinhubClient
from kafka_client.producer import send_message
from config.constants import (STOCK_QUOTES_TOPIC,
                              STOCK_CANDLES_TOPIC,
                              STOCK_COMPANY_PROFILE_TOPIC,
                              STOCK_EARNINGS_TOPIC,
                              STOCK_FINENCIAL_TOPIC,
                              STOCK_MARKET_STETUS_TOPIC,
                              STOCK_NEWS_TOPIC)
from utils.logger import LOGGER

client = FinhubClient()
def run_quote_producer(STOCK_SYMBOLS):
    quote_data = {}
    for symbol in STOCK_SYMBOLS:
        quote_data = client.get_stock_quote(symbol=symbol)
        if quote_data:
            send_message(topic=STOCK_QUOTES_TOPIC,data=quote_data)
            LOGGER.info(f"Sent {symbol} to Kafka")

def run_stock_candles(STOCK_SYMBOLS):
    candles_data = {}
    for symbol in STOCK_SYMBOLS:
        candles_data = client.get_stock_candles(symbol=symbol)
        if candles_data:
            send_message(topic=STOCK_CANDLES_TOPIC,data=candles_data)
            LOGGER.info(f"Sent {symbol} to Kafka")


def run_company_profile(STOCK_SYMBOLS):
    company_profile = {}
    for symbol in STOCK_SYMBOLS:
        company_profile = client.get_stock_company_profile(symbol=symbol)
        print(company_profile)
        if company_profile:
            send_message(topic=STOCK_COMPANY_PROFILE_TOPIC,data=company_profile)
            LOGGER.info(f"Sent {symbol} to Kafka")


def run_earning(STOCK_SYMBOLS):
    earning_data = {}
    for symbol in STOCK_SYMBOLS:
        earning_data = client.get_stock_earning(symbol=symbol)
        if earning_data:
            send_message(topic=STOCK_EARNINGS_TOPIC,data=earning_data)
            LOGGER.info(f"Sent {symbol} to Kafka")


def run_market_status(STOCK_SYMBOLS):
    market_status_data = {}
    for symbol in STOCK_SYMBOLS:
        market_status_data = client.get_stock_market_stetus(symbol=symbol)
        if market_status_data:
            send_message(topic=STOCK_MARKET_STETUS_TOPIC,data=market_status_data)
            LOGGER.info(f"Sent {symbol} to Kafka")

def run_finencials(STOCK_SYMBOLS):
    finencial_data = {}
    for symbol in STOCK_SYMBOLS:
        finencial_data = client.get_stock_finencial(symbol=symbol)
        if finencial_data:
            send_message(topic=STOCK_FINENCIAL_TOPIC,data=finencial_data)
            LOGGER.info(f"Sent {symbol} to Kafka")


def run_stock_news(STOCK_SYMBOLS):
    news_data = {}
    for symbol in STOCK_SYMBOLS:
        news_data = client.get_stock_news(symbol=symbol)
        if news_data:
            send_message(topic=STOCK_NEWS_TOPIC,data=news_data)
            LOGGER.info(f"Sent {symbol} to Kafka")






    