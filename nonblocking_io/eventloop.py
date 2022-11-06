import asyncio
import nest_asyncio

nest_asyncio.apply()


class EventLoop:
    def __init__(self):
        self.__tasks = []
        self.__loop = asyncio.get_event_loop()

    async def nonblocking1(self, func):
        async def wrapper(*args, **kwargs):
            print(1)
            task = self.__loop.create_task(func(*args, **kwargs))
            self.__tasks.append(task)

        return wrapper

    def nonblocking(self, task, *args):
        task = self.__loop.create_task(task(*args))
        self.__tasks.append(task)
        if len(self.__tasks) >= 2:
            self.__loop.run_until_complete(asyncio.wait(self.__tasks))
            self.__tasks.clear()


# TODO: why it's working on fastapi endpoints without run_until_compile ???
def nonblock(task, *args):
    loop = asyncio.get_event_loop()
    loop.create_task(task(*args))
