#!/usr/bin/env python3
"""This module contains the Cache class
"""

import redis
import requests
from typing import Callable
from functools import wraps


_redis = redis.Redis()


def call_history(method: Callable) -> Callable:
    """stores the history of inputs and outputs for a particular function
    """
    @wraps(method)
    def save_cache(*args, **kwargs):
        """saves the input and output of each function in redis
        """
        key = ":count:{}".format(*args)

        _redis.incr(key)
        cache = _redis.get(*args)
        if cache:
            return cache.decode('utf-8')

        html = method(*args, **kwargs)

        _redis.setex(*args, 10, html)

        return html

    return save_cache


@call_history
def get_page(url: str) -> str:
    """gets the url content of a page
    """
    x = requests.get(url)

    return x.text
