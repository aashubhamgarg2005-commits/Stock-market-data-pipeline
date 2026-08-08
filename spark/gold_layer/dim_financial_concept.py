from pyspark.sql.functions import *
from pyspark.sql.window import Window

def dim_financial(bs_df,cf_df,ic_df):
    window = Window.orderBy("statement_type","concept")
    
    bs_concept = (bs_df.select("concept","label").\
        withColumn("statement_type",lit("BS")))
    
    cf_concept = (cf_df.select("concept","label").\
        withColumn("statement_type",lit("CF")))
    
    ic_concept = (ic_df.select("concept","label").\
        withColumn("statement_type",lit("IC")))

    financial_concept = (
        bs_concept.unionByName(cf_concept).
        unionByName(ic_concept).
        dropDuplicates(["statement_type","concept"])
    )

    financial_concept = (
        financial_concept.
        withColumn("concept_id",row_number().over(window)).
        select(
            "concept_id",
            "statement_type",
            "concept",
            "label"
        )
    )
    return financial_concept
    