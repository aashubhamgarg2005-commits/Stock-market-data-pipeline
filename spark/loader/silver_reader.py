from producer.utils.logger import LOGGER

class SilverReader:
    def __init__(self,spark):
        self.spark = spark

    def candles_reader(self):
        try:
            LOGGER.info("try to read data")
            candles_df = self.spark.read.parquet("s3a://silver/candles")

            return candles_df
        except Exception as e:
            LOGGER.error(f"failed to read data: {e}")
            raise

    def earning_reader(self):
            try:
                LOGGER.info("try to read data")
                earning_df = self.spark.read.parquet("s3a://silver/earnings")
    
                return earning_df
            except Exception as e:
                LOGGER.error(f"failed to read data: {e}")
                raise

    def finencial_bs_reader(self):
                try:
                    LOGGER.info("try to read data")
                    finencial_bs_df = self.spark.read.parquet("s3a://silver/finencial/bs")
        
                    return finencial_bs_df
                except Exception as e:
                    LOGGER.error(f"failed to read data: {e}")
                    raise

    def finencial_cf_reader(self):
                    try:
                        LOGGER.info("try to read data")
                        finencial_cf_df = self.spark.read.parquet("s3a://silver/finencial/cf")
            
                        return finencial_cf_df
                    except Exception as e:
                        LOGGER.error(f"failed to read data: {e}")
                        raise

    def finencial_ic_reader(self):
                    try:
                        LOGGER.info("try to read data")
                        finencial_ic_df = self.spark.read.parquet("s3a://silver/finencial/ic")
            
                        return finencial_ic_df
                    except Exception as e:
                        LOGGER.error(f"failed to read data: {e}")
                        raise

    def market_status_reader(self):
                        try:
                            LOGGER.info("try to read data")
                            market_df = self.spark.read.parquet("s3a://silver/market_status")
                
                            return market_df
                        except Exception as e:
                            LOGGER.error(f"failed to read data: {e}")
                            raise

    def news_reader(self):
                            try:
                                LOGGER.info("try to read data")
                                news_df = self.spark.read.parquet("s3a://silver/news")
                    
                                return news_df
                            except Exception as e:
                                LOGGER.error(f"failed to read data: {e}")
                                raise
    
        
        
    