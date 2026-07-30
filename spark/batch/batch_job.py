from sparkSession import spark_session
from Minio_client.minio_reader import MinioReader
from schemas.news_schema import News_schema
from producer.utils.logger import LOGGER

def main():
    spark = spark_session()
    obj_read = MinioReader(spark=spark)
    try:
        LOGGER.info("Data read ")
        news_df = obj_read.read_json(path="s3a://bronze/news/",schema=News_schema)
        LOGGER.info(f"total data {news_df.count()}")
        news_df.show()
    except Exception as e:
        LOGGER.error(f"read failed {e}")


if __name__ == "__main__":
    main()