import asyncio


async def calculate_salary():
    while True:
        print('calculate_salary')
        await asyncio.sleep(2)