from pyspark.sql.types import StructType
from pyspark.sql import DataFrame

class MinioReader():
    def __init__(self,spark):
        self.spark = spark

    def read_json(self,path,schema:StructType = None) -> DataFrame:
        reader = self.spark.read.option("multiLine", True)
        if schema is not None:
            reader = reader.schema(schema)
        return reader.json(path)
        

    def read_parquet(self,path:str) -> DataFrame: 
        return self.spark.read.parquet(path)
        