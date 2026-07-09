from kafka import KafkaProducer
from utils.logger import LOGGER
from config.constants import KAFKA_BROKER_URL
import json
import time

producer = None

try:
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
except Exception as e:
    LOGGER.error(f"Kafka connection failed: {e}")
    time.sleep(5)


def send_message(topic, data):
    if producer is None:
        LOGGER.error("Kafka producer unavailable, message not sent")
        return

    try:
        producer.send(topic, value=data)
        producer.flush()
    except Exception as e:
        LOGGER.error(f"Failed to send Kafka message to {topic}: {e}")
