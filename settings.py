import os
import config
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = config.config.REDIS_URL
QUEUES = ["emails", "default"]
