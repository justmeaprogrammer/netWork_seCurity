import yaml
import os,sys
import numpy as np
import pickle

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

def read_yaml_file(file_path:str) -> dict:
    try:
        with open(file_path,"rb") as file_obj:
            return yaml.safe_load(file_obj)
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
    
def write_yaml(file_path:str,content:object,replace:bool = False)-> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w") as file_obj:
            yaml.dump(content,file_obj)    
    except Exception as e:
        raise NetworkSecurityException(e,sys)  
    
    

def save_numpy_array_data(file_path:str,array:np.array):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            np.save(file_obj,array)
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
    
def load_numpy_array_data(file_path:str)->np.array:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file path:{file_path} is invalid")
        
        with open(file_path,"rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
    
def save_object(file_path:str, obj:object):
    try:
        logging.info("Entered the save_object method of MainUtils class")
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj=obj,file=file_obj)
            
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
    
def load_object(file_path:str)->object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file path:{file_path} doesnt exists")
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
    
def evaluate_models(xtrain,ytrain,xtest,ytest,models:dict,params:dict):
    try:
        report={}
        
        for i in range(len(list(models))):
            model=list(models.values())[i]
            parameter=params[list(models.keys())[i]]
            
            gs=GridSearchCV(estimator=model,
                            param_grid=parameter,
                            cv=3,
                            n_jobs=-1,
                            verbose=0)
            gs.fit(xtrain,ytrain)
            
            model.set_params(**gs.best_params_)
            model.fit(xtrain,ytrain)
            y_train_pred = model.predict(xtrain)

            y_test_pred = model.predict(xtest)

            
            test_model_score=accuracy_score(y_true=ytest,y_pred=y_test_pred)
            report[list(models.keys())[i]] = test_model_score

        return report

            
        
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
