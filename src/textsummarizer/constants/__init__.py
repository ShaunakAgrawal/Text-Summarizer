# we want to return config.yaml and param.yaml 
# instead of hard coding this we pass it as a constant 

from pathlib import Path 

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path ("params.yaml")
