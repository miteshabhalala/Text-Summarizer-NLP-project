from src.TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from src.TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.TextSummarizer.logging import logger

STAGE_NAME = " Data Ingestion stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = " Data validation stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e