import dotenv
import os
import importlib
from utils import config

dotenv.load_dotenv(dotenv.find_dotenv())
TOKEN = os.getenv("TOKEN")

DATETIME_FORMAT = "%H:%M:%S %Y-%m-%d"
language = importlib.import_module(f"language.{config['language']}")
