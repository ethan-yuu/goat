# 线程共享变量
import multiprocessing
import threading

balance = 0
lock = threading.Lock()


def change_balance(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_change_balance(n):
    for i in range(10000000):
        # 加锁
        lock.acquire()
        try:
            change_balance(n)
        finally:
            # 释放
            lock.release()


if __name__ == '__main__':
    # r5 = threading.Thread(target=run_change_balance, args=(5,))
    # r8 = threading.Thread(target=run_change_balance, args=(8,))
    # r5.start()
    # r8.start()
    # r5.join()
    # r8.join()
    # print('finial balance:', balance)
    print(multiprocessing.cpu_count())
