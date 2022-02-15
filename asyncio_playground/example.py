import asyncio
import time
from typing import Callable

# async def f(x):
#     y = await z(x)  # OK - `await` and `return` allowed in coroutines
#     return y

# async def g(x):
#     yield x  # OK - this is an async generator

# async def m(x):
#     yield from gen(x)  # No - SyntaxError

# def m(x):
#     y = await z(x)  # Still no - SyntaxError (no `async def` here)
#     return y

async def print_time_elapsed(fn: Callable):
    s = time.perf_counter()
    result = asyncio.run(fn())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
    return result

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    asyncio.run(print_time_elapsed(main()))
    # s = time.perf_counter()
    # asyncio.run(main())
    # elapsed = time.perf_counter() - s
    # print(f"{__file__} executed in {elapsed:0.2f} seconds.")

# async def f():
#     await asyncio.sleep(1)
#     return "It worked. - called from f()"

# async def main():
#     result = await print_time_elapsed(f())
#     return result

# if __name__ == "__main__":
#     asyncio.run(main())


