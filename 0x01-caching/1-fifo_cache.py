#!/usr/bin/env python3
"""
Module for BaseCaching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Represents  FIFOCache which is an object that allows storing and
    retrieving items from a dictionary with a FIFO
    removal mechanism when the limit is reached
    """
    def __init__(self):
        """
        Initializes the cache class with the parents init method.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Caches a key value paid and Adds an item in the cache.
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item by key
        """
        return self.cache_data.get(key, None)
