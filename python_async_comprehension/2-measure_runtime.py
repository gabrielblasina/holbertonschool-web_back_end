#!/usr/bin/env python3
"""python_async_comprehension"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure time and execute in paralallel
    Args:
        void
    Return:
        float random numbers
    """
    first_time = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    elapsed = time.perf_counter()
    return (elapsed - first_time)
