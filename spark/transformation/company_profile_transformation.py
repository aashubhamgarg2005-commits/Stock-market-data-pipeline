from pyspark.sql.functions import *

def clean_company_profile(df):
    return df.select(
        trim(col("ticker")).alias("symbol"),
        trim(col("name")).alias("company_name"),
        upper(trim(col("country"))).alias("country"),
        upper(trim(col("currency"))).alias("currency"),
        trim(col("estimateCurrency")).alias("estimate_currency"),
        trim(col("exchange")).alias("exchange"),
        trim(col("finnhubIndustry")).alias("industry"),
        col("floatingShare").cast("double").alias("floating_share"),
        to_date("ipo").alias("ipo_date"),
        trim(col("logo")).alias("logo_url"),
        col("marketCapitalization").cast("double").alias("market_cap"),
        trim(col("phone")).alias("phone"),
        col("shareOutstanding").cast("double").alias("shares_outstanding"),
        trim(col("weburl")).alias("website"),
        current_timestamp().alias("processed_at")
    ).dropDuplicates(["symbol"])