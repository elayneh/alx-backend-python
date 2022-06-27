#!/usr/bin/env python3
""" Take an argument and return a task """
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """ Create and return a task """
    return asyncio.create_task(wait_random(max_delay))
