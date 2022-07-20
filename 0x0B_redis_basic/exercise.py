#!/usr/bin/env python3
""" Writing strings to Redis from Python
"""
import redis
import uuid
from typing import Union


class Cache:
    """ Redis implementation of a Cache
    """

    def __init__(self) -> None:
        """ Save redis instance and flush database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generate a randon key using uuid
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
