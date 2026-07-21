from api.rest_produce import run_stocks
import time
from Minio_client.minio_connection import MiniConnection
from Minio_client.minio_writer import MinioWritter
from producer.utils.logger import LOGGER
from producer.utils.time_manager import StateManager

def main():
    client = MiniConnection(endpoint="minio:9000",
                            secret_key="minioadmin",
                            access_key="minioadmin").get_client()
    writer = MinioWritter(client=client)
    state = StateManager()
    data = run_stocks()

    for endpoint,value in data.items():
        writer.create_bucket(bucket_name="bronze")
        writer.write_file(
            bucket_name="bronze",
            object_name=f"{endpoint}/{int(time.time())}",
            file_format="json",
            data=value,
            
        )
    state.update_state()

if __name__ == "__main__":
    main()
    