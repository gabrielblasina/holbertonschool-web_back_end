#!/usr/bin/env python3
"""python_async_function"""
import asyncio
from time import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """
    Args:
        n (int): number of times to call 'wait_random'
        max_delay (int): max wait

    Return:
        measute time
    """
    start_time: float = time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time()
    return (end_time - start_time) / n
