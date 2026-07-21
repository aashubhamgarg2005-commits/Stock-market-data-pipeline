from sparkSession import spark_session
from Minio_client.minio_reader import MinioReader
from producer.utils.logger import LOGGER

def main():
    spark = spark_session()
    obj_read = MinioReader(spark=spark)
    try:
        LOGGER.info("Data read ")
        df = obj_read.read_json(path="s3a://bronze/stock-news/")
    except Exception as e:
        LOGGER.error(f"read failed {e}")


if __name__ == "__main__":
    main()