#!/usr/bin/env python3
""" Take the code from wait_n and alter it into task_wait_n """

from typing import List
import asyncio
import random
task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ Waits for ran delay until max_delay, returns list of actual delays """
    spawn_list = []
    delay_list = []
    for i in range(n):
        delayed_task = asyncio.create_task(task_wait_random(max_delay))
        delayed_task.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(delayed_task)

    for spawn in spawn_list:
        await spawn

    return delay_list
