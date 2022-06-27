#!/usr/bin/env python3
""" Takes integer argument, wait for random delay """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for random delay between 0 and max_delay, returns that """
    rand: float = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
