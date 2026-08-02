from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,  
    IntegerType, 
)

earnings_schema = StructType([
    StructField("actual",DoubleType(),True),
    StructField("estimate",DoubleType(),True),
    StructField("period",StringType(),True),
    StructField("quarter",IntegerType(),True),
    StructField("surprise",DoubleType(),True),
    StructField("surprisePercent",DoubleType(),True),
    StructField("symbol",StringType(),True),
    StructField("year",IntegerType(),True)
])