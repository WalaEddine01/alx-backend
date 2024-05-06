#!/usr/bin/env python3
"""
This mudule contains the This is the index_range method
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    This is the index_range method
    """
    first_index = 0
    last_index = page * page_size
    if page:
        first_index = (page - 1) * page_size
    else:
        first_index = page_size * page
    return (first_index, last_index)
