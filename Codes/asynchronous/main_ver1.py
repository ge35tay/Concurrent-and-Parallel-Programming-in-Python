import asyncio
import time

async def async_sleep(n):
    print("Before sleep", n)
    await asyncio.sleep(5)
    print("After sleep", n)

async def print_hello():
    print("hello")

async def main():
    start_time = time.time()
    task = asyncio.create_task(async_sleep(1))  # use task to run a synchronous async_sleep function 
    await async_sleep(2)
    # await task
    await print_hello()
    await task
    print("total time ", time.time() - start_time)


asyncio.run(main())   