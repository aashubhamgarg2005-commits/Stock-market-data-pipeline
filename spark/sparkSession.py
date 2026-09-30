from pyspark.sql import SparkSession


def spark_session():

    spark = (
        SparkSession.builder
        .appName("StockMarketBatch")
        .master("local[*]")

        # S3A / MinIO + PostgreSQL JDBC dependencies
        .config(
            "spark.jars.packages",
            "org.apache.hadoop:hadoop-aws:3.5.0,"
            "org.postgresql:postgresql:42.7.7"
        )

        # MinIO endpoint
        .config(
            "spark.hadoop.fs.s3a.endpoint",
            "http://localhost:9000"
        )

        # MinIO credentials
        .config(
            "spark.hadoop.fs.s3a.access.key",
            "minioadmin"
        )
        .config(
            "spark.hadoop.fs.s3a.secret.key",
            "minioadmin"
        )

        # MinIO configuration
        .config(
            "spark.hadoop.fs.s3a.path.style.access",
            "true"
        )
        .config(
            "spark.hadoop.fs.s3a.connection.ssl.enabled",
            "false"
        )

        # S3A filesystem
        .config(
            "spark.hadoop.fs.s3a.impl",
            "org.apache.hadoop.fs.s3a.S3AFileSystem"
        )

        # MinIO region
        .config(
            "spark.hadoop.fs.s3a.endpoint.region",
            "us-east-1"
        )

        .getOrCreate()
    )

    return spark