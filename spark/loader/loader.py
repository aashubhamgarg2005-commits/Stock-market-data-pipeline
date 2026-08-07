from sparkSession import spark_session
from silver_reader import SilverReader
from producer.utils.logger import LOGGER
from gold_layer.dim_symbol import dim_symbol
from gold_layer.dim_company import dim_company
from gold_layer.fact_candles import fact_candles
from gold_layer.fact_earning import fact_earning
from gold_layer.fact_market import fact_market
from gold_layer.dim_news import dim_news
from Minio_client.minio_writer import MinioWritter
from producer.utils.minio_client import client
import traceback

def main():
    spark = spark_session()
    silver_read = SilverReader(spark=spark)
    create_bucket = MinioWritter(client=client)
    create_bucket.create_bucket(bucket_name="gold")
    try:
        LOGGER.info("Analysis candles data")
        candles_df = silver_read.candles_reader(path="s3a://silver/candles")
        #candles_df.show()
    except Exception as e:
        traceback.print_exc()
    try:
        LOGGER.info("Analysis earning data")
        earning_df = silver_read.earning_reader(path="s3a://silver/earnings")
        #earning_df.show()
    except Exception as e:
        traceback.print_exc()
    try:
        LOGGER.info("Analysis company data")
        company_df = silver_read.company_profile_reader(path="s3a://silver/company_profile")
        #company_df.show()
    except Exception as e:
        traceback.print_exc()
    try:
        LOGGER.info("Analysis financial balance sheet data")
        finencial_bs_df = silver_read.finencial_bs_reader(path="s3a://silver/financial/bs")
        #finencial_bs_df.show()
    except Exception as e:
        traceback.print_exc()
    try:
        LOGGER.info("Analysis financial cash flow data ")
        finencial_cf_df = silver_read.finencial_cf_reader(path="s3a://silver/financial/cf")
        #finencial_cf_df.show()
    except Exception as e:
        traceback.print_exc()
    try:
        LOGGER.info("Analysis financial income statement data")
        finencial_ic_df = silver_read.finencial_ic_reader(path="s3a://silver/financial/ic")
        #finencial_ic_df.show()
    except Exception as e:
        traceback.print_exc()
    try:
        LOGGER.info("Analysis market status data")
        market_df = silver_read.market_status_reader(path="s3a://silver/market_status")
        #market_df.show()
    except Exception as e:
        traceback.print_exc()
    try:
        LOGGER.info("Analysis news data")
        news_df = silver_read.news_reader(path="s3a://silver/news")
        #news_df.show()
    except Exception as e:
        traceback.print_exc()
    try:
        LOGGER.info("create symbols dim ")
        symbol_df = dim_symbol(candles_df=candles_df,
                               company_profile=company_df,
                               earnings_df=earning_df,
                               financial_bs=finencial_bs_df,
                               financial_cf=finencial_cf_df,
                               financial_ic=finencial_ic_df,
                               news_df=news_df)
        symbol_df.show()
        symbol_df.write\
        .mode("overwrite")\
        .parquet("s3a://gold/dim_symbol")
    except Exception as e:
        traceback.print_exc()

    try:
        LOGGER.info("create company dim")
        dim_company_df = dim_company(company_df=company_df,symbol_df=symbol_df)
        dim_company_df.show()
        dim_company_df.write\
        .mode("overwrite")\
        .parquet("s3a://gold/dim_company")
    except Exception as e:
        traceback.print_exc()

    try:
        LOGGER.info("create fact candles")
        fact_candles_df = fact_candles(candles_df=candles_df,symbol_df=symbol_df)
        fact_candles_df.show()
        fact_candles_df.write\
        .mode("overwrite")\
        .parquet("s3a://gold/fact_candles")
    except Exception as e:
        traceback.print_exc()
    try:
        LOGGER.info("create fact earning")
        fact_earning_df = fact_earning(earning_df=earning_df,symbol_df=symbol_df)
        fact_earning_df.show()
        fact_earning_df.write\
        .mode("overwrite")\
        .parquet("s3a://gold/fact_earning")
    except Exception as e:
        traceback.print_exc()

    try:
        LOGGER.info("create fact market")
        fact_market_df = fact_market(market_df=market_df)
        fact_market_df.show()
        fact_market_df.write\
        .mode("overwrite")\
        .parquet("s3a://gold/fact_market")
    except Exception as e:
        traceback.print_exc()

    try:
        LOGGER.info("create dim news")
        dim_news_df = dim_news(news_df=news_df,symbol_df=symbol_df)
        dim_news_df.show()
        dim_news_df.write\
        .mode("overwrite")\
        .parquet("s3a://gold/dim_news")
    except Exception as e:
        traceback.print_exc()

    
    

if __name__ == "__main__":
    main()