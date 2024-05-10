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
        if key is not None and item is not None:
            self.cache_data[key] = item
        elif len(self.cache_data) > self.MAX_ITEMS:
            self.cache_data[0]
