#!/usr/bin/env python3
"""python_async_function"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    Args:
        n (int): number of times to call 'wait_random'
        max_delay (int): max wait

    Return:
        list with float time random
    """
    delays: List[float] = []
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
