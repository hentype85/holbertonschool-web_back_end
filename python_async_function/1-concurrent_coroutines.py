#!/usr/bin/env python3
"""asynchronous coroutine"""
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays in ascending order"""
    completed_task_lst = []

    for _ in range(n):
        task = await wait_random(max_delay)
        completed_task_lst.append(task)

    return sorted(completed_task_lst)
