from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Pipeline"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} start <<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} complete <<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e