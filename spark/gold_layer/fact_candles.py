from pyspark.sql.functions import *
from pyspark.sql.window import Window


def fact_candles(candles_df,symbol_df):
    window_spec = Window.partitionBy("symbol_id").orderBy("trade_date")
    candles = (
                candles_df.join(
                    symbol_df.filter(col("symbol").isNotNull())\
                    .select("symbol","symbol_id"),
                    on = "symbol",
                    how = "inner"
                ).select(
                    "symbol_id",
                    "open",
                    "high",
                    "low",
                    "close",
                    "volume",
                    "trade_date",
                    round(col("close") - col("open"), 2).alias("price_change"),
                    round(((col("close") - col("open")) / col("open")) * 100, 2).alias("price_change_pct"),
                    round(col("high") - col("low"), 2).alias("daily_change"),
                    round(((col("high") - col("low")) / col("low")) * 100, 2).alias("daily_change_pct")
        )
        .withColumn(
            "previous_volume",
            lag("volume").over(window_spec)
        )
        .withColumn(
            "volume_change_pct",
            round(
                ((col("volume") - col("previous_volume")) / col("previous_volume")) * 100,
                2
            )
        )
        .drop("previous_volume")
                    )



    return candles