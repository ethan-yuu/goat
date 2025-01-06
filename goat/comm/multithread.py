import random
import threading
import time


def loop():
    print('thread {} start run'.format(threading.current_thread().name))
    n = 0
    while n < 5:
        n = n + 1
        print('thread {}  >>> {}'.format(threading.current_thread().name, n))
        time.sleep(random.random())
    print('thread {} end run'.format(threading.current_thread().name))


if __name__ == '__main__':
    print('thread {} start run'.format(threading.current_thread().name))
    t = threading.Thread(target=loop)
    t.start()
    t.join()
    print('thread {} ended.'.format(threading.current_thread().name))
