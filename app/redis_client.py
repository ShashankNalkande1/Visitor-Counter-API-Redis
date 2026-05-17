import redis
from .config import os

class RedisClient:
    _client = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            try:
                redis_url = os.getenv("REDIS_URL")
                cls._client = redis.StrictRedis.from_url(redis_url, decode_responses=True)
            except Exception as e:
                raise ConnectionError(f"Failed to initialize Redis client. Error: {e}")
        return cls._client

    @classmethod
    async def close(cls):
        if cls._client:
            cls._client.close()
            cls._client = None

# Convenience function
def get_redis():
    return RedisClient.get_client()