import sys
import os
import pandas as pd

from src.components.data_ingestion import DataIngestionClass
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTrainer
from src.logger import logging
from src.exception import CustomException

class TrainingPipeline : 
    def data_ingestion(self):
        try:
            logging.info("Entering into the data ingestion ....")
            data_ingestion = DataIngestionClass()
            feature_file_path = data_ingestion.initiate_data_ingestion()
            logging.info("feature file path got successfully ")
            return feature_file_path
        except Exception as e:
            raise CustomException(e,sys)
    def data_transformation(self,feature_file_path ):
        try:
            logging.info("Entering into data transformation ....")
            data_transformation = DataTransformation(feature_file_path=feature_file_path)
            train_arr , test_arr , processor = data_transformation.initiate_data_transformation()
            logging.info("Data Transformation successfully completed!")
            return train_arr,test_arr,processor
        except Exception as e:
            raise CustomException(e,sys)
    def model_training(self,train_arr,test_arr):
        try:
            logging.info("Entering into model trainig and evaluating part ....")
            model = ModelTrainer()
            model_score = model.initiate_model_trainer(
                train_array=train_arr,
                test_array=test_arr
            )
            logging.info("Model Training successfully completed!")
            return model_score
        except Exception as e:
            raise CustomException(e,sys)
        
    def run_pipeline(self):
        try:
            feature_file_path = self.data_ingestion()
            train_arr , test_arr, preprocessor = self.data_transformation(feature_file_path=feature_file_path)
            r2_score=self.model_training(train_arr=train_arr,test_arr=test_arr)

            print(f"Training Completed Successfuly. Model Score is {r2_score}")
        except Exception as e:
            raise CustomException(e,sys)

