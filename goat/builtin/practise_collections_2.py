import argparse
import os
from collections import ChainMap, Counter

if __name__ == '__main__':
    # 缺省构造参数
    defaults = {
        'color': 'red',
        'user': 'guest'
    }

    # 构造命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user')
    parser.add_argument('-c', '--color')
    namespace = parser.parse_args()
    command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}

    # 组合成ChainMap
    combined = ChainMap(command_line_args, os.environ, defaults)

    # 打印参数
    print('color: {}'.format(combined['color']))
    print('user: {}'.format(combined['user']))

    # Counter 计数器
    c = Counter('ssssssssscdvnknnnnnn')
    print(c.most_common())
    print('c {} '.format(c))
    print(c.keys())
    print(c.pop('s'))
    print(c)

