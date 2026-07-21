from minio import Minio
from producer.utils.logger import LOGGER

class MiniConnection:
    def __init__(self,endpoint,access_key,secret_key,secure=False):
        self.client = Minio(
            endpoint = endpoint,
            access_key = access_key,
            secret_key = secret_key,
            secure = secure
        )

    def get_client(self):
        return self.client