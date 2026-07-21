class MinioReader():
    def __init__(self,spark):
        self.spark = spark

    def read_json(self,path):
        return self.spark.read.json(path)
        

    def read_parquet(self,path):
        return self.spark.read.parquet(path)
        