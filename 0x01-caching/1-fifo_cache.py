#!/usr/bin/python3
"""
This module contains the FIFOCache class
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    This is the FIFOCache class
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()

    def put(self, key, item):
        """
        the put method
        """
        if key is not None and item is not None and key not in self.cache_data:
            if len(self.cache_data) > self.MAX_ITEMS - 1:
                key_Dis = next(iter(self.cache_data.keys()))
                self.cache_data.pop(key_Dis)
                print("DISCARD: {}".format(key_Dis))
            self.cache_data[key] = item

    def get(self, key):
        """
        the get method
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
