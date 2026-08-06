from spark.sparkSession import spark_session
from silver_reader import SilverReader

def main():
    spark = spark_session()
    silver_read = SilverReader(spark=spark)
    candles_df = silver_read.candles_reader()
    candles_df.show()
    earning_df = silver_read.earning_reader()
    earning_df.show()
    finencial_bs_df = silver_read.finencial_bs_reader()
    finencial_bs_df.show()
    finencial_cf_df = silver_read.finencial_cf_reader()
    finencial_cf_df.show()
    finencial_ic_df = silver_read.finencial_ic_reader()
    finencial_ic_df.show()

    market_df = silver_read.market_status_reader()
    market_df.show()
    news_df = silver_read.news_reader()
    news_df.show()

if __name__ == "__main__":
    main()