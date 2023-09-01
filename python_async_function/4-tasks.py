#!/usr/bin/env python3
"""python_async_function"""
import asyncio
import random
from typing import List


async def task_wait_random(max_delay: int = 10) -> float:
    """
    Args:
        max_delay (int): max wait

    Return:
        float time random
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    Args:
        n (int): number of times to call 'task_wait_random'
        max_delay (int): max wait

    Return:
        sorted result
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
