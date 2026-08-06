from pyspark.sql.functions import *

def clean_earnings_df(df):
    return df.select(
        trim(col("symbol")).alias("symbol"),
        col("year").cast("int").alias("year"),
        col("quarter").cast("int").alias("quarter"),
        to_date(col("period")).alias("period"),
        round(col("actual"), 2).alias("actual_eps"),
        round(col("estimate"), 2).alias("estimated_eps"),
        round(col("surprise"), 2).alias("eps_surprise"),
        round(col("surprisePercent"), 2).alias("surprise_percent")
    )