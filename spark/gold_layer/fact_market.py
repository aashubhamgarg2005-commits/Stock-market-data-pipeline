from pyspark.sql.functions import *

def fact_market(market_df):
    fact_market_df = (
        market_df.select(
            "exchange",
            "holiday",
            "is_open",
            "session",
            "market_time",
            "timezone"
        )
        .withColumn("market_status",when(col("is_open"),"open")
                    .otherwise("close"))
        .withColumn("is_regular_session",when(col("session") == "regular","true").
                   otherwise("false"))
        .withColumn("market_date",to_date(col("market_time")))
        .withColumn("market_year",year(col("market_time")))
        .withColumn("market_month",month(col("market_time")))
        .withColumn("market_quarter",quarter(col("market_time")))
        .withColumn("market_day",day(col("market_time")))
        .withColumn("market_hour",hour(col("market_time")))
    )

    return fact_market_df