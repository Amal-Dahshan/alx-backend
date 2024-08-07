#!/usr/bin/env python3
""" Create index_range function """
from typing import Tuple, Dict
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return the first index of the page and the last """
    start = (page - 1) * page_size
    return (start, start + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get the data in the page """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        tu = index_range(page, page_size)
        if tu[0] > len(self.dataset()):
            return []
        return self.dataset()[tu[0]: tu[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ return dict with all data about pages """
        my_dict = {}
        my_dict['page_size'] = page_size
        my_dict['page'] = page
        my_dict['data'] = self.get_page(page, page_size)
        page_data = self.get_page(page + 1, page_size)
