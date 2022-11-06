import asyncio
from types import FunctionType
import nest_asyncio

nest_asyncio.apply()


class EventLoop:
    def __init__(self):
        self.__tasks = []
        self.__loop = asyncio.get_event_loop()

    def nonblocking(self, task, *args):
        task = self.__loop.create_task(task(*args))
        self.__tasks.append(task)
        if len(self.__tasks) >= 0:
            self.__loop.run_until_complete(asyncio.wait(self.__tasks))
            self.__tasks.clear()


def foo():
    pass


print(type(foo) is FunctionType)
