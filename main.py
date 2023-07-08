import asyncio

from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date


async def date_today():
    while True:
        print(date.today())
        await asyncio.sleep(10)


if __name__ == '__main__':

    async def main():
        task_1 = asyncio.create_task(calculate_salary())
        task_2 = asyncio.create_task(get_employees())
        task_3 = asyncio.create_task(date_today())

        await asyncio.gather(task_1, task_2, task_3)

    asyncio.run(main())