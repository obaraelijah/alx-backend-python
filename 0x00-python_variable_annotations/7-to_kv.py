#!/usr/bin/env python3
"""return a tuple"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return a tuple"""
    return (str(k), float(v**2))