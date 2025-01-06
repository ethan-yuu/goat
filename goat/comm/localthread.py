import threading

# 全局变量，ThreadLocal
local_var = threading.local()


def process_var():
    vari = local_var.var
    print('thread local variable: {}'.format(vari))


def process_thread(vari):
    local_var.var = vari
    process_var()


if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=('hhhhhhh',))
    t2 = threading.Thread(target=process_thread, args=('llllllll',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
