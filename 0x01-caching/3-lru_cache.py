#!/usr/bin/python3
"""
This module contains the LRUCache class
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    This is the LRUCache class
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
                Key_Dis, _ = self.cache_data.popitem(True)
                print("DISCARD: {}".format(Key_Dis))
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """
        the get method
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
