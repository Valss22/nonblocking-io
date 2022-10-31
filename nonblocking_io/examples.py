import asyncio
from eventloop import nonblocking


async def task_1(msg: str) -> None:
    await asyncio.sleep(2)
    print(msg)


async def task_2(msg: str) -> None:
    await asyncio.sleep(1)
    print(msg)


# @EventLoop()
# async def main():
#     loop = EventLoop()
#     loop.nonblocking(task_1, "task_1 is completed")
#     loop.nonblocking(task_2, "task_2 is completed")
#     print("main is completed")


@nonblocking
async def main():
    print("main is completed")


# asyncio.run(main())

# ioloop = asyncio.get_event_loop()
# tasks = [
#     ioloop.create_task(task_1("task_1 is completed")),
#     ioloop.create_task(task_2("task_2 is completed")),
#     ioloop.create_task(main()),
# ]
# ioloop.run_until_complete(asyncio.wait(tasks))
# ioloop.close()
