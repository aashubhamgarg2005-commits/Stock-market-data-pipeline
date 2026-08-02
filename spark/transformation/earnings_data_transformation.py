from pyspark.sql.functions import *

def clean_earnings_data(earning_df):
    """
    Function to clean the earnings data and return a transformed DataFrame.
    :param earning_df: Input DataFrame containing earnings data.
    :return: Transformed DataFrame with

    """
    return ( earning_df.\
        withColumn("actual", col("actual").cast("double"))
        .withColumn("estimate", col("estimate").cast("double"))
        .withColumn("period", to_date(col("period"), "yyyy-MM-dd"))
        .withColumn("quarter", col("quarter").cast("integer"))
        .withColumn("surprise", col("surprise").cast("double"))
        .withColumn("surprisePercent", col("surprisePercent").cast("double"))
        .withColumn("symbol",upper(trim(col("symbol"))))
        .withColumn("year", col("year").cast("integer"))
    )