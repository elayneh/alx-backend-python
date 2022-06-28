#!/usr/bin/env python3
""" Async Comprehension """

import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Returns random numbers """
    collectoin = [counter async for counter in async_generator()]
    return collectoin
