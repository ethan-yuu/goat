import queue
import time
from multiprocessing.managers import BaseManager
import random

# 实例化队列为任务队列-全局变量，相当于单例
task_queue = queue.Queue()
# 实例化队列为结果队列-全局变量，相当于单例
result_queue = queue.Queue()


# 发送任务的队列:
def get_task_queue():
    return queue.Queue()


# 接收结果的队列:
def get_result_queue():
    return queue.Queue()


# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    # 把两个Queue都注册到网络上，callable参数关联了Queue对象
    QueueManager.register('get_task_queue', callable=get_task_queue)
    QueueManager.register('get_result_queue', callable=get_result_queue)

    # 绑定端口号5000，设置验证码为‘abc’
    manager = QueueManager(address=('127.0.0.1', 5001), authkey=b'abc')
    # manager = QueueManager(address=('', 5001), authkey=b'abc')
    # 启动队列
    manager.start()
    # 获得通过网络访问的Queue对象
    task = manager.get_task_queue()
    print('master-->task:{}'.format(task))
    result = manager.get_result_queue()
    print('master-->result:{}'.format(result))

    # 给task队列放几个任务进去
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task {} to task_queue'.format(n))
        task.put(n)

    time.sleep(10)

    # 从result队列读取任务结果
    print('Try get result from result_queue ...')
    for i in range(10):
        r = result.get(timeout=2)
        print('Result: {}'.format(r))

    # 关闭
    manager.shutdown()
    print('task_master exit!')
