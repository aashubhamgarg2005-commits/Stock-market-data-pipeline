from pyspark.sql.functions import *

def transform_news(df):
    return df.select(
        col("id").alias("news_id"),
        col("category"),
        col("headline"),
        col("summary"),
        col("source"),
        col("related").alias("symbol"),
        col("url").alias("article_url"),
        to_timestamp(from_unixtime(col("datetime"))).alias("published_at")
    ) 
    