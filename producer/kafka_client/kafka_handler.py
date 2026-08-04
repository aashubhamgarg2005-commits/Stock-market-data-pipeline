from producer.kafka_client.kafka_producer import KafkaClient
from producer.config.constants import (
    KAFKA_BROKER_URL,
    STOCK_QUOTES_TOPIC
)
import json
kafka_client = KafkaClient(bootstrap_servers=KAFKA_BROKER_URL)
def kafka_handler(data):
        kafka_client.send_message(topic=STOCK_QUOTES_TOPIC,
                                  message=json.dumps(data))