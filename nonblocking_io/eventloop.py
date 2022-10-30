import asyncio
from functools import wraps
import nest_asyncio

nest_asyncio.apply()


class EventLoop:
    def __init__(self) -> None:
        self._tasks = []
        self._loop = asyncio.get_event_loop()

    def nonblocking(self, task, *args):
        task = self._loop.create_task(task(*args))
        self._tasks.append(task)
        if len(self._tasks) >= 0:
            self._loop.run_until_complete(asyncio.wait(self._tasks))
            self._tasks.clear()
