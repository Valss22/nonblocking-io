import asyncio
from utils import nonblock
from fastapi import FastAPI
import schedule


def task_1(msg: str) -> None:
    print(msg)


async def task_2(msg: str) -> None:
    await asyncio.sleep(1)
    print(msg)


app = FastAPI()


@app.on_event("startup")
async def startup():
    ...
    # schedule.every(2).seconds.do(task_1, "task_1")

    # while True:
    #     schedule.run_pending()
    #     await asyncio.sleep(0.1)


@app.post("/user/")
async def create_user():
    nonblock(task_1, "task1")
    nonblock(task_2, "task2")
    return {"detail": "created"}
