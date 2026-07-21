from pyspark.sql import SparkSession

def spark_session():
    spark = (SparkSession.builder\
    .appName("StockMarketBatch")\
    .config("spark.haoop.fs.s3a.endpoint","http://minio:9000")\
    .config("spark.hadoop.fs.s3a.access.key","minioadmin")\
    .config("spark.hadoop.fs.s3a.secret.key","minioadmin")\
    .config("spark.hadoop.fs.s3a.path.style.access","true")\
    .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false")\
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    .getOrCreate()
    ) 
    return spark