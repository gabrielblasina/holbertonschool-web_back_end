#!/usr/bin/env python3
"""Module Variable_anotations"""
from typing import Iterable
from typing import Sequence
from typing import List
from typing import Tuple


def element_length(lst: Iterable[Sequence])\
        -> List[Tuple[Sequence, int]]:
    """
    Args:
        lst: list.
    Returns:
        list of tuples.
    """

    return [(i, len(i)) for i in lst]
