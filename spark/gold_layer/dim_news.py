from pyspark.sql.functions import *
def dim_news(news_df,symbol_df):
    news_df = news_df.join(
                symbol_df.filter(col("symbol").isNotNull())\
                                    .select("symbol","symbol_id"),
                                    on = "symbol",
                                    how = "inner"
            ).\
    select(
        "news_id",
        "symbol_id",
        "category",
        "headline",
        "summary",
        "source",
        "article_url",
        "published_at"
    )

    return news_df