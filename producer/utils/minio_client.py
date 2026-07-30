from Minio_client.minio_connection import MiniConnection


client = MiniConnection(endpoint="minio:9000",
                            secret_key="minioadmin",
                            access_key="minioadmin").get_client()