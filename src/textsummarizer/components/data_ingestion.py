import os
from pathlib import Path
import urllib.request as requests
import zipfile
from src.textSummarizer.logging import logger
from src.textSummarizer.utils.common import get_size
from textSummarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config
        
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,header=requests.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{header}")
        else:
            logger.info(f"File is already exists of size: {get_size(Path(self.config.local_data_file))}")
    
    
    
    def extract_zipfile(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            
               