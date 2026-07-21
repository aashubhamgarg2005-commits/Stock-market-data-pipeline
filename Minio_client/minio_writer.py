import json
from io import BytesIO
import pandas as pd

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
        elif file_format == "parquet":
            df = pd.DataFrame(data=data)
            buffer = BytesIO()
            df.to_parquet(buffer,index=False)
            buffer.seek(0)
            self.client.put_object(
                bucket_name = bucket_name,
                object_name = f"{object_name}.parquet",
                data = buffer,
                legth = buffer.getbuffer().nbytes,
                content_type = "application/octet-stream"

            )
        else :
            raise ValueError(
                "Supported formats are: json, parquet"
            )
            