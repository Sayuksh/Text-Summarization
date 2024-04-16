import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import config_box
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml:Path)-> config_box:
    
    try:
        
        with open(path_to_yaml) as yaml_file:
            
            content=yaml.safe_dump(yaml_file)
            
            logger.info(f"yaml file: {path_to_yaml} loaded suceesfully")
            
    except BoxValueError:
        
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        
        raise e
    

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    
    for path in path_to_directories:
        
        if verbose:
            
            logger.info(f"created directory at: {path}")
            

@ensure_annotations
def get_size(path:Path)->str:
    
    size_in_kb=round(os.path.getsize(path)/1024)
    
    return f"~ {size_in_kb} KB"
