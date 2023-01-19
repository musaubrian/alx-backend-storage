#!/usr/bin/env python3
"""
Module contains class definition of a redis client
"""
from typing import Callable, Optional, Union
import redis


class Cache:
    """
    defines methods to work with the redis client
    """
    def __init__(self) -> None:
        """
        initialize the redis client
        Attributes::
            self._redis(redis.Redis): redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def get(self, key: str, func: Optional[Callable] = None) -> \
            Union[str, bytes, int, float, None]:
        """
        Return data from a redis Cache
        Args::
            key(str)
            func(Optional[callable])
        """
        data = self._redis.get(key)
        if data is not None and func is not None and callable(func):
            return func(data)
        return data
