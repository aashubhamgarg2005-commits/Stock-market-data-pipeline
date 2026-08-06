import json
from io import BytesIO


class MinioWritter:
    def __init__(self,client):
        self.client = client

    def create_bucket(self,bucket_name):
        if not self.client.bucket_exists(bucket_name):
            self.client.make_bucket(bucket_name)

    def write_file(self,
                   bucket_name,
                   object_name,
                   data,
                   file_format):
        
        if file_format == "json":
            payload = json.dumps(data).encode("utf-8")
            self.client.put_object(
                bucket_name = bucket_name,
                object_name = f"{object_name}.json",
                data = BytesIO(payload),
                length = len(payload),
                content_type = "application/json"

            )
        else :
            raise ValueError(
                "Supported formats are: json, parquet"
            )
            