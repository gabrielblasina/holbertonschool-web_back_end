#!/usr/bin/env python3
"""Module Variable_anotations"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Args:
        sum_list (list[float]): only paramether.
    Returns:
        sum of float in sum_list.
    """

    sum: float = 0.0
    for num in input_list:
        sum += num
    return sum
