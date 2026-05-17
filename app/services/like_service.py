from ..redis_client import RedisClient
from ..config import settings

class LikeService:
    LIKES_KEY = "likes"

    @classmethod
    def ensure_key_exists(cls):
        """Initialise key with 0 if not present (idempotent)."""
        try:
            redis = RedisClient.get_client()
            if not redis.exists(cls.LIKES_KEY):
                redis.set(cls.LIKES_KEY, 0)
        except Exception as e:
            raise ConnectionError(f"Failed to connect to Redis. Error: {e}")

    @staticmethod
    def get_likes() -> int:
        """Retrieve current like count from Redis."""
        redis = RedisClient.get_client()
        count = redis.get(settings.LIKES_KEY)
        return int(count) if count is not None else 0

    @staticmethod
    def increment_likes() -> int:
        """
        Atomically increment like count using Redis INCR.
        Returns the new count.
        """
        redis = RedisClient.get_client()
        new_count = redis.incr(settings.LIKES_KEY)
        return new_count