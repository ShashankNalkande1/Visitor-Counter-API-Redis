from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Redis Configuration
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))

class Settings:
    REDIS_URL: str = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
    LIKES_KEY: str = "instagram:likes"
    # Optional: Redis connection pool settings
    REDIS_MAX_CONNECTIONS: int = 10

settings = Settings()