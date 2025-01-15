import asyncio
import threading


async def hello1(name):
    print('1泥嚎啊，{} - {}'.format(name, threading.current_thread()))
    # 异步调用 asyncio.sleep(1)，睡了一秒
    await asyncio.sleep(4)
    print('1泥嚎啊，又见面了 {} - {}'.format(name, threading.current_thread()))
    return name


async def hello(name):
    print('泥嚎啊，{} - {}'.format(name, threading.current_thread()))
    # 异步调用 asyncio.sleep(1)，睡了一秒
    await asyncio.sleep(2)
    print('泥嚎啊，又见面了 {} - {}'.format(name, threading.current_thread()))

    for i in range(5):
        print(i)
    return name


async def main():
    L = await asyncio.gather(hello("hhhh"), hello1("llll"))
    print(L)


if __name__ == '__main__':
    asyncio.run(main())
    print('main end')
