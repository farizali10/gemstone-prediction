import os
import sys
import pickle
import numpy as np 
import pandas as pd
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

from src.exception import CustomException
from src.logger import logging

def save_object(file_path,obj):
    """This function will save contents of a file (obj) as per the given file path """
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        logging.info("Error occured during saving file {file_path}")
        raise CustomException(e,sys)

def evaluate_model(X_train,y_train,X_test,y_test,models):
    """This function will perform performance metrics based upon given model names (models) for Train Data"""
    try:
        report = {}

        for i in range(len(models)):
            model = list(models.values())[i]

            # Training Model
            model.fit(X_train,y_train)

            # Predicting Test data
            y_test_pred = model.predict(X_test)

            # Get R2 scores for train and test data
            #train_model_score = r2_score(y_train,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] = test_model_score
        
        return report

    except Exception as e:
        logging.info("Exception occured during model training")
        raise(CustomException(e,sys))
