#!/usr/bin/env python3
""" Annotate the below function’s parameters
    and return values with the appropriate types"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a list that contains a tuple with sequence member and length"""
    lst = []
    for i in lst:
        lst.append(i, len(i))
    return lst
