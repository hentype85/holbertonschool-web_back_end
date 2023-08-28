#!/usr/bin/env python3
"""type-annotated function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a list of integers,floats and returns their sum as float"""
    return sum(mxd_lst)
