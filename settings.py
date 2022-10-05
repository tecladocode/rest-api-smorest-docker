import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("RENDER_REDIS_URL", "redis://localhost:6379")
QUEUES = ["emails", "default"]
