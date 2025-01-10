import psutil


def get_cpu():
    cpu_count = psutil.cpu_count()
    print('cpu count: {}'.format(cpu_count))
    logical_cpu_count = psutil.cpu_count(logical=False)
    print('logical cpu count: {}'.format(logical_cpu_count))
    cpu_times = psutil.cpu_times()
    print('cpu times: {}'.format(cpu_times))
    cpu_percent = psutil.cpu_percent()
    print('cpu percent: {}'.format(cpu_percent))


def get_memory():
    virtual_memory = psutil.virtual_memory()
    print('virtual memory: {}'.format(virtual_memory))
    swap_memory = psutil.swap_memory()
    print('swap memory: {}'.format(swap_memory))


def get_disk():
    # 磁盘使用情况
    disk_usage = psutil.disk_usage('/')
    print('disk usage: {}'.format(disk_usage))
    # 磁盘分区情况
    disk_partitions = psutil.disk_partitions()
    print('disk partitions: {}'.format(disk_partitions))
    # 磁盘IO情况
    disk_io = psutil.disk_io_counters()
    print('disk io: {}'.format(disk_io))


def get_network():
    # 获取网络读写字节/包的个数
    net_io_counters = psutil.net_io_counters()
    print('net io counters: {}'.format(net_io_counters))
    # 获取网络接口信息
    net_if_addresses = psutil.net_if_addrs()
    print('net if addresses: {}'.format(net_if_addresses))
    # 获取网络接口状态
    net_if_stats = psutil.net_if_stats()
    print('net if stats: {}'.format(net_if_stats))
    # 获取网络连接信息
    net_connections = psutil.net_connections()
    print('net connections: {}'.format(net_connections))


def get_process():
    # 获取所有的进程id
    pids = psutil.pids()
    print('all process ids: {}, counts is {}'.format(pids, len(pids)))
    # 获取指定进程ID=98531
    pro = psutil.Process(98531)
    # process info psutil.Process(pid=56886, name='DiskUnmountWatcher', status='running', started='2025-01-08 10:43:24')
    print('process info: {}'.format(pro))
    # 进程exe路径
    pro_exe = pro.exe()
    print('process exe path: {}'.format(pro_exe))
    # 进程工作目录
    # pro_cwd = pro.cwd()
    # print('process cwd: {}'.format(pro_cwd))
    # 进程启动的命令行
    # pro_cmdline = pro.cmdline()
    # print('process cmdline: {}'.format(pro_cmdline))
    # 进程的父进程id
    pro_ppid = pro.ppid()
    print('process ppid: {}'.format(pro_ppid))
    # 进程的父进程
    pro_parent = pro.parent()
    print('process parent: {}'.format(pro_parent))
    # TODO


def get_ps():
    pass


if __name__ == '__main__':
    # get_cpu()
    # get_memory()
    # get_disk()
    # get_network()
    get_process()
    get_ps()
