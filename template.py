import os
from pathlib import Path 
import logging

logging .basicConfig(level=logging.INFO, format ='[%(asctime)s]:%(message)s:')

#structre implements from here we will create a src folder where it will have name etc
project_name ="textsummarizer"

list_files = [
    ".github/workflows/.gitkeep", #for deployment doesnt alow upload of empty folder 
    f"src/{project_name}/__init__.py", #instlls folder as local package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/loggging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__intit__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_files:
    filepath = Path(filepath)#detects the operating system and then based on that gives path 
    filedir,filename = os.path.split(filepath)#return file name and directory
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file :{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file:{filepath}")
    

    else:
        logging.info(f"{filename} already exists")



