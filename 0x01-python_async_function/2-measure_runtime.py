#!/usr/bin/env python3
"""  Measure the runtime
"""

import asyncio
import random
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measure runtime."""
    start_time = perf_counter()
    await wait_n(n, max_delay)
    elapsed = perf_counter() - start_time
    return elapsed

