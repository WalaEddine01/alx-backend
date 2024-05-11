#!/usr/bin/python3
"""
This module contains the MRUCache class
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    This is the MRUCache class
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        the put method
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    key_Dis = list(self.cache_data.keys())[0]
                    self.cache_data.pop(key_Dis)
                    print("DISCARD: {}".format(key_Dis))
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """
        the get method
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key, last=False)
        return self.cache_data[key]
