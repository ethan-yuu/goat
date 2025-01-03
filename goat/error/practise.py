from functools import reduce


def str2num(s):
    assert s != None, "No valid string"
    try:
        return float(s)
    except ValueError:
        raise ValueError(f"Cannot convert '{s}' to a number.")


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print(e)
