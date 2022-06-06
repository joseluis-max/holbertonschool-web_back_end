#!/usr/bin/env python3
""" Write a type-annotated function sum_mixed_list which
    takes a list mxd_lst of integers and floats and returns
    their sum as a float.
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Sum every item in a list """
    return sum(mxd_lst)
