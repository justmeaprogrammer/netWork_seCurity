from datetime import datetime
import os
from datetime import datetime
from networksecurity.constant import trainig_pipeline

class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp=timestamp.strftime('%m_%d_%Y_%H_%M_%S')
        self.pipeline_name=trainig_pipeline.PIPELINE_NAME
        self.artifact_name=trainig_pipeline.ARTIFACT_DIR
        self.artifact_dir=os.path.join(self.artifact_name,timestamp)
        self.timestamp:str=timestamp
        

class DataIngestionConfig:
    def __init__(self,trainig_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir:str = os.path.join(
            trainig_pipeline_config.artifact_dir,trainig_pipeline.DATA_INGESTION_DIR_NAME
        )
        
        self.feature_store_file_path:str = os.path.join(
            self.data_ingestion_dir,trainig_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,
            trainig_pipeline.FILE_NAME
        )
        
        self.training_file_path:str = os.path.join(
            self.data_ingestion_dir,trainig_pipeline.DATA_INGESTION_INGESTED_DIR,
            trainig_pipeline.TRAIN_FILE_NAME
        )
        
        self.testing_file_path:str = os.path.join(
            self.data_ingestion_dir,trainig_pipeline.DATA_INGESTION_INGESTED_DIR,
            trainig_pipeline.TEST_FILE_NAME
        )
        
        self.train_test_split_ratio:float = trainig_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.collection_name:str = trainig_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name:str = trainig_pipeline.DATA_INGESTION_DATABASE_NAME 