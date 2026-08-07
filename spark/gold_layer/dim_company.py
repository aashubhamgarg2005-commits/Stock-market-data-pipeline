from pyspark.sql.functions import *
from functools import reduce

def dim_company(company_df,symbol_df):
    company = (
        company_df.join(
            symbol_df.filter(col("symbol").isNotNull())\
            .select("symbol","symbol_id"),
            on = "symbol",
            how = "inner"
        ).select("symbol_id",
                "company_name",
                "country",
                "currency",
                "estimate_currency",
                "exchange",
                "industry",
                "floating_share",
                "ipo_date",
                "logo_url",
                "market_cap",
                "phone",
                "shares_outstanding",
                "website",
                "processed_at")
        
    )

    return company