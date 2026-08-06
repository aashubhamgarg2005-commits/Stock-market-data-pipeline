from pyspark.sql.functions import *

def clean_market_status(df):
    return df.select(
        trim(col("exchange")).alias("exchange"),
        when(col("holiday").isNull(),"Not provided")
        .otherwise(col("holiday")).alias("holiday"),
        col("isOpen").alias("is_open"),
        trim(col("session")).alias("session"),
        to_timestamp(from_unixtime(col("t"))).alias("market_time"),
        trim(col("timezone")).alias("timezone")
    )