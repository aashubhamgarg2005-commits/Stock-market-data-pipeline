from producer.utils.logger import LOGGER

class SilverReader:
    def __init__(self,spark):
        self.spark = spark

    def candles_reader(self,path):
        try:
            LOGGER.info("try to read data")
            candles_df = self.spark.read.parquet(path)

            return candles_df
        except Exception as e:
            LOGGER.error(f"failed to read data: {e}")
            raise

    def earning_reader(self,path):
            try:
                LOGGER.info("try to read data")
                earning_df = self.spark.read.parquet(path)
    
                return earning_df
            except Exception as e:
                LOGGER.error(f"failed to read data: {e}")
                raise

    def finencial_bs_reader(self,path):
                try:
                    LOGGER.info("try to read data")
                    finencial_bs_df = self.spark.read.parquet(path)
        
                    return finencial_bs_df
                except Exception as e:
                    LOGGER.error(f"failed to read data: {e}")
                    raise

    def finencial_cf_reader(self,path):
                    try:
                        LOGGER.info("try to read data")
                        finencial_cf_df = self.spark.read.parquet(path)
            
                        return finencial_cf_df
                    except Exception as e:
                        LOGGER.error(f"failed to read data: {e}")
                        raise

    def finencial_ic_reader(self,path):
                    try:
                        LOGGER.info("try to read data")
                        finencial_ic_df = self.spark.read.parquet(path)
            
                        return finencial_ic_df
                    except Exception as e:
                        LOGGER.error(f"failed to read data: {e}")
                        raise

    def market_status_reader(self,path):
                        try:
                            LOGGER.info("try to read data")
                            market_df = self.spark.read.parquet(path)
                
                            return market_df
                        except Exception as e:
                            LOGGER.error(f"failed to read data: {e}")
                            raise

    def news_reader(self,path):
                            try:
                                LOGGER.info("try to read data")
                                news_df = self.spark.read.parquet(path)
                    
                                return news_df
                            except Exception as e:
                                LOGGER.error(f"failed to read data: {e}")
                                raise

    def company_profile_reader(self,path):
        try:
            LOGGER.info("try to read data")
            company_df = self.spark.read.parquet(path)
                               
            return company_df
        except Exception as e:
            LOGGER.error(f"failed to read data: {e}")
            raise
           
    
        
        
    