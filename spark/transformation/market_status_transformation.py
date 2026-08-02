from pyspark.sql.functions import *

def clean_market(df):
    return (
        df.dropDuplicates(["exchange"])\
        .withColumn("exchange",trim(col("exchange")))\
        .fillna({"exchange":"Unknown",
                "holiday":"No Holiday",
                "session":"Unknown",
                "timezone":"Unknown"})\
        .withColumn("session",trim(col("session")))\
        .withColumn(
                    "market_timestamp",
                    to_timestamp(from_unixtime(col("t")))
                 )
                    .drop("t")\
        .withColumnRenamed("timezone","market_timezone")
    )