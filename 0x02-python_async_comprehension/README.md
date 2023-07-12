# Asynchronous Generator and Comprehensions

This repository contains Python scripts that demonstrate the concepts of asynchronous generator and comprehensions. Each script corresponds to a specific task and is described below.

## Files

### 0-async_generator.py
This script defines a coroutine called `async_generator`. The coroutine loops 10 times, asynchronously waits for 1 second on each iteration, and then yields a random number between 0 and 10. The `random` module is used to generate random numbers. This script can be executed using the provided `0-main.py` script.

### 1-async_comprehension.py
This script imports the `async_generator` coroutine from the previous task (`0-async_generator.py`). It defines another coroutine called `async_comprehension`, which collects 10 random numbers using an asynchronous comprehension over `async_generator`. It returns the list of 10 random numbers. To execute this script, you can use the `1-main.py` script.

### 2-measure_runtime.py
The `2-measure_runtime.py` script imports the `async_comprehension` coroutine from the previous file (`1-async_comprehension.py`). It defines a coroutine called `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather`. The `measure_runtime` coroutine measures the total runtime of executing the four parallel comprehensions and returns it. When you run this script using `2-main.py`, it will output the total runtime, which should be approximately 10 seconds.

