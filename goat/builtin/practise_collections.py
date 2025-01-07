from collections import namedtuple, deque, defaultdict, OrderedDict


# 先进先出的dict
class LastUpdatedDict(OrderedDict):
    def __init__(self, cap):
        super(LastUpdatedDict, self).__init__()
        self._cap = cap

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._cap:
            last = self.popitem(last=False)
            print('remove: {}'.format(last))
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


if __name__ == '__main__':
    # namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print('{} , p.x = {}, p.y = {}'.format(p, p.x, p.y))
    print('is tuple: {}'.format(isinstance(p, tuple)))
    print('is Point: {}'.format(isinstance(p, Point)))

    # deque
    q = deque(['a', 'b', 'c', 'd'])
    q.appendleft('e')
    q.append('f')
    print('q --> {}'.format(q))
    q.pop()
    print('q --> {}'.format(q))
    q.popleft()
    print('q --> {}'.format(q))

    # defaultdict
    dd = defaultdict(lambda: 'hhh')
    dd['key1'] = 'abc'
    dd['key2'] = 'def'
    print("dd['key1'] --> {}".format(dd['key1']))
    print("dd['key2'] --> {}".format(dd['key2']))
    print("dd['key3'] --> {}".format(dd['key3']))

    # OrderedDict
    d = dict([('a', 1), ('b', 2), ('c', 3)])
    print('d --> {}'.format(d))
    print('d --> {}'.format(d))
    print('d --> {}'.format(d))
    print('d --> {}'.format(d))
    print('d.keys() --> {}'.format(d.keys()))
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print('od --> {}'.format(od))
    print('od.keys() --> {}'.format(od.keys()))
