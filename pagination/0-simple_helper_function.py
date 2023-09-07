#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page, page_size):
    """ return a tuple of two containing a start index
        and end index for pagination"""
    end_index = page * page_size
    start_index = end_index - page_size

    return (start_index, end_index)
