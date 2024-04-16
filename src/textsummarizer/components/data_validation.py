import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config=config
        
    def validation_all_files_exist(self)->bool:
        try:
            valdiation_stauts=None
            all_file=os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))
            for file in all_file:
                if file not in self.config.ALL_REQUIRED_FILES:
                    valdiation_stauts=False
                    with open(self.config.STATUS_FILE,"w") as f:
                        f.write(f"Validation Status:{valdiation_stauts}")
                        
                else:
                    Validation_status=True
                    with open(self.config.STATUS_FILE,"w") as f:
                        f.write(f"Validation Status: {Validation_status}")
            return Validation_status
        except Exception as e:
            raise e