#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ if between two queries, certain rows are removed from the dataset,
            the user does not miss items from dataset when changing page"""

        # ensure index is int
        assert isinstance(index, int)
        # ensure index on the valid limits
        assert 0 <= index < len(self.indexed_dataset())

        # list of data elements in the actual page
        lst_data = []
        for v in range(index, index + page_size):
            element = self.indexed_dataset().get(v)
            if element:
                lst_data.append(element)

        # calculate next index page
        next_index = index + page_size

        # dict with info about the requested page and its data
        dic_response = {
            "index": index,
            "page_size": page_size,
            "next_index": next_index,
            "data": lst_data
            }

        # return data as a dictionary
        return dic_response
