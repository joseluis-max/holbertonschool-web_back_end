#!/usr/bin/env python3
""" Augment the following code with the correct duck-typed annotations:
"""


from typing import Sequence, Union, Any, Type


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, Type[None]]:
    if lst:
        return lst[0]
    else:
        return None
