#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

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
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ return dict with data """
        indexed_data = self.indexed_dataset()
        assert (isinstance(index, int)
                and index >= 0
                and index is not None
                and index <= max(indexed_data.keys()))
        page_data = []
        i = 0
        for key, value in indexed_data.items():
            if i == page_size:
                break
            if key >= index:
                page_data.append(value)
                i += 1
        my_dict = {}
        my_dict['index'] = index
        my_dict['next_index'] = index + page_size
        my_dict['page_size'] = len(page_data)
        my_dict['data'] = page_data
        return my_dict
