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
    # await asyncio.gather(async_sleep(1), async_sleep(2), print_hello())  # ! not await in print, it can just print, but for the sleep it needs to sleep
    await asyncio.gather(async_sleep(2), async_sleep(1), print_hello()) # ! once we hit the await, we can give back the control, so another code rountine can continue
    print("total time ", time.time() - start_time)


asyncio.run(main())   