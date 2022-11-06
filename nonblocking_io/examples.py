import asyncio
from eventloop import nonblocking


async def task_1(msg: str) -> None:
    await asyncio.sleep(2)
    print(msg)


async def task_2(msg: str) -> None:
    await asyncio.sleep(1)
    print(msg)


@nonblocking
async def main():
    print("main is completed")


# asyncio.run(main())
