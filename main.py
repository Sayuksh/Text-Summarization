from textSummarizer.components import data_ingestion, model_evalution, model_trainer
from textSummarizer.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.pipline.stage_03_data_transformation import DataTransformationPipeline
from textSummarizer.pipline.stage_04_model_trainer import ModelTrainerPipeline
from textSummarizer.pipline.stage_05_model_evalution import ModelEvalutionPipeline
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


STAGE_NAME="Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation=DataTransformationPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\n x================x")
except Exception as e:
    raise e

STAGE_NAME="Model Trainer stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer=ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\n x================x")
except Exception as e:
    raise e


STAGE_NAME="Model Evalution stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evalution=ModelEvalutionPipeline()
    model_evalution.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\n x================x")
except Exception as e:
    raise e