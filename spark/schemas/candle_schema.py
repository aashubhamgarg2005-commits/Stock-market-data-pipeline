from pyspark.sql.types import *

candles_schema = StructType([
    StructField("Meta Data",
                StructType([
                    StructField("1. Information",StringType(),True),
                    StructField("2. Symbol",StringType(),True),
                    StructField("3. Last Refreshed",StringType(),True),
                    StructField("4. Output Size",StringType(),True),
                    StructField("5. Time Zone",StringType(),True)
                ]),True
                ),
    StructField("Time Series (Daily)",
                MapType(
                    StringType(),
                    StructType([
                        StructField("1. open",StringType(),True),
                        StructField("2. high",StringType(),True),
                        StructField("3. low",StringType(),True),
                        StructField("4. close",StringType(),True),
                        StructField("5. volume",StringType(),True)
                    ])

                ),True)
])