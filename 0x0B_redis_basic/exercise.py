#!/usr/bin/env python3
""" Writing strings to Redis from Python
"""
from curses import keyname
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ System to count how many times methods are called
    """
    key = method.__qualname__

    @wraps(method)
    def counter(self, *args, **kwargs):
        """ Increment cache counter
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    
    return counter

def call_history(method: Callable) -> Callable:
    """ Store the history of inputs and outputs
        for a particular function.
    """

    @wraps(method)
    def history(self, *args, **kwargs):
        """ append inputs arguments to history 
        """
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        output = method(self, *args, **kwargs)
        self._redis.rpush(input_key, str(args))
        self._redis.rpush(output_key, str(output))

        return output
    return history


class Cache:
    """ Redis implementation of a Cache
    """

    def __init__(self) -> None:
        """ Save redis instance and flush database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generate a randon key using uuid
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """ Convert the data back to the desired format
        """
        data = self._redis.get(key)

        if fn:
            fn(data)
        return data

    def get_str(self):
        """ Parametrize Cache.get with the correct conversion function
        """

    def get_int(self):
        """ Parametrize Cache.get with the correct conversion function
        """
