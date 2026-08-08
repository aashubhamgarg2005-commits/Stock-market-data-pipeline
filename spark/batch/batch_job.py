from producer.utils.minio_client import client
from sparkSession import spark_session
from Minio_client.minio_reader import MinioReader
from Minio_client.minio_writer import MinioWritter
from schemas.news_schema import news_schema
from schemas.company_profile_schema import company_schema
from schemas.market_schema import market_schema
from schemas.earning_schema import earnings_schema
from schemas.candles_schema import candles_schema
from schemas.financial_schema import financial_schema
from transformation.news_transfoemation import transform_news
from transformation.company_profile_transformation import clean_company_profile
from transformation.market_status_transformation import clean_market_status
from transformation.earning_transformation import clean_earnings_df
from transformation.candles_data_transformation import clean_candles_df
from transformation.financial_data_transform import clean_financial_data
from producer.utils.logger import LOGGER
import traceback

def main():
    spark = spark_session()
    obj_read = MinioReader(spark=spark)
    create_bucket = MinioWritter(client=client)
    create_bucket.create_bucket(bucket_name="silver")
    
    try:
        LOGGER.info("News Data Read")
        news_df = obj_read.read_json(path="s3a://bronze/news",schema=news_schema)
        news_df.show(truncate=False)
    except Exception as e:
        LOGGER.error(f"Failed {e}")

    try:
        LOGGER.info("Transform News Data")
        clean_news_df = transform_news(df=news_df)
        clean_news_df.coalesce(1) \
        .write \
        .mode("overwrite") \
        .parquet("s3a://silver/news")

    except Exception as e:
        LOGGER.error(f"transformation failed {e}") 
    
    try:
        LOGGER.info("Read company profile")
        company_df = obj_read.read_json("s3a://bronze/company_profile",schema=company_schema)
    except Exception as e:
        LOGGER.error(f"Failed {e}") 

    try:
        LOGGER.info("Transform Company Data")
        clean_company = clean_company_profile(df=company_df)
        clean_company.show()
        clean_company.coalesce(1)\
        .write\
        .mode("overwrite")\
        .parquet("s3a://silver/company_profile")
    except Exception as e:
        LOGGER.info(f"failed to transform {e}")
    
    try:
        LOGGER.info("Read Market status")
        market_df = obj_read.read_json("s3a://bronze/market_status",schema=market_schema)
        market_df.show()
        market_df.printSchema()

    except Exception as e:
        LOGGER.error(f"Failed {e}")

    try:
        LOGGER.info("Standerize Market Status Data")
        clean_market_df = clean_market_status(df=market_df)
        clean_market_df.show()
        clean_market_df.coalesce(1)\
                .write\
                .mode("overwrite")\
                .parquet("s3a://silver/market_status")
    except Exception as e:
        traceback.print_exc()
    
    try:
        LOGGER.info("Read Earnings data")
        earning_df = obj_read.read_json("s3a://bronze/earnings",schema=earnings_schema)
        earning_df.show()
        earning_df.printSchema()
    except Exception as e:
        LOGGER.error(f"Failed {e}")

    try:
        LOGGER.info("Standrize earning data")
        clean_earning_df = clean_earnings_df(df=earning_df)
        clean_earning_df.show()
        clean_earning_df.coalesce(1)\
        .write\
        .mode("overwrite")\
        .parquet("s3a://silver/earnings")
    except Exception as e:
        traceback.print_exc()
    
    try:
        LOGGER.info("Read candles Data")
        candles_df = obj_read.read_json("s3a://bronze/candles",schema=candles_schema)
        candles_df.show()
        candles_df.printSchema()
    except Exception as e:
        LOGGER.error(f"Failed {e}")

    try:
        LOGGER.info("Standerize candles data")
        clean_candles_data = clean_candles_df(df=candles_df)
        clean_candles_data.show()
        clean_candles_data.coalesce(1)\
        .write\
        .mode("overwrite")\
        .parquet("s3a://silver/candles")
    except Exception as e:
        traceback.print_exc()
    
    try:
        LOGGER.info("Read Financial Data")
        finencial_df = obj_read.read_json("s3a://bronze/financial",schema=financial_schema)
        finencial_df.show()
        finencial_df.printSchema()

    except Exception as e:
        LOGGER.error(f"Failed {e}")

    try:
        LOGGER.info("Standerize financial data")
        clean_bs,clean_cf,clean_ic = clean_financial_data(df=finencial_df)
        clean_bs.show()
        clean_cf.show()
        clean_ic.show()
        LOGGER.info("write clean bs data")
        clean_bs.coalesce(1)\
        .write\
        .mode("overwrite")\
        .parquet("s3a://silver/financial/bs")
        LOGGER.info("write clean cf data")
        clean_cf.coalesce(1)\
                .write\
                .mode("overwrite")\
                .parquet("s3a://silver/financial/cf")
        LOGGER.info("write clean ic data")
        clean_ic.coalesce(1)\
                        .write\
                        .mode("overwrite")\
                        .parquet("s3a://silver/financial/ic")
    except Exception as e:
        traceback.print_exc() 
                

if __name__ == "__main__":
    main() 