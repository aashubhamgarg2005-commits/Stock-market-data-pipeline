from pyspark.sql.functions import *

def fact_financial_ic(financial_df,symbol_df,dim_financial_concept):
    fact_income_statement = (
                        financial_df.alias("f").join(
                        symbol_df.filter(col("symbol").isNotNull())\
                        .select("symbol","symbol_id")
                        .alias("s"),
                        on = "symbol",
                        how = "inner"

    ).join(
        dim_financial_concept.filter(col("statement_type") == "IC")
        .select("concept","concept_id")
        .alias("c"),
        col("f.concept") == col("c.concept"),
        how="inner"
    )
    .select(
        col("s.symbol_id"),
        col("c.concept_id"),
        col("f.year"),
        col("f.quarter"),
        col("f.value"),
        col("f.unit")
        
    )
)  
    
    return fact_income_statement