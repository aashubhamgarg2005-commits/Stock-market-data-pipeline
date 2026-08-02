from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType
)

company_profile_schema = StructType([
    StructField("ticker",StringType(),True),
    StructField("name",StringType(),True),
    StructField("country",StringType(),True),
    StructField("currency",StringType(),True),
    StructField("estimateCurrency",StringType(),True),
    StructField("exchange",StringType(),True),
    StructField("ipo",StringType(),True),
    StructField("marketCapitalization",DoubleType(),True),
    StructField("logo",StringType(),True),
    StructField("shareOutstanding",DoubleType(),True),
    StructField("finnhubIndustry",StringType(),True),
    StructField("phone",StringType(),True),
    StructField("weburl",StringType(),True),
    StructField("floatingShare",DoubleType(),True)
])