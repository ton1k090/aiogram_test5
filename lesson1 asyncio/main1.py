import asyncio

'''выводить счетчик секунд в первой функции каждую секунду кроме третей
во второй функции просто каждую третью секунду'''

async def send_one():
    '''выводит каждую секунду кроме 3'''
    n = 0
    while True:
        await asyncio.sleep(1)
        n += 1
        print(f'passed {n} seconds' if n % 3 != 0 else '---' )


async def send_three():
    '''выводит каждую 3 секунду'''
    n = 0
    while True:
        await asyncio.sleep(3)
        n += 3
        print(f'passed still {n} seconds')


async def main():# corutine
    task = asyncio.create_task(send_one())
    task2 = asyncio.create_task(send_three())

    await task
    await task2

if __name__ == '__main__':
    asyncio.run(main()) # object corutine