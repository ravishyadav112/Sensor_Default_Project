import numpy as np 
import pandas as pd
import sys
import os 
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from src.constant import *
from src.utils.main_utils import MainUtils
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

@dataclass 
class DataTransformationConfig:
    artifact_dir = os.path.join(ARTIFACT_FOLDER)
    transformed_train_data = os.path.join(artifact_dir , "train_data.npy")
    transformed_test_data = os.path.join(artifact_dir , "test_data.npy")
    transformed_object_file_path = os.path.join(artifact_dir,'preprocessor.pkl')

class DataTransformation:
    def __init__(self,feature_file_path):
        self.feature_file_path=feature_file_path
        self.datatransformationconfig = DataTransformationConfig()
        self.utils = MainUtils()
    @staticmethod
    def get_data(feature_file_path : str) -> pd.DataFrame:
        try:
            df= pd.read_csv(feature_file_path)
            df.rename(columns={"Good/Bad" : TARGET_COLUMN}, inplace=True)
            return df
        except Exception as e:
            raise CustomException(e , sys)
    @staticmethod
    def get_transformer_object():
        try:
            imputer = SimpleImputer(strategy="constant", fill_value=0)
            scaler = RobustScaler()
            processor = Pipeline(steps=[
                ('imputer' , imputer) , 
                ("scaler" , scaler)]
                )
            return processor
        except Exception as e:
            raise CustomException(e , sys)
    def initiate_data_transformation(self):
        logging.info("Entered initiate_data_transformation method of Data Transformation class")
        try:
            dataframe=self.get_data(feature_file_path=self.feature_file_path)
            X = dataframe.drop(columns=TARGET_COLUMN)
            y = np.where(dataframe[TARGET_COLUMN]==-1,0,1)

            X_train, X_test, y_train , y_test = train_test_split(X,y,test_size = 0.2,random_state=42)

            preprocessor = self.get_transformer_object()

            X_train_scaled = preprocessor.fit_transform(X_train)
            X_test_scaled = preprocessor.transform(X_test)

            preprocessor_path = self.datatransformationconfig.transformed_object_file_path
            os.makedirs(os.path.dirname(preprocessor_path),exist_ok=True)

            self.utils.save_object(file_path=preprocessor_path,obj=preprocessor)

            train_arr = np.c_[X_train_scaled, np.array(y_train)]
            test_arr = np.c_[X_test_scaled,np.array(y_test)]

            return (train_arr, test_arr, preprocessor_path)
        except Exception as e:
            raise CustomException(e,sys) from e

        