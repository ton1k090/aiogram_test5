import asyncio

async def send_hello(): # корутина
    await asyncio.sleep(2)
    print('hello')


async def send_bye():
    await asyncio.sleep(1)
    print('bye')


async def main():
    task = asyncio.create_task(send_hello()) # для исполнения кода конкурентно
    task2 = asyncio.create_task(send_bye()) # для исполнения кода конкурентно

    await task
    await task2

asyncio.run(main()) # задачи выведуться асинхронно в оотв с условием
