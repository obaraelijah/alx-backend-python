#!/usr/bin/env python3
"""sum of mixed types of floats and ints"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """sum of mixed types of floats and ints"""
    return float(sum(mxd_lst))
