#!/usr/bin/env python3
""" Run time calculator for the parallel comprehensions """

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Returns runtime """
    initial_time = time.perf_counter()
    for counter in range(4):
        await asyncio.gather(async_comprehension())
    time_elapsed = time.perf_counter()
    return time_elapsed - initial_time
