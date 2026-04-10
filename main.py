from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import TrainingPipelineConfig,\
                                                 DataIngestionConfig ,\
                                                 DataValidationConfig,\
                                                 DataTransformationConfig,\
                                                 ModelTrainerConfig    

from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact 
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer

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
        logging.info("INITIATE DATA validation !")
        data_validation_Artifact=datavalidationobject.initiat_data_validation()
        logging.info("data validation completed")
        print(data_validation_Artifact) 
        
        data_Transformation_Config=DataTransformationConfig(training_pipeline_config=trainigpiplelineconfig)
        data_transformation_object=DataTransformation(data_validation_artifact=data_validation_Artifact,
                                                      data_transformation_config=data_Transformation_Config)
        logging.info("INITIATE DATA TRANSFORMATION !")
        data_transformation_artifact=data_transformation_object.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data Transformation completed")
        
        model_trainer_config=ModelTrainerConfig(trainigpiplelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,
                                   data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_training()
        logging.info("Model Training artifact created")
        print(model_trainer_artifact)
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)

