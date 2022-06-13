#!/usr/bin/env python3
""" Write a function named index_range that takes
    two integer arguments page and page_size.
    - The function should return a tuple of size two
    containing a start index and an end index corresponding
    to the range of indexes to return in a list for those
    particular pagination parameters.
    - Page numbers are 1-indexed, i.e. the first page is page 1.
"""
from typing import Tuple


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
