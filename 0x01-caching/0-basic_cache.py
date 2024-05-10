#!/usr/bin/python3
"""
This module contains the BasicCache class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    the BasicCache CLASS
    """
    def put(self, key, item):
        """
        the put method
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        the get method
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
