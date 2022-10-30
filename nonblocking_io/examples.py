import asyncio


async def task_1(msg: str) -> None:
    await asyncio.sleep(2)
    print(msg)


async def task_2(msg: str) -> None:
    await asyncio.sleep(1)
    print(msg)


async def main():
    await task_1("task_1 is completed")
    await task_2("task_2 is completed")
    print("main is completed")


asyncio.run(main())
