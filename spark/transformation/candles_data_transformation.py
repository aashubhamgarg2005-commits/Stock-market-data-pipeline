from pyspark.sql.functions import col, to_date, to_timestamp, explode

def parse_candles_data(candle_df):
    """
    Function to parse the candles data and return a transformed DataFrame.
    :param candle_df: Input DataFrame containing candles data.
    :return: Transformed DataFrame with parsed candles data
    """
    return (candle_df.select(
        col("`Meta Data`.`2. Symbol`").alias("symbol"),
        explode(col("`Time Series (Daily)`")).alias("trade_date", "price"))
        .select(
            col("symbol"),
            to_date(col("trade_date"), "yyyy-MM-dd").alias("trade_date"),
            col("price.`1. open`").cast("double").alias("open"),
            col("price.`2. high`").cast("double").alias("high"),
            col("price.`3. low`").cast("double").alias("low"),
            col("price.`4. close`").cast("double").alias("close"),
            col("price.`5. volume`").cast("long").alias("volume")
        )
    )


            