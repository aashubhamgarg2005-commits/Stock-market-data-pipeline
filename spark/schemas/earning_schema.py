from pyspark.sql.types import *

earnings_schema = StructType([
    StructField("actual",DoubleType(),True),
    StructField("estimate",DoubleType(),True),
    StructField("period",StringType(),True),
    StructField("quarter",LongType(),True),
    StructField("surprise",DoubleType(),True),
    StructField("surprisePercent",DoubleType(),True),
    StructField("symbol",StringType(),True),
    StructField("year",LongType(),True)
])