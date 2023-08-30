#!/usr/bin/env python3
"""Module Variable_anotations"""
from typing import List
from typing import Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Args:
        mxd_list (list[Union[int, float]]): only paramether.
    Returns:
        sum of floats and integers in mxd_list.
    """

    sum: float = 0.0
    for num in mxd_lst:
        sum += num
    return sum
