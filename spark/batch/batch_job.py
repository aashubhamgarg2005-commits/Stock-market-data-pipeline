
from spark.schemas import earnings_schema
from spark.schemas import financial_schema
from sparkSession import spark_session
import time
from Minio_client.minio_reader import MinioReader
from schemas.news_schema import News_schema
from schemas.candle_schema import candles_schema
from schemas.marketStatus_schema import Market_schema
from schemas.company_profile_schema import company_profile_schema
from schemas.earnings_schema import earnings_schema
from schemas.financial_schema import FinancialSchema
from transformation.news_transformation import transformation
from transformation.company_profile_transformation import cleaning_company
from transformation.market_status_transformation import clean_market
from transformation.candles_data_transformation import parse_candles_data
from transformation.earnings_data_transformation import clean_earnings_data
from transformation.finencial_data_transformation import transform_finencial_data
from Minio_client.minio_writer import MinioWritter
from producer.utils.minio_client import client
from producer.utils.logger import LOGGER

def main():
    spark = spark_session()
    obj_read = MinioReader(spark=spark)
    obj_writter = MinioWritter(client=client)
    
    try:
        LOGGER.info("News Data read ")
        news_df = obj_read.read_json(path="s3a://bronze/news/",schema=News_schema)
        LOGGER.info(f"total data {news_df.count()}")
    except Exception as e:
        LOGGER.error(f"read failed {e}")

    try:
        LOGGER.info("News Data Transformation")
        clean_news_df = transformation(df=news_df)
        obj_writter.create_bucket(bucket_name="silver")
        clean_news_df.write \
        .mode("overwrite") \
        .parquet("s3a://silver/news/")
    except Exception as e:
        LOGGER.error(f"Transformation Failed: {e}")

    try:
        LOGGER.info("Candles Data Read")
        candle_df = obj_read\
            .read_json(path="s3a://bronze/candles/",schema=candles_schema)
    except Exception as e:
        LOGGER.error(f"Read Faild {e}")
    try:
        LOGGER.info("Candles Data Transformation")
        clean_candle_df = parse_candles_data(candle_df=candle_df)
        obj_writter.create_bucket(bucket_name="silver")
        clean_candle_df.write \
            .mode("overwrite") \
            .parquet("s3a://silver/candles/")
    except Exception as e:
        LOGGER.error(f"Transformation Failed {e}")
    
    try:
        LOGGER.info("Company Profile Data Read")
        company_df = obj_read.read_json(path="s3a://bronze/company_profile/",schema=company_profile_schema)
        company_df.show(truncate=False, vertical=True)
    except Exception as e:
        LOGGER.error(f"Failed to Read Data {e}")

    try:
        LOGGER.info("Company Data Tranform")
        clean_company_df = cleaning_company(df=company_df)
        obj_writter.create_bucket(bucket_name="silver")
        clean_company_df.write \
        .mode("overwrite") \
        .parquet("s3a://silver/company_profile/")
    except Exception as e:
        LOGGER.error(f"Cleaning Failed {e}")

    try:
        LOGGER.info("Market Data Read")
        market_df = obj_read.read_json(path="s3a://bronze/market_status",schema=Market_schema)
        market_df.show()
    except Exception as e:
        LOGGER.info(f"Failed to Read Market Data {e}")

    try:
        LOGGER.info("Transform Market data")
        clean_market_df = clean_market(df=market_df)
        obj_writter.create_bucket(bucket_name="silver")
        clean_market_df.write \
                .mode("overwrite") \
                .parquet("s3a://silver/market_status/")
    except Exception as e:
                LOGGER.error(f"Cleaning Failed {e}")

    try:
        LOGGER.info("Earning Data Read")
        earning_df = obj_read.read_json(path="s3a://bronze/earnings/",schema=earnings_schema)
        earning_df.show()
        earning_df.printSchema()
    except Exception as e:
        LOGGER.error(f"Failed to read Data {e}")
    try:
        LOGGER.info("Transform Earning Data")
        clean_earning_df = clean_earnings_data(earning_df=earning_df)
        obj_writter.create_bucket(bucket_name="silver")
        clean_earning_df.write \
            .mode("overwrite") \
            .parquet("s3a://silver/earnings/")
    except Exception as e:
        LOGGER.error(f"Cleaning Failed {e}")

    try:
        LOGGER.info("Candles Data Read")
        finencial_df = obj_read\
                .read_json(path="s3a://bronze/finencial/",schema=FinancialSchema)
        finencial_df.show()
        finencial_df.printSchema()
    except Exception as e:
        LOGGER.error(f"Read Failed {e}")

    try:
        LOGGER.info(" Financial Data Transformation")
        clean_bs, clean_cf, clean_ic = transform_finencial_data(df=finencial_df)
        clean_bs.write \
            .mode("overwrite") \
            .parquet("s3a://silver/finencial/bs/")
        clean_cf.write \
            .mode("overwrite") \
            .parquet("s3a://silver/finencial/cf/")
        clean_ic.write \
            .mode("overwrite") \
            .parquet("s3a://silver/finencial/ic/")
    except Exception as e:
        LOGGER.error(f"Transformation Failed {e}")



if __name__ == "__main__":
    main()