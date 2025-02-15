import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    STRACT_API_TOKEN = os.getenv('STRACT_API_TOKEN')
    BASE_URL = os.getenv('BASE_URL')
