#!/usr/bin/env python3
"""
BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Represents an object that allows storing and
    retrieving items from a dictionary
    """
    def put(self, key, item):
        """
        Module that adds an item in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def __init__(self):
        """
        Initialize the class using the parent class __init__ method
        """
        BaseCaching.__init__(self)

    def get(self, key):
        """
        Module to r eturn value linked to key.
        If key is None or doesn't exist, return None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
