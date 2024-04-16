from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger


class DataValidationPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()

        data_validation_config=config.get_data_validation_config()

        data_validation=DataValidation(config=data_validation_config)

        data_validation.validation_all_files_exist()
