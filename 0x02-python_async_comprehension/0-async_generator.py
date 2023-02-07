#!/usr/bin/env python3
'''
Module for 0x02. Python - Async Comprehension
'''

from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """Async Generator a coroutine"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
