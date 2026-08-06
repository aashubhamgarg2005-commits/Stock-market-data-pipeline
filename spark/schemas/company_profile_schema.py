from pyspark.sql.types import *

company_schema = StructType([
    StructField("country",StringType(),True),
    StructField("currency",StringType(),True),
    StructField("estimateCurrency",StringType(),True),
    StructField("exchange",StringType(),True),
    StructField("finnhubIndustry",StringType(),True),
    StructField("floatingShare",DoubleType(),True),
    StructField("ipo",StringType(),True),
    StructField("logo",StringType(),True),
    StructField("marketCapitalization",DoubleType(),True),
    StructField("name",StringType(),True),
    StructField("phone",StringType(),True),
    StructField("shareOutstanding",DoubleType(),True),
    StructField("ticker",StringType(),True),
    StructField("weburl",StringType(),True),

])