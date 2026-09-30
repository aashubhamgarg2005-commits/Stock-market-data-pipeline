from Minio_client.minio_connection import MiniConnection
from producer.config.constants import MINIO_ENDPOINT


client = MiniConnection(endpoint=MINIO_ENDPOINT,
                            secret_key="minioadmin",
                            access_key="minioadmin").get_client()