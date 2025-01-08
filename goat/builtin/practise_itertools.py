import itertools

if __name__ == '__main__':
    # itertools.count(1)
    # n = itertools.count(1)
    # for i in n:
    #     print(i)

    # itertools.cycle('zxcvbnm')
    # c = itertools.cycle('zxcvbnm')
    # for i in c:
    #     print(i)

    # itertools.repeat('h', 20)
    # r = itertools.repeat('h', 20)
    # for i in r:
    #     print(i)

    # c = itertools.chain('zxc', 'dvg', '124')
    # for i in c:
    #     print(i)

    for key, group in itertools.groupby('bfubvbubchbBUVTYUBHFYSVBFHBJD', lambda c: c.upper()):
        print(key, list(group))
