import logging


def foo():
    r = some_function()
    if r == -1:
        return -1
    # do some other
    return r


def bar():
    r = foo()
    if r == -1:
        print('Error')
    else:
        pass


def some_function():
    pass


if __name__ == '__main__':
    try:
        print('try')
        r = 10 / int('2')
        print('result {}'.format(r))
    except ZeroDivisionError as e:
        logging.exception(e)
    except ValueError as e:
        logging.exception(e)
    else:
        raise ValueError('其实执行没报错，嘻嘻')
    finally:
        logging.info('finally')
