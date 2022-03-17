from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

# Salesforce 
PATH_RESOURCE_FILE = os.getenv('PATH_RESOURCE_FILE')