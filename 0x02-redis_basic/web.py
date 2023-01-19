#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""

import redis
import requests

redis_client = redis.Redis()
count = 0


def get_page(url: str) -> str:
    """
    get page and cache value
    Args::
        url(str)
    """
    redis_client.set(f"cached: {url}", count)
    response = requests.get(url)
    redis_client.incr(f"count:{url}")
    redis_client.setex(
            f"cached: {url}", 10, redis_client.get(f"cached: {url}"))
    return response.text


if __name__ == "__main__":
    get_page(" http://slowwly.robertomurray.co.uk")
