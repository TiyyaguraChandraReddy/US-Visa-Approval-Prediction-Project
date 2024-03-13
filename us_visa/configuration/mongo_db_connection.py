import os
from us_visa.constant import DATABASE_NAME, MONGODB_URL_KEY
from us_visa.logger import logging
from us_visa.exception import USvisaException
import pymongo
import certifi
import sys

ca = certifi.where()

class MongoDBClient:
    """
    Class Name : export_data_into_feature_store
    Description : This method exports the dataframe from mongodb feature store as dataframe

    output : connection to mongodb database
    On Failure : raise an exception
    """
    client = None

    def __init__(self, database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                if mongo_db_url is None:
                    raise Exception(f"Environment key : {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile = ca)
            self.client = MongoDBClient.client
            self.databse = self.client[database_name]
            self.database_name = database_name
            logging.info("MonoDB Connection Successfull")
        except Exception as e:
            raise USvisaException(e, sys) from e
        
