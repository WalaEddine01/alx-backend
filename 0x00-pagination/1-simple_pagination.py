#!/usr/bin/env python3
"""
This mudule contains the This is the index_range method
"""
from typing import Tuple
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        This is the get page tha returns the list of data set
        of the given indexes
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        list_data_set = []
        if page * page_size > len(self.dataset()):
            return []
        indexs = index_range(page, page_size)
        for i in self.dataset()[indexs[0]:indexs[1]]:
            list_data_set.append(i)
        return list_data_set
