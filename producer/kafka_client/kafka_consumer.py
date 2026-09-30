from kafka import KafkaConsumer
from producer.utils.logger import LOGGER
from producer.config.constants import KAFKA_BROKER_URL,STOCK_QUOTES_TOPIC
from Minio_client.minio_writer import MinioWritter
from producer.utils.minio_client import client
import traceback
import time
import json

class KafkaConsumerClient:
    def __init__(self,):
        self.bootstrap_servers = KAFKA_BROKER_URL
        self.consumer = KafkaConsumer(
            STOCK_QUOTES_TOPIC,
            bootstrap_servers=self.bootstrap_servers,
            group_id="bronze-consumers_group",
            auto_offset_reset="earliest",
            enable_auto_commit=False,
            value_deserializer=lambda x :json.loads(x.decode('utf-8'))
        )

    def consume_message(self):
        obj_writer = MinioWritter(client=client)
        bucket = obj_writer.create_bucket(bucket_name="bronze")
        for messages in self.consumer:
            data = messages.value
            LOGGER.info(data)
            try:
                obj_writer.write_file(bucket_name="bronze",
                                    object_name=f"trade/{int(time.time()*1000)}",
                                    file_format="json",
                                    data=data)
                self.consumer.commit()
                LOGGER.info(f"Data store successfully at {time.time()*1000}")
            except Exception as e:
                traceback.print_exc()



