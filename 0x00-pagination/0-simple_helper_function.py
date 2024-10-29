#!/usr/bin/env python3
"""
Module for a function named index_range that takes
two integer arguments page and page_size
"""
from typing import Tuple


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
