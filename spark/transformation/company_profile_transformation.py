from pyspark.sql.functions import *

def cleaning_company(df):
    return (df.dropDuplicates("ticker")\
            .withColumn("ticker",trim(col("ticker")))\
            .withColumn("name",trim(col("name")))\
            .withColumn("country",trim(col("country")))\
            .withColumn("currency",trim(col("currency")))\
            .withColumn("estimateCurrency",trim(col("estimateCurrency")))\
            .withColumn("exchange",trim(col("exchange")))\
            .withColumn("ipo",to_date(col("ipo"), "yyyy-MM-dd"))\
            .drop("logo")\
            .withColumn("finnhubIndustry",trim(col("finnhubIndustry")))\
            .drop("phone")\
            .withColumn("weburl",trim(col("weburl")))
            )