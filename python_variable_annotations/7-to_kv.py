#!/usr/bin/env python3
"""Module Variable_anotations"""
from typing import Tuple
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
        k (str): string.
        v (Union[int,float]): int or float value.
    Returns:
        Tuple of str and square of int or flote.
    """

    squared_value: float = v ** 2
    return k, squared_value
