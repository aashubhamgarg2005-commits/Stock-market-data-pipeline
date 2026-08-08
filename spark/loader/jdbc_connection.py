from producer.utils.logger import LOGGER
class PostgresLoader:
    def __init__(self,jdbc_url,user,password):
        self.jdbc_url = jdbc_url
        self.properties = {
            "user":user,
            "password":password,
            "driver":"org.postgresql.Driver"
        }

    def load(self,df,table_name,mode="append"):
        try:
            (
                df.write
                .format("jdbc")
                .option("url",self.jdbc_url)
                .option("dbtable",table_name)
                .option("user",self.properties["user"])
                .option("password",self.properties["password"])
                .option("driver",self.properties["driver"])
                .mode(mode)
                .save()
            )
            LOGGER.info(f"Successfully loaded data into {table_name}")
        except Exception as e:
            LOGGER.error(f"Load Failed {e}")