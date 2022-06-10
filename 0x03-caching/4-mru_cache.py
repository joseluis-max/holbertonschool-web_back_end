#!/usr/bin/env python3
""" MRUCache is a caching system """
from re import S


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRU Caching system """
    cache_copy = {}
    MRU = 1
    insert = 0

    def __init__(self) -> None:
        """ Call super and init super """
        super().__init__()

    def put(self, key, item):
        """ Must assign to the dictionary the item value for the key"""
        if key and item:
            if key in list(self.cache_data.keys()):
                self.cache_data.update({key: item})
                self.cache_copy.update({key: [item, self.insert]})
                self.MRU = self.insert
                self.insert += 1
            else:
                if len(self.cache_data.keys()) == self.MAX_ITEMS:
                    for k, v in self.cache_copy.items():
                        if v[1] == self.MRU:
                            print("DISCARD: {}".format(k))
                            del self.cache_data[k]
                            del self.cache_copy[k]
                            self.MRU += 1
                            break
                self.cache_copy[key] = [item, self.insert]
                self.cache_data[key] = item
                if self.insert <= 4:
                    self.MRU = 1
                else:
                    self.MRU = self.insert
                self.insert += 1

    def get(self, key):
        """ Must return the value in self.cache_data linked to key """
        if key:
            try:
                return self.cache_data.get(key)
            except KeyError:
                return None
        return None
