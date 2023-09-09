#!/usr/bin/env python3
"""Hypermedia pagination"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """ return a tuple of two containing a start index
        and end index for pagination"""
    end_index = page * page_size
    start_index = end_index - page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the appropriate page of the dataset"""

        # ensure that page and page_size are integers and positive
        assert isinstance(page, int) and (page > 0)
        assert isinstance(page_size, int) and (page_size > 0)

        # get data from the .csv
        data = self.dataset()

        # get start and end index
        start_index, end_index = index_range(page, page_size)

        # return the appropiate page of the dataset
        if start_index < len(data):
            return data[start_index:end_index]
        else:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """returns a dictionary"""
        # ensure that page and page_size are integers and positive
        assert isinstance(page, int) and (page > 0)
        assert isinstance(page_size, int) and (page_size > 0)

        # get data from the .csv
        data = self.dataset()

        # get start and end index
        start_index, end_index = index_range(page, page_size)

        # calculate the total number of pages
        total_pages = math.ceil(len(data) / page_size)

        # determine the next and previous page numbers
        if end_index < len(data):
            next_page = page + 1
        else:
            next_page = None
        if start_index > 0:
            prev_page = page - 1
        else:
            prev_page = None

        # return appropiate page data as a dictionary
        dic_response = {
            "page_size": page_size,
            "page": page,
            "data": data[start_index:end_index],
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return dic_response
