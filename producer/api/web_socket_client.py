import websocket
import json
import time
from producer.utils.logger import LOGGER

class WebSocketClient:
    def __init__(self, web_url, token,symbols,message_handler=None):
        self.websocket_url = web_url
        self.token = token
        self.symbols = symbols
        self.message_handler = message_handler
        self.url = f"{self.websocket_url}token={self.token}"
        self.ws = None

    def on_message(self, ws, message):
        try:
            LOGGER.info(f"Received message: {message}")
            data = json.loads(message)
            if data.get("type") == "ping":
                LOGGER.debug(f"Finhub ping / Keep-alive heartbeat received.")
                return
            if self.message_handler:
                self.message_handler(data)
        except Exception as e:
            LOGGER.error(f"Failed to process message {e}")
            

    def on_error(self, ws, error):
        LOGGER.error(f"WebSocket error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        LOGGER.info(f"WebSocket closed. Code={close_status_code}, Reason={close_msg}")

    def on_open(self, ws):
        LOGGER.info("WebSocket connection opened")
        for symbol in self.symbols:
            payload = {
                "type": "subscribe",
                 "symbol":symbol
                 }
            LOGGER.info(f"payload : {payload}")
            ws.send(json.dumps(payload))
            LOGGER.info(f"Subscribed to symbol: {symbol}")

    def connect(self):
        while True:
            try:
                self.ws = websocket.WebSocketApp(
                    self.url,
                    on_open=self.on_open,
                    on_message=self.on_message,
                    on_error=self.on_error,
                    on_close=self.on_close,
                )

                self.ws.run_forever()

            except Exception as e:
                LOGGER.error(f"Connection failed: {e}")

            LOGGER.info("Reconnecting in 5 seconds...")
            time.sleep(5)