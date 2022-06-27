#!/usr/bin/env python3
""" Takes 2 arguments n and max_delay and returns total_time / n """

import random
import time
import asyncio
from_task_1 = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int = 10) -> float:
    """ Returns the average time taken to complete the task """
    time_before = time.perf_counter()
    asyncio.run(from_task_1(n, max_delay))
    time_elased = time.perf_counter() - time_before
    
    return time_elased / n