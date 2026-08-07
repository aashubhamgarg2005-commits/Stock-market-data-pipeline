from pyspark.sql.functions import *

def fact_earning(symbol_df,earning_df):
    earning = (
        earning_df.join(
            symbol_df.filter(col("symbol").isNotNull())\
                                .select("symbol","symbol_id"),
                                on = "symbol",
                                how = "inner"
        ).
        select(
            "symbol_id",
            "year",
            "quarter",
            "period",
            "actual_eps",
            "estimated_eps",
            "eps_surprise",
            "surprise_percent",  
        ).
        withColumn("eps_beat_miss",
                   when(col("actual_eps") > col("estimated_eps"),"Beat")
                   .when(col("actual_eps") < col("estimated_eps"),"Miss")
                   .otherwise("Meet"))
        .withColumn("eps_surprise_abs",
                    abs(col("eps_surprise")))
        .withColumn("fiscal_year_quarter",
                    concat(
                        col("year").cast("string"),
                        lit("-Q"),
                        col("quarter").cast("string")
                    ))
    )

    return earning