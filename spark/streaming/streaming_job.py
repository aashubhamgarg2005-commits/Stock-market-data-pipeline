from sparkSession import spark_session
from producer.config.constants import KAFKA_BROKER_URL
from producer.config.constants import STOCK_QUOTES_TOPIC

def main():
    spark = spark_session()
    spark.sparkContext.setLogLevel("WARN")

    df = spark.readStream\
        .format("kafka")\
        .option("kafks.bootstrap.servers",KAFKA_BROKER_URL)\
        .option("subscribe",STOCK_QUOTES_TOPIC)\
        .option("startingOffsets","latest")\
        .load()

    print(df)


if __name__ == "__main__":
    main()
