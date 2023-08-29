#!/usr/bin/env python3
"""asynchronous coroutine"""
from typing import List
import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """return the list of all the delays (float) in ascending order"""
    lst = []
    for _ in range(n):
        lst.append(await wait_random(max_delay))
    return sorted(lst)
