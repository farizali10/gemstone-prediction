import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

## Initializing Data Ingestion Configuration ##

# We use dataclass when we do not have to perform any functionalities inside our class.
@dataclass 
class DataIngestionConfig:
    # As we are using dataclass as decorator so it doesn't require a constructor (self)
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","raw.csv")

    # We used os.path as when working with Linux based systems it only recognizes paths given as os.path

# Creating a class for Data Ingestion:
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Method Started")
        
        try:
            # Extracting Dataset and Reading Dataset as Pandas DataFrame
            df = pd.read_csv(r'notebooks\data\gemstone.csv')
            logging.info("Dataset read as Pandas DataFrame")

            # Saving df to artifacts/raw.csv
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True) # exist_ok = True means don't create new folder if already created
            df.to_csv(self.ingestion_config.raw_data_path,index=False)  # We use index=False as we want to drop unique indexes for each record of the df
            logging.info("Saved the data to artifacts/raw.csv")

            # Performing Train Test Split
            logging.info("Train Test Split")
            train_set,test_set = train_test_split(df,test_size = 0.30, random_state = 36)

            # Storing Train & Test DataFrames to artifacts/train+test.csv in .csv format
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True) # header = True as we want column names too! 
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Train & Test Dataset successfully addedd to artifacts/train+test.csv")

            logging.info("Data Ingestion Completed")

            # We are returning train & test data path as in overview of data ingestion we are required to read a dataset and as output given the train and test data
            return (self.ingestion_config.train_data_path,self.ingestion_config.test_data_path)

        except Exception as e:
            logging.info("Exception occured at Data Ingestion")
            raise CustomException(e,sys)
