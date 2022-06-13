#!/usr/bin/env python3
""" Create a class BasicCache and is a caching system:
    - This caching system doesn’t have limit
    - def put(self, key, item):
        - Must assign to the dictionary the item value for the key.
        - If key or item is None, this method should not do anything.
    - If key or item is None, this method should not do anything.
        - Must return the value linked to key.
        - If key is None or if the key doesn’t exist return None.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Caching System """
    def __init__(self) -> None:
        """ Constructor and init super """
        super().__init__()

    def put(self, key, item):
        """ Must assign to the dictionary self.cache_data
            the item value for the key
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key:
            try:
                return self.cache_data.get(key)
            except KeyError:
                return None
        return None
