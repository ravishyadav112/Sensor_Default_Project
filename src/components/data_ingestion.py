import sys
import os
import pandas as pd
import numpy as np
from  src.constant import *
from src.utils.main_utils import MainUtils
from src.exception import CustomException
from src.logger import logging
from pymongo import MongoClient
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    artifact_folder : str = os.path.join(ARTIFACT_FOLDER)

class DataIngestionClass : 
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.utils = MainUtils()

    def export_collection_as_dataframe(self , collection_name : str , database_name : str) -> pd.DataFrame:
        try:
            logging.info("Connecting with the MongoDB")
            client = MongoClient(MONGO_DB_URL)
            collection = client[database_name][collection_name]
            logging.info("Fetching the Data with the mongodb")
            df = pd.DataFrame(list(collection.find()))
            logging.info("Data Fetched Sucessfully")

            if "_id" in df.columns.to_list():
                df.drop("_id" , axis=1 , inplace=True)
            df.replace({"na" : np.nan} ,inplace=True)

            return df
        except Exception as e :
            raise CustomException(e , sys)
            
    
    def save_dataframe_to_feature_file_path(self) -> str:
        try:
            logging.info("Fetching the path  for saving it to csv file")
            raw_file_path = self.data_ingestion_config.artifact_folder

            os.makedirs(raw_file_path, exist_ok=True)
            feature_file_path =os.path.join(raw_file_path , "wafer_fault.csv")

            sensor_data = self.export_collection_as_dataframe(collection_name=MONGO_COLLECTION_NAME,database_name=MONGO_DATABASE_NAME)
            logging.info(f"Saving exported data into feature store file path : {raw_file_path}")

            sensor_data.to_csv(feature_file_path , index = False)
            logging.info("Saved Successfully")

            return feature_file_path
        except Exception as e:
            raise CustomException(e , sys)
    def  initiate_data_ingestion(self) -> str:
        logging.info("Entered initiated_data_ingestion method of data_integration class")

        try:
            feature_file_path = self.save_dataframe_to_feature_file_path()

            logging.info("got the data from mongodb")   

            logging.info("exited and initiated data_ingestion method of data ingestion  class")
            return feature_file_path
        except Exception as e:
            raise CustomException(e,sys)        

    

