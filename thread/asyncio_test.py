import threading
import asyncio


# # @asyncio.coroutine把一个generator标记为coroutine类型
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")
#
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


@asyncio.coroutine
def nihao():
    print('你好 (%s)' % threading.current_thread())
    yield from asyncio.sleep(2)
    print('你又好 (%s)' % threading.current_thread())


loop = asyncio.get_event_loop()
tasks = [hello(), nihao()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# async和await是针对coroutine的新语法，
# 要使用新的语法，只需要做两步简单的替换：
# 把@asyncio.coroutine替换为async；
# 把yield from替换为await
