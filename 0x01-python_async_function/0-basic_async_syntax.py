#!/usr/bin/env python3
"""Basic async function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random number of seconds multiplied by numbers between 0-10 and returns float"""
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
