#!/usr/bin/env python3
""" Create index_range function """
import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """ return the first index of the page and the last """
    start = (page - 1) * page_size
    return (start, start + page_size)
