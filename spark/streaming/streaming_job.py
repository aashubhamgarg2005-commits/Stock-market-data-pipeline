from spark.stream_consumer.consume_data import consume_stream_data
from Minio_client.minio_writer import MinioWritter
from producer.utils.minio_client import client
from producer.config.constants import RAW_DATA_BUCKET,PROCESSED_DATA_BUCKET


def main():
    stock_quote = consume_stream_data()
    mini_client = MinioWritter(client=client)

    # write raw data into minio 
    mini_client.create_bucket(bucket_name=RAW_DATA_BUCKET)
    query = (
        stock_quote.writeStream
        .format("json")
        .outputMode("append")
        .option("path","s3a://bronze/stock_quotes" )
        .option("checkpointLocation", "s3a://bronze/stock_quotes/checkpoints")
        .start()
    )

    print("Streaming data to MinIO:","stock_quotes")

    query.awaitTermination()


if __name__ == "__main__":
    main()
