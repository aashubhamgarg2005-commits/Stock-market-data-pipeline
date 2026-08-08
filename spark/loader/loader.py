from sparkSession import spark_session
from silver_reader import SilverReader
from jdbc_connection import PostgresLoader
from producer.utils.logger import LOGGER
from gold_layer.dim_symbol import dim_symbol
from gold_layer.dim_company import dim_company
from gold_layer.fact_candles import fact_candles
from gold_layer.fact_earning import fact_earning
from gold_layer.fact_market import fact_market
from gold_layer.dim_news import dim_news
from gold_layer.dim_financial_concept import dim_financial
from gold_layer.fact_financial_bs import fact_financial_bs
from gold_layer.fact_financial_cf import fact_financial_cf
from gold_layer.fact_financial_ic import fact_financial_ic
from Minio_client.minio_writer import MinioWritter
from producer.utils.minio_client import client
from producer.config.constants import (JDBC_URL,
                                       DATABASE_USER,
                                       DATABASE_PASSWORD
                                       )
import traceback


def main():
    # Initialize Spark session and data readers
    spark = spark_session()
    silver_read = SilverReader(spark=spark)

    # Ensure the gold bucket exists in MinIO before writing transformed data
    create_bucket = MinioWritter(client=client)
    create_bucket.create_bucket(bucket_name="gold")

    # Initialize Postgres loader for persisting data to the warehouse
    data_loader = PostgresLoader(jdbc_url=JDBC_URL,
                                 user=DATABASE_USER,
                                 password=DATABASE_PASSWORD)
    
    # Load raw silver data into Spark DataFrames
    try:
        LOGGER.info("Analysis candles data")
        candles_df = silver_read.candles_reader(path="s3a://silver/candles")
        # candles_df.show()  # optional debug display
    except Exception as e:
        traceback.print_exc()

    try:
        LOGGER.info("Analysis earning data")
        earning_df = silver_read.earning_reader(path="s3a://silver/earnings")
        # earning_df.show()  # optional debug display
    except Exception as e:
        traceback.print_exc()

    try:
        LOGGER.info("Analysis company data")
        company_df = silver_read.company_profile_reader(path="s3a://silver/company_profile")
        # company_df.show()  # optional debug display
    except Exception as e:
        traceback.print_exc()

    try:
        LOGGER.info("Analysis financial balance sheet data")
        finencial_bs_df = silver_read.finencial_bs_reader(path="s3a://silver/financial/bs")
    except Exception as e:
        traceback.print_exc()

    try:
        LOGGER.info("Analysis financial cash flow data")
        finencial_cf_df = silver_read.finencial_cf_reader(path="s3a://silver/financial/cf")
    except Exception as e:
        traceback.print_exc()

    try:
        LOGGER.info("Analysis financial income statement data")
        finencial_ic_df = silver_read.finencial_ic_reader(path="s3a://silver/financial/ic")
    except Exception as e:
        traceback.print_exc()

    try:
        LOGGER.info("Analysis market status data")
        market_df = silver_read.market_status_reader(path="s3a://silver/market_status")
    except Exception as e:
        traceback.print_exc() 

    try:
        LOGGER.info("Analysis news data")
        news_df = silver_read.news_reader(path="s3a://silver/news")
    except Exception as e:
        traceback.print_exc()
    
    # Build and persist dimension tables
    try:
        LOGGER.info("create symbols dim")
        symbol_df = dim_symbol(candles_df=candles_df,
                               company_profile=company_df,
                               earnings_df=earning_df,
                               financial_bs=finencial_bs_df,
                               financial_cf=finencial_cf_df,
                               financial_ic=finencial_ic_df,
                               news_df=news_df)

        # Write dimension table to gold storage and load into Postgres
        symbol_df.write\
            .mode("overwrite")\
            .parquet("s3a://gold/dim_symbol")
        data_loader.load(df=symbol_df, table_name="dim_symbol")
    except Exception as e:
        traceback.print_exc()
    
    try:
        LOGGER.info("create company dim")
        dim_company_df = dim_company(company_df=company_df, symbol_df=symbol_df)

        dim_company_df.write\
            .mode("overwrite")\
            .parquet("s3a://gold/dim_company")
        data_loader.load(df=dim_company_df, table_name="dim_company")
    except Exception as e:
        traceback.print_exc() 

    try:
        LOGGER.info("create dim news")
        dim_news_df = dim_news(news_df=news_df, symbol_df=symbol_df)
        LOGGER.info(f"Dim news count: {dim_news_df.count()}")
        dim_news_df.printSchema()
        dim_news_df.show(20, truncate=False)

        dim_news_df.write\
            .mode("overwrite")\
            .parquet("s3a://gold/dim_news")
        dim_news_df.groupBy("news_id").count().filter("count > 1").show()
        data_loader.load(df=dim_news_df, table_name="dim_news")
    except Exception as e:
        traceback.print_exc()
    
    try:
        LOGGER.info("create dim financial concept")
        financial_concept = dim_financial(bs_df=finencial_bs_df,
                                         cf_df=finencial_cf_df,
                                         ic_df=finencial_ic_df)

        financial_concept.write\
            .mode("overwrite")\
            .parquet("s3a://gold/dim_financial_concept")
        data_loader.load(df=financial_concept, table_name="dim_financial_concept")
    except Exception as e:
        traceback.print_exc()

    # Build and persist fact tables
    try:
        LOGGER.info("create fact candles")
        fact_candles_df = fact_candles(candles_df=candles_df, symbol_df=symbol_df)

        fact_candles_df.write\
            .mode("overwrite")\
            .parquet("s3a://gold/fact_candles")
        data_loader.load(df=fact_candles_df, table_name="fact_candles")
    except Exception as e:
        traceback.print_exc()

    try:
        LOGGER.info("create fact earning")
        fact_earning_df = fact_earning(earning_df=earning_df, symbol_df=symbol_df)

        fact_earning_df.write\
            .mode("overwrite")\
            .parquet("s3a://gold/fact_earning")
        data_loader.load(df=fact_earning_df, table_name="fact_earnings")
    except Exception as e:
        traceback.print_exc()

    try:
        LOGGER.info("create fact market")
        fact_market_df = fact_market(market_df=market_df)

        fact_market_df.write\
            .mode("overwrite")\
            .parquet("s3a://gold/fact_market")
        data_loader.load(df=fact_market_df, table_name="fact_market")
    except Exception as e:
        traceback.print_exc()

    try:
        LOGGER.info("create fact financial balance sheet")
        balance_sheet = fact_financial_bs(financial_df=finencial_bs_df,
                                          symbol_df=symbol_df,
                                          dim_financial_concept=financial_concept)

        balance_sheet.write\
            .mode("overwrite")\
            .parquet("s3a://gold/fact_financial_balance_sheet")
        data_loader.load(df=balance_sheet, table_name="fact_financial_bs")
    except Exception as e:
        traceback.print_exc()

    try:
        LOGGER.info("create financial cash flow")
        cash_flow = fact_financial_cf(financial_df=finencial_cf_df,
                                      symbol_df=symbol_df,
                                      dim_financial_concept=financial_concept)

        cash_flow.write\
            .mode("overwrite")\
            .parquet("s3a://gold/fact_financial_cash_flow")
        data_loader.load(df=cash_flow, table_name="fact_financial_cf")
    except Exception as e:
        traceback.print_exc()

    try:
        LOGGER.info("create financial income statement")
        income_statement = fact_financial_ic(financial_df=finencial_ic_df,
                                             symbol_df=symbol_df,
                                             dim_financial_concept=financial_concept)
        LOGGER.info("Fact financial IC schema:")
        income_statement.printSchema()
        income_statement.show(5, truncate=False)

        income_statement.write\
            .mode("overwrite")\
            .parquet("s3a://gold/fact_financial_income_statement")
        data_loader.load(df=income_statement, table_name="fact_financial_ic")
    except Exception as e:
        traceback.print_exc() 


if __name__ == "__main__":
    main()