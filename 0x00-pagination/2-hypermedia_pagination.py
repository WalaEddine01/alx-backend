#!/usr/bin/env python3
"""
This mudule contains the This is the index_range method
"""
from typing import Dict
import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Constructor
        """
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        This is the get hyper method
        """
        data = self.get_page(page, page_size)
        next_page = page + 1
        total_pages = math.ceil(len(self.dataset()) / page_size)
        if len(data) == 0 or page == total_pages:
            next_page = None
        if len(data) == 0 or page == 1:
            prev_page = None
        else:
            prev_page = page - 1
        dict_pageInfo = {'page_size': len(data),
                         'page': page,
                         'data': data,
                         'next_page': next_page,
                         'prev_page': prev_page,
                         'total_pages': total_pages}
        return dict_pageInfo
