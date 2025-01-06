import os
import random
import time
from multiprocessing import Queue, Process


# 写进程写数据
def write(q):
    print('{}-Process to write'.format(os.getpid()))
    for value in ('A', 'B', 'C', 'D'):
        print('{}-Process put {} to queue:'.format(os.getpid(), value))
        q.put(value)
        time.sleep(random.random())


# 读进程读数据
def read(q):
    print('{}-Process to read'.format(os.getpid()))
    while True:
        value = q.get(True)
        print('{}-Process get {} from queue:'.format(os.getpid(), value))


if __name__ == '__main__':
    # 父进程创建子进程间的通信通道
    q = Queue()
    wp = Process(target=write, args=(q,))
    rp = Process(target=read, args=(q,))
    # 启动写进程
    wp.start()
    # 启动读进程
    rp.start()
    # 等待写进程写完数据之后开始执行，不用管读进程，因为它一直在读，强行终止
    wp.join()
    rp.terminate()
    # 及时关闭队列
    q.close()
