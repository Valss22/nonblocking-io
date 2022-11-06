import asyncio
from eventloop import nonblock
from fastapi import FastAPI


async def task_1(msg: str) -> None:
    await asyncio.sleep(2)
    print(msg)


async def task_2(msg: str) -> None:
    await asyncio.sleep(1)
    print(msg)


app = FastAPI()


@app.post("/user/")
async def create_user():
    nonblock(task_1, "task1")
    nonblock(task_2, "task2")
    return {"detail": "created"}
