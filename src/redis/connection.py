import redis.asyncio as redis

from src.common.settings import settings

# redis connection
redis_client = redis.from_url(
   url=str(settings.redis_url),
   decode_responses=True,
)