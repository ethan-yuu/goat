def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[消费者 消费中.... {}]'.format(n))


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[生产者 生产中... {}]'.format(n))
        r = c.send(n)
        print('[生产者 消费者return: ]'.format(r))
    c.close()


if __name__ == '__main__':
    c = consumer()
    produce(c)
