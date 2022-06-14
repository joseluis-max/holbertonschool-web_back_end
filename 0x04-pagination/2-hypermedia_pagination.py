#!/usr/bin/env python3
""" Replicate code from the previous task.

    Implement a get_hyper method that takes the
    same arguments (and defaults) as get_page and
    returns a dictionary containing the following key-value pairs:
        - page_size: the length of the returned dataset page
        - page: the current page number
        - data: the dataset page (equivalent to return from previous task)
        - next_page: number of the next page, None if no next page
        - prev_page: number of the previous page, None if no previous page
        - total_pages: the total number of pages in the dataset as an integer
        - Make sure to reuse get_page in your implementation.

    You can use the math module if necessary.
"""
import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int]:
    """ Index_range

        Arguments:
        ---------
            `page`: current page number
            `page_size`: items number in every page

        Return:
        -------
            list for those particular pagination parameters
    """
    start: int
    end: int

    if page == 1:
        start = 0
    else:
        start = (page - 1) * page_size

    end = page * page_size

    return (start, end)


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
        """ paginate the dataset correctly and
            return the appropriate page of the dataset
        """
        assert(type(page) == int)
        assert(type(page_size) == int)
        assert(page > 0)
        assert(page_size > 0)
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        return dataset[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """ returns a dictionary containing the following key-value pairs """
        data: List[Any] = self.get_page(page, page_size)
        total_pages: int = math.ceil(len(self.__dataset) / page_size)
        next_page: int = page + 1
        prev_page: int = page - 1
        if next_page > total_pages:
            next_page = None

        if prev_page <= 0:
            prev_page = None

        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
