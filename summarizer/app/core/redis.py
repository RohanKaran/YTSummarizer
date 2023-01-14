import aioredis

from app.core import config

redis = aioredis.from_url(
    "redis://" + config.REDIS_HOST,
    password=config.REDIS_PASSWORD,
    decode_responses=True,
)
