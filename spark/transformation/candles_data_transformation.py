from pyspark.sql.functions import *


def clean_candles_df(df):
    valid_df = df.filter(
        col("Meta Data").isNotNull() &
        col("Time Series (Daily)").isNotNull()
    )
    valid_df.select(
    explode(col("Time Series (Daily)")).alias("trade_date", "price")
).select("price.*").show(5, truncate=False)

    clean_df = valid_df.select(
        col("Meta Data.`2. Symbol`").alias("symbol"),
        explode(col("Time Series (Daily)")).alias("trade_date", "price")
    )\
    .select(
        trim(col("symbol")).alias("symbol"),
        col("trade_date").cast("date"),
        col("price.`1. open`").cast("double").alias("open"),
        col("price.`2. high`").cast("double").alias("high"),
        col("price.`3. low`").cast("double").alias("low"),
        col("price.`4. close`").cast("double").alias("close"),
        col("price.`5. volume`").cast("long").alias("volume")
    )

    return clean_df