#!/usr/bin/env python3
'''
Module for 0x01. Python - Async
'''

import random
import asyncio


async def wait_random(max_delay: float = 10) -> float:
    '''Function that waits for a random delay'''
    randomVar = random.uniform(0, max_delay)
    await asyncio.sleep(randomVar)
    return randomVar
