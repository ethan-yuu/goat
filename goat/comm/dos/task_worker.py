import time, queue
from multiprocessing.managers import BaseManager


# 队列管理工具
class QueueManager(BaseManager):
    pass


# 由于这个QueueManager只能从网络上获取Queue，所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

if __name__ == '__main__':
    # 连接到服务器，也就是运行task_master.py的机器:
    server_addr = '127.0.0.1'
    # 端口和验证码注意保持与task_master.py设置的完全一致:
    m = QueueManager(address=(server_addr, 5001), authkey=b'abc')
    # 从网络连接:
    m.connect()
    print('Connected to server %s.' % server_addr)
    # 获取Queue的对象:
    task = m.get_task_queue()
    result = m.get_result_queue()
    print('Get task')
    # 从task队列取任务,并把结果写入result队列:
    for i in range(10):
        print('Task %d' % i)
        try:
            n = task.get(timeout=1)
            print('run task %d * %d...' % (n, n))
            r = '%d * %d = %d' % (n, n, n * n)
            time.sleep(1)
            result.put(r)
            # result.put(i)
        except queue.Empty:
            print('task queue is empty.')
    # 处理结束:
    print('worker exit.')
