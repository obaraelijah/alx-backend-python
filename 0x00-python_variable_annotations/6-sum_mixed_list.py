#!/usr/bin/env python3
"""mixed types"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """int and float to float"""
    return float(sum(mxd_lst))