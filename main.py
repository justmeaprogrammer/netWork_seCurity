from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact 

import sys


if __name__=="__main__":
    try:
        trainigpiplelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainig_pipeline_config=trainigpiplelineconfig)
        dataingestion=DataIngestion(data_ingestion_config=dataingestionconfig)
        logging.info("Initiating Data Ingestion")
        dataingestionartifact=dataingestion.initiate_data_ingestion()
        logging.info("data initiation complpeet")
        print(dataingestionartifact)
        
        dataValidationConfig=DataValidationConfig(trainigpiplelineconfig)
        datavalidationobject=DataValidation(data_ingestion_artifact=dataingestionartifact,
                                            data_validation_config=dataValidationConfig)
        logging.info("INITIATE DATA INGESTION !")
        data_validation_artifact=datavalidationobject.initiat_data_validation()
        logging.info("data validation completed")
        print(data_validation_artifact)        
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)


