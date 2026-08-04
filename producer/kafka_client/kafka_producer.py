from kafka import KafkaProducer
from producer.utils.logger import LOGGER
import json

class KafkaClient:
    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers
        self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers,
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                      key_serializer=lambda k: json.dumps(k).encode('utf-8'),
                                      retries=5)

    def send_message(self, topic, message):
        try:
            self.producer.send(topic, value=message)
            self.producer.flush()
            LOGGER.info(f"Message sent to topic {topic}: {message}")
        except Exception as e:
            LOGGER.error(f"Failed to send message to topic {topic}: {e}")