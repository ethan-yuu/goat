import os
import time
from multiprocessing import Process, Pool
from random import random


def run_proc(name):
    print('Run child process: {}-{}'.format(name, os.getpid()))


def long_time_task(name):
    print('Run child process: {}-{}'.format(name, os.getpid()))
    start = time.time()
    time.sleep(random() * 2)
    end = time.time()
    print('long_time_task runs {} seconds'.format(end - start))


if __name__ == '__main__':
    print(os.cpu_count())

    # 进程池
    p = Pool(8)
    for i in range(9):
        p.apply_async(long_time_task, args=(i,))
    print('waiting for all subprocesses to finish')
    p.close()
    p.join()
    # time.sleep(random() * 5)
    print('all subprocesses finished')

    # 多进程
    # print('Run child process: {}'.format(os.getpid()))
    # p = Process(target=run_proc, args=('test',))
    # print('child process will start')
    # p.start()
    # p.join()
    # print('child process end')
