#!/usr/bin/env python3
""" Given the parameters and the return values,
    add type annotations to the function
"""


from typing import Union, Mapping, Any, TypeVar, Type


T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, Type[None]] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
