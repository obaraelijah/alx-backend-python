#!/usr/bin/env python3
'''Async generator'''
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''creates a list of 10 numbers from a 10-number generator'''
    x = [number async for number in async_generator()]
    return x