from me_pack.application.salary import *
from me_pack.application.db.people import *


async def dirty_main():
    task_1 = asyncio.create_task(calculate_salary())
    task_2 = asyncio.create_task(get_employees())

    await asyncio.gather(task_1, task_2)

asyncio.run(dirty_main())