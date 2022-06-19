import asyncio


async def async_sleep():
    print("Before sleep")
    await asyncio.sleep(5)
    print("After sleep")

async def print_hello():
    print("hello")

async def main():
    await async_sleep()  # nothign can do until i get this, stop the function before it going down to next function, we can not skip it
    await print_hello()  # execute sequentially
    result = await print_hello()
    print(result)

asyncio.run(main())   