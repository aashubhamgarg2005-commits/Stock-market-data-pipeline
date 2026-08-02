from pyspark.sql.functions import *

def parse_news(df):
    return (df.withColumn("datetime",
                         from_unixtime(col("datetime"))))

def clean_news(df):
    return (
        df.dropDuplicates(["id"])\
        .dropna(subset=["headline"])\
        .filter(col("headline") != "")\
        .withColumn("headline",trim(col("headline")))\
        .drop("image")\
        .withColumn("related",trim(col("related")))\
        .fillna("Unknown",subset=["source"])\
        .withColumn("source",trim(col("source")))\
        .withColumn("summary",trim(col("summary")))\
        .withColumn("url",trim(col("url")))

    )

def transformation(df):
    df = parse_news(df=df)
    clean_df = clean_news(df=df)
    return clean_df


