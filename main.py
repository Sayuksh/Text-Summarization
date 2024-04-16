from textSummarizer.components import data_ingestion
from textSummarizer.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.logging import logger

STAGE_NAME="Data ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\n x================x")
except Exception as e:
    raise e

STAGE_NAME="Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation=DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\n x================x")
except Exception as e:
    raise e