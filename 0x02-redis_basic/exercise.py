#!/usr/bin/env python3
"""
Working with redis
"""
import redis


class Cache:
    """
    defines methods to work with the redis client
    """
    def __init__(self) -> None:
        """
        initialize the redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
