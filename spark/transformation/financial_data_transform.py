from pyspark.sql.functions import col, explode, trim,expr


def clean_financial_data(df):

    # Explode outer data array
    financial_df = (
        df.select(
            explode(col("data")).alias("data")
        )
    )

    # -----------------------------
    # Balance Sheet
    # -----------------------------
    balance_sheet_df = (
        financial_df
        .select(
            trim(col("data.symbol")).alias("symbol"),
            col("data.year").cast("int").alias("year"),
            col("data.quarter").cast("int").alias("quarter"),
            explode(col("data.report.bs")).alias("bs")
        )
        .select(
            col("symbol"),
            col("year"),
            col("quarter"),
            trim(col("bs.concept")).alias("concept"),
            trim(col("bs.label")).alias("label"),
            trim(col("bs.unit")).alias("unit"),
            expr("try_cast(bs.value as double)").alias("value")
        )
    )

    # -----------------------------
    # Cash Flow
    # -----------------------------
    cash_flow_df = (
        financial_df
        .select(
            trim(col("data.symbol")).alias("symbol"),
            col("data.year").cast("int").alias("year"),
            col("data.quarter").cast("int").alias("quarter"),
            explode(col("data.report.cf")).alias("cf")
        )
        .select(
            col("symbol"),
            col("year"),
            col("quarter"),
            trim(col("cf.concept")).alias("concept"),
            trim(col("cf.label")).alias("label"),
            trim(col("cf.unit")).alias("unit"),
            expr("try_cast(cf.value as double)").alias("value")
        )
    )

    # -----------------------------
    # Income Statement
    # -----------------------------
    income_statement_df = (
        financial_df
        .select(
            trim(col("data.symbol")).alias("symbol"),
            col("data.year").cast("int").alias("year"),
            col("data.quarter").cast("int").alias("quarter"),
            explode(col("data.report.ic")).alias("ic")
        )
        .select(
            col("symbol"),
            col("year"),
            col("quarter"),
            trim(col("ic.concept")).alias("concept"),
            trim(col("ic.label")).alias("label"),
            trim(col("ic.unit")).alias("unit"),
            expr("try_cast(ic.value as double)").alias("value")
        )
    )

    return (
        balance_sheet_df,
        cash_flow_df,
        income_statement_df
    )