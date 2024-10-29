#!/usr/bin/env python3
"""
Module to Implement a get_hyper method that takes
the same arguments (and defaults) as get_page and returns
a dictionary containing the following key-value pairs:
"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    Args: page(int): page number to return
        : page_size (int) number of itenms on a page

    Return: tuple (start_index, end_index)
    """
    begin, end = 0, 0
    for a in range(page):
        begin = end
        end += page_size
    return (begin, end)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Takes 2 integer arguments and returns requested page from the dataset
        Args: page (int): required page number. must be a positive integer
        page_size (int): number of records per page. must be a +ve integer
        Return: list of lists containing required data from the dataset
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

        def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
            """
            Returns a page of the dataset.
            Args: page (int): The page number.
            page_size (int): The page size.
            Returns: List[List]: The page of the dataset.
            """
        total_pages = len(self.dataset()) // page_size + 1
        data_set = self.get_page(page, page_size)
        page_info = {
            "page": page,
            "page_size": page_size if page_size <= len(data_set)
            else len(data_set),
            "total_pages": total_pages,
            "data": data_set,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page + 1 <= total_pages else None
        }
        return page_info
