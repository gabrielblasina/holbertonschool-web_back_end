#!/usr/bin/env python3
"""Module Variable_anotations"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Args:
        multiplier (float): number to multipli.
    Returns:
        Function that multiplies a float.
    """

    def mult_factor(factor: float) -> float:
        """Function to multipli"""
        return float(factor * multiplier)

    return mult_factor
