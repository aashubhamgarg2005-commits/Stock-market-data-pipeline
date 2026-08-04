from producer.api.web_socket_client import WebSocketClient
from producer.kafka_client.topic_manager import TopicManager
from producer.config.settings import (
                                    WEBSOCKET_URL as url,
                                    STOCK_API_KEY as token,
                                    STOCK_SYMBOLS,
                                    )
from producer.config.constants import KAFKA_BROKER_URL,STOCK_QUOTES_TOPIC
from producer.kafka_client.kafka_handler import kafka_handler


def main():
    # Initialize Kafka client and topic manager
    topic_manager = TopicManager(bootstrap_servers=KAFKA_BROKER_URL)

    # Create the Kafka topic if it doesn't exist
    topic_manager.create_topic(topic_name=STOCK_QUOTES_TOPIC)

    # Initialize WebSocket client
    ws_client = WebSocketClient(web_url=url, token=token,symbols=STOCK_SYMBOLS,message_handler=kafka_handler)

    # Define a callback function to handle incoming messages
    
    # Connect to the WebSocket server
    ws_client.connect()

if __name__ == "__main__":
    main()