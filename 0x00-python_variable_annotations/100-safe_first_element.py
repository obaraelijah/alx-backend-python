#!/usr/bin/env python3
"""augmenting code"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """if-else statements"""
    if lst:
        return lst[0]
    else:
        return None