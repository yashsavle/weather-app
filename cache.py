import redis
from config import Config
import logging
from typing import Optional

logger = logging.getLogger(__name__)

redis_client = redis.Redis(
    host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB
)

def get_cached_data(key: str) -> Optional[str]:
    try:
        data = redis_client.get(key)
        if data:
            logger.info(f"Cache hit for key: {key}")
        else:
            logger.info(f"Cache miss for key: {key}")
        return data.decode("utf-8") if data else None
    except redis.RedisError as e:
        logger.error(f"Error accessing Redis: {str(e)}")
        return None

def set_cached_data(key: str, value: str, expiration: int) -> None:
    try:
        redis_client.set(key, value, ex=expiration)
    except redis.RedisError as e:
        logger.error(f"Error setting cache in Redis: {str(e)}")
