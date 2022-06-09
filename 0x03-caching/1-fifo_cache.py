#!/usr/bin/env python3
""" Create a class FIFOCache that inherits from
    BaseCaching and is a caching system:

    You must use self.cache_data
        - dictionary from the parent class BaseCaching
    You can overload def __init__(self): but don’t
    forget to call the parent init: super().__init__()

    def put(self, key, item):
    Must assign to the dictionary self.cache_data
    the item value for the key key.
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data
    is higher that BaseCaching.MAX_ITEMS:
    you must discard the first item put in cache (FIFO algorithm)
    you must print DISCARD: with the key
    discarded and following by a new line

    def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesn’t exist
    in self.cache_data, return None.
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Cache System """
    def __init__(self) -> None:
        """ Constructor and init super """
        super().__init__()

    def put(self, key, item) -> None:
        """ Must assign to cache_data the item value for key"""
        if key and item:
            if (len(self.cache_data.keys()) == self.MAX_ITEMS):
                k = list(self.cache_data.keys())[0]
                del self.cache_data[k]
                print("DISCARD: {}".format(k))
            self.cache_data.update({key: item})

    def get(self, key):
        """ Must return the value in self.cache_data linked to key """
        if key:
            try:
                return self.cache_data.get(key)
            except KeyError:
                return None
        return None
