from pyspark.sql.types import *


News_schema = StructType([
    StructField("category",StringType(),True),
    StructField("datetime",LongType(),True),
    StructField("headline",StringType(),True),
    StructField("id",LongType(),True),
    StructField("image",StringType(),True),
    StructField("related",StringType(),True),
    StructField("source",StringType(),True),
    StructField("summary",StringType(),True),
    StructField("url",StringType(),True)

])
