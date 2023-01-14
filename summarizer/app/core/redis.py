import aioredis

from app.core import config

redis = aioredis.from_url(config.REDIS_URL, decode_responses=True)
