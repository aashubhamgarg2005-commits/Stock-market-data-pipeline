from api.finhub_client import FinhubClient
from config.settings import STOCK_SYMBOLS
from kafka_client.producer import send_message

client = FinhubClient()
stock_data = {}
for symbol in STOCK_SYMBOLS:
    data = client.get_stock_quote(symbol=symbol)
    if data:
        send_message(topic="stock-data",data=data)
        print(f"Sent {symbol} to Kafka")