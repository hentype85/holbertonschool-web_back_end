#!/usr/bin/env python3
"""asynchronous coroutine"""
from asyncio import sleep
from random import uniform


async def wait_random(max_delay: int=10) -> float:
    """asynchronous coroutine that waits for a random delay and returns it"""
    delay = uniform(0, max_delay)
    await sleep(delay)
    return delay
