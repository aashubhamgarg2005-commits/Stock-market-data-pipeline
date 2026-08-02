from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
    LongType,
    ArrayType,
)

FinancialSchema = StructType([
    StructField("cik", StringType(), True),
    StructField("data", ArrayType(StructType([
        StructField("acceptedDate", StringType(), True),
        StructField("accessNumber", StringType(), True),
        StructField("cik", StringType(), True),
        StructField("endDate", StringType(), True),
        StructField("filedDate", StringType(), True),
        StructField("form", StringType(), True),
        StructField("quarter", LongType(), True),
        StructField("report",StructType([
            StructField("bs", ArrayType(StructType([
                StructField("concept", StringType(), True),
                StructField("label", StringType(), True),
                StructField("unit", StringType(), True),
                StructField("value", StringType(), True)
            ])), True),
            StructField("cf", ArrayType(StructType([
                StructField("concept", StringType(), True),
                StructField("label", StringType(), True),
                StructField("unit", StringType(), True),
                StructField("value", StringType(), True)
            ])),True),
            StructField("ic", ArrayType(StructType([
                StructField("concept", StringType(), True),
                StructField("label", StringType(), True),
                StructField("unit", StringType(), True),
                StructField("value", DoubleType(), True)
        ])), True),
        ]), True),
        StructField("startDate", StringType(), True),
        StructField("symbol", StringType(), True),
        StructField("year", LongType(), True)
    ])), True),
    StructField("symbol", StringType(), True),
])