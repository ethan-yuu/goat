import os
import random
import time
from multiprocessing import Pipe, Process


# 写进程写数据
def write(p):
    print('{}-Process start to write data to pipe'.format(os.getpid()))
    for date in ('A', 'B', 'C', 'D'):
        print('{}-Process write data {} to pipe'.format(os.getpid(), date))
        p.send(date)
        time.sleep(random.random())
    # 关闭通道
    p.close()


# 读进程读数据
def read(p):
    print('{}-Process start to read data from pipe'.format(os.getpid()))
    while True:
        if p.poll():
            value = p.recv()
            print('{}-Process read date {} from pipe'.format(os.getpid(), value))
            if value == 'D':
                # 跳出死循环不再等待
                break
    # 关闭通道
    p.close()


if __name__ == '__main__':
    # 父进程创建用于通信的管道
    p1, p2 = Pipe()
    wp = Process(target=write, args=(p1,))
    rp = Process(target=read, args=(p2,))
    # 启动读写进程
    wp.start()
    rp.start()
    # 等待读写进程写完数据后关闭进程
    wp.join()
    rp.join()
