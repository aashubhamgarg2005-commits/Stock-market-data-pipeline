from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers = "kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def send_message(topic,data):
    producer.send(topic,value=data)
    producer.flush()