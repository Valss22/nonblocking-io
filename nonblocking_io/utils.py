import asyncio
import nest_asyncio

nest_asyncio.apply()


# Why it's working on fastapi endpoints without run_until_compile ???
def nonblock(task, *args):
    loop = asyncio.get_event_loop()
    loop.create_task(task(*args))
