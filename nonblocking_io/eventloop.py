import asyncio
from curses import wrapper
from functools import wraps
import nest_asyncio

nest_asyncio.apply()


# def nonblocking(task, *args):
#     loop = asyncio.get_event_loop()
#     task = loop.create_task(task(*args))
#     loop.run_until_complete(asyncio.wait([task]))


# class EventLoop:
#     def __init__(self, func=None) -> None:
#         self.__func = func
#         self.__tasks = []
#         self.__loop = asyncio.get_event_loop()

#     async def __call__(self):
#         self.__tasks.append(self.__func)
#         await self.__func()

#     def nonblocking(self, task, *args):
#         task = self.__loop.create_task(task(*args))
#         self.__tasks.append(task)
#         if len(self.__tasks) >= 0:
#             self.__loop.run_until_complete(asyncio.wait(self.__tasks))
#             self.__tasks.clear()


def nonblocking(func):
    def wrapper():
        print(1)
        return func()

    return wrapper
