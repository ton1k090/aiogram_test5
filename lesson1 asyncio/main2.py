import asyncio


async def send_time(second: int):
    await asyncio.sleep(second)
    print(f'passed {second} seconds')


# print(send_time(2), send_time(5), sep='\n') # разные объекты корутины

async def main():
    task = asyncio.create_task(send_time(2)) # разные объекты корутины
    task2 = asyncio.create_task(send_time(5)) # разные объекты корутины

    await task
    await task2


if __name__ == '__main__':
    asyncio.run(main())