#!/usr/bin/env python3
"""takes in a function and return a function"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes in a function and return a function"""
    def multiply(n: float) -> float:
        return float(n * multiplier)
    return multiply