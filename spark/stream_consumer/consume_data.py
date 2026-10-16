
from pyspark.sql.functions import (
    col,
    to_date,
)

from spark.streaming.stream_spark_session import spark_streaming
from producer.config.constants import (
    KAFKA_BROKER_URL,
    STOCK_QUOTES_TOPIC
)


def consume_stream_data():
    # Read stream from Kafka
    stock_quote = (
        spark_streaming.readStream
        .format("kafka")
        .option(
            "kafka.bootstrap.servers",
            KAFKA_BROKER_URL,
        )
        .option("subscribe",STOCK_QUOTES_TOPIC)
        .option("startingOffsets", "latest")
        .option("failOnDataLoss", "false")
        .load()
    )

    # Convert Kafka value from binary to string
    stock_quote_json = stock_quote.select(
        col("value").cast("string").alias("json_data"),
        col("timestamp").alias("kafka_timestamp"),
    )

    # Create partition date using Kafka timestamp
    stock_quote_json = stock_quote_json.withColumn(
        "events_date",
        to_date(col("kafka_timestamp")),
    )

    return stock_quote_json
