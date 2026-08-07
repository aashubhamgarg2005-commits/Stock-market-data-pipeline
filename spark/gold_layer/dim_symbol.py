from pyspark.sql.functions import *
from functools import reduce

def dim_symbol(candles_df,company_profile,
               earnings_df,financial_bs,
               financial_cf,financial_ic,
                news_df):
    symbols = [
        candles_df.select("symbol"),
        earnings_df.select("symbol"),
        company_profile.select("symbol"),
        financial_bs.select("symbol"),
        financial_cf.select("symbol"),
        financial_ic.select("symbol"),
        news_df.select("symbol")
    ]

    symbol_df = reduce(
        lambda df1,df2:df1.unionByName(df2),
        symbols
    ).filter(col("symbol").isNotNull())\
    .filter(trim(col("symbol")) != "")\
    .distinct()
    print("reduce module:", reduce.__module__)
    print("reduce:", reduce)


    symbol_df = symbol_df.withColumn(
        "symbol_id",monotonically_increasing_id() + lit(1)
    )

    return symbol_df

    
