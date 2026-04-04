from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys


if __name__=="__main__":
    try:
        trainigpiplelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainig_pipeline_config=trainigpiplelineconfig)
        dataingestion=DataIngestion(data_ingestion_config=dataingestionconfig)
        logging.info("Initiating Data Ingestion")
        dataingestionartifact=dataingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)


