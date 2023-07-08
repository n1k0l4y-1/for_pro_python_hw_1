import asyncio


async def get_employees():
    while True:
        print('get_employees')
        await asyncio.sleep(2)