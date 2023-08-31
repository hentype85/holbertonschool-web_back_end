#!/usr/bin/env python3
"""coroutine"""
import asyncio


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """collect 10 random numbers and return the 10 random numbers"""
    lst = []
    async for i in async_generator():
        lst.append(i)
    return lst
