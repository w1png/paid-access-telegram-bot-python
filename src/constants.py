import dotenv
import os
import importlib

dotenv.load_dotenv(dotenv.find_dotenv())
TOKEN = os.getenv("TOKEN")

DATETIME_FORMAT = "%H:%M:%S %Y-%m-%d"
