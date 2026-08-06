from pyspark.sql.types import *

market_schema = StructType([
    StructField("exchange",StringType(),True),
    StructField("holiday",StringType(),True),
    StructField("isOpen",BooleanType(),True),
    StructField("session",StringType(),True),
    StructField("t",LongType(),True),
    StructField("timezone",StringType(),True),
])