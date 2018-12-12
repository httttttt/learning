"""
async和await是针对coroutine的新语法，
    要使用新的语法，只需要做两步简单的替换：
    1、把@asyncio.coroutine替换为async；
    2、把yield from替换为await
"""

import threading
import asyncio


async def hello():
    print('are u ok? (%s)' % threading.currentThread())
    await asyncio.sleep(2)
    print('am ok (%s)' % threading.currentThread())


async def nihao():
    print('你好吗 (%s)' % threading.currentThread())
    await asyncio.sleep(4)
    print('我很好 (%s)' % threading.currentThread())


task = [hello(), nihao()]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(task))
loop.close()
