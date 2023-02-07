#!/usr/bin/env python3
'''
Module for 0x02. Python - Async Comprehension
'''

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Run time for four parallel comprehensions """
    start = time()
    tasks = [async_comprehension() for _ in range(4)]
    await gather(*tasks)
    end = time()
    return (end - start)
