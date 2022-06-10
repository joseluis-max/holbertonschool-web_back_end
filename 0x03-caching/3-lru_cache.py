#!/usr/bin/env python3
""" Create a class LRUCache """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache System """
    cache_copy = {}
    insert = 0
    LRU = 0

    def __init__(self) -> None:
        """ Call super and init super """
        super().__init__()

    def put(self, key, item):
        """ Must assign to the dictionary the item value for the key"""
        if key and item:
            if key in list(self.cache_data.keys()):
                self.cache_data.update({key: item})
                self.LRU = self.cache_copy.get(key)[1] + 1
                self.cache_copy.update({key: [item, self.insert]})
                self.insert += 1
            else:
                if len(self.cache_data.keys()) == self.MAX_ITEMS:
                    for k, v in self.cache_copy.items():
                        if v[1] == self.LRU:
                            print("DISCARD: {}".format(k))
                            del self.cache_data[k]
                            del self.cache_copy[k]
                            self.LRU += 1
                            break
                self.cache_copy[key] = [item, self.insert]
                self.cache_data[key] = item
                self.insert += 1

    def get(self, key):
        """ Must return the value in self.cache_data linked to key """
        if key:
            try:
                return self.cache_data.get(key)
            except KeyError:
                return None
        return None
