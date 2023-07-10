#!/usr/bin/env python3
"""This module implements a function that accepts a
a list of floats and returns their sum as a float
"""
from typing import List



def sum_list(input_list: List[float]) -> float:
    """Calculates the sum of floats in a list"""
    return float(sum(input_list))