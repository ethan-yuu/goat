from contextlib import contextmanager


class Query(object):
    def __init__(self, name):
        self.name = name

    # 写法一
    # def __enter__(self):
    #     print('Begin')
    #     return self
    #
    # def __exit__(self, exc_type, exc_value, traceback):
    #     if exc_type is not None:
    #         print('Error')
    #     else:
    #         print('End')

    def query(self):
        print('Query info about {}'.format(self.name))


# 写法二
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


if __name__ == '__main__':
    print('0000')
    # 写法一
    with Query('HHHH') as q:
        print('1111')
        q.query()
        print('2222')

    # 写法二
    with create_query('llllll') as q:
        print('3333')
        q.query()
        print('4444')
