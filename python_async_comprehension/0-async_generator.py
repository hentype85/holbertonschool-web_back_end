#!/usr/bin/env python3
"""coroutine"""
import asyncio
import random


async def async_generator():
    """asynchronous coroutine that generates random float numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
