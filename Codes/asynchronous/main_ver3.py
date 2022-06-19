import asyncio
import time

async def async_sleep(n):
    print("Before sleep", n)
    await asyncio.sleep(n)
    print("After sleep", n)

async def print_hello():
    print("hello")

async def main():
    start_time = time.time()
    try:
        # await asyncio.gather(async_sleep(1), async_sleep(2), print_hello())  
        await asyncio.gather(asyncio.wait_for(async_sleep(30), 5), async_sleep(1), print_hello())  #! use wait for to make sure it won't block for a long time
    except asyncio.TimeoutError:
        print("Encountered timeout error")
    print("total time ", time.time() - start_time)


asyncio.run(main())   