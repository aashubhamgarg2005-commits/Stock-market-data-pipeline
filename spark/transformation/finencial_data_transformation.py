from pyspark.sql.functions import *
from pyspark.sql.types import DoubleType

def transform_finencial_data(df):
    """
    Transforms the financial data DataFrame by performing necessary transformations.

    Args:
        df (DataFrame): Input DataFrame containing financial data.

    Returns:
        DataFrame: Transformed DataFrame with necessary transformations applied.    
 """
    # Explode Data
    df_data = df.withColumn(
        "data_item",explode_outer(col("data"))
    )

    # Common Finencial data

    df_data = df_data.select(
        col("cik").alias("company_cik"),
        col("symbol").alias("symbol"),
        col("data_item.acceptedDate").alias("accepted_date"),
        col("data_item.accessNumber").alias("access_number"),
        col("data_item.cik").alias("data_cik"),
        col("data_item.endDate").alias("end_date"),
        col("data_item.filedDate").alias("filed_date"),
        col("data_item.form").alias("form"),
        col("data_item.quarter").alias("quarter"),
        col("data_item.startDate").alias("start_date"),
        col("data_item.symbol").alias("data_symbol"),
        col("data_item.year").alias("year"),

        col("data_item.report.bs").alias("bs"),
        col("data_item.report.cf").alias("cf"),
        col("data_item.report.ic").alias("ic")
    )

    # Clean metadata

    df_data = (
        df_data.withColumn("accepted_date",to_timestamp(col("accepted_date")))
        .withColumn("filed_date",to_date(col("filed_date")))
        .withColumn("end_date",to_date(col("end_date")))
        .withColumn("start_date",to_date(col("start_date")))
        .withColumn("symbol",trim(col("symbol")))
        .withColumn("form",trim(col("form")))
    )

    # Balance Sheet(bs)

    df_bs = df_data\
        .withColumn("bs_item",explode_outer(col("bs")))\
        .select(
            col("company_cik"),
            col("symbol"),
            col("accepted_date"),
            col("access_number"),
            col("data_cik"),
            col("end_date"),
            col("filed_date"),
            col("form"),
            col("quarter"),
            col("start_date"),
            col("year"),

            col("bs_item.concept").alias("concept"),
            col("bs_item.label").alias("label"),
            col("bs_item.unit").alias("unit"),
            col("bs_item.value").alias("value")
        )

    # Cash Flow(Cf)
    df_cf = df_data\
        .withColumn("cf_item",explode_outer(col("cf")))\
        .select(
            col("company_cik"),
            col("symbol"),
            col("accepted_date"),
            col("access_number"),
            col("data_cik"),
            col("end_date"),
            col("filed_date"),
            col("form"),
            col("quarter"),
            col("start_date"),
            col("year"),

            col("cf_item.concept").alias("concept"),
            col("cf_item.label").alias("label"),
            col("cf_item.unit").alias("unit"),
            col("cf_item.value").alias("value")
        )

    # Income Statement(ic)
    df_ic = df_data\
        .withColumn("ic_item",explode_outer(col("ic")))\
        .select(
            col("company_cik"),
            col("symbol"),
            col("accepted_date"),
            col("access_number"),
            col("data_cik"),
            col("end_date"),
            col("filed_date"),
            col("form"),
            col("quarter"),
            col("start_date"),
            col("year"),

            col("ic_item.concept").alias("concept"),
            col("ic_item.label").alias("label"),
            col("ic_item.unit").alias("unit"),
            col("ic_item.value").alias("value")
        )

    # Convert Corretct Data Type
    df_bs = df_bs.withColumn("value", when(col("value") == "N/A", None).
                             otherwise(regexp_replace(col("value"),",","").cast(DoubleType())))
    df_cf = df_cf.withColumn("value", when(col("value") == "N/A", None).
                             otherwise(regexp_replace(col("value"),",","").cast(DoubleType())))
    df_ic = df_ic.withColumn("value", when(col("value").cast("string") == "N/A", None).
                             otherwise(regexp_replace(col("value"),",","").cast(DoubleType())))


    # Remove Invalid Record

    df_bs = df_bs.filter(col("concept").isNotNull())
    df_cf = df_cf.filter(col("concept").isNotNull())
    df_ic = df_ic.filter(col("concept").isNotNull())

    # Drop Duplicates

    df_bs = df_bs.dropDuplicates()
    df_cf = df_cf.dropDuplicates()
    df_ic = df_ic.dropDuplicates()

    # Record Column
    final_column = [
        "symbol",
        "company_cik",
        "concept",
        "label",
        "unit",
        "value",
        "form",
        "year",
        "quarter",
        "start_date",
        "end_date",
        "filed_date",
        "accepted_date",
        "access_number",
        "data_cik"
    ]

    df_bs = df_bs.select(final_column)
    df_cf = df_cf.select(final_column)
    df_ic = df_ic.select(final_column)

    return df_bs,df_cf,df_ic