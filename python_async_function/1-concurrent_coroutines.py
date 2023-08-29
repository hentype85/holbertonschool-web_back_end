#!/usr/bin/env python3
"""asynchronous coroutine"""
from typing import List
import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays in ascending order"""
    tasks_lst = []
    completed_lst = []

    for _ in range(n):
        tasks_lst.append(wait_random(max_delay))

    for task in tasks_lst:
        completed_lst.append(await task)

    return sorted(completed_lst)
