# Python Async Function

This repository contains Python code for implementing asynchronous programming using `async` and `await` syntax, as well as the `asyncio` library. The code includes examples and functions that demonstrate various concepts of asynchronous programming in Python.

## Contents

The repository contains the following files:

- `0-basic_async_syntax.py`: An asynchronous coroutine that introduces the basics of `async` and `await` syntax. It waits for a random delay between 0 and a given maximum delay.
- `1-concurrent_coroutines.py`: Demonstrates how to execute multiple coroutines concurrently using `asyncio`. It spawns `n` coroutines that wait for a random delay.
- `2-measure_runtime.py`: Measures the total execution time for executing `wait_n(n, max_delay)` from the previous file and calculates the average runtime per coroutine.
- `3-tasks.py`: Provides a function that returns an `asyncio.Task` object to execute a coroutine.
- `4-tasks.py`: Contains a modified version of the `wait_n` function from the previous file that uses `task_wait_random` to create and execute tasks.