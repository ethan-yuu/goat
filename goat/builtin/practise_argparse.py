import argparse


def main():
    # 定义一个 ArgumentParser 实例
    parser = argparse.ArgumentParser(
        prog='practise_argparse',  # 程序名
        description='Backup MySQL database',  # 描述
        epilog='Copyright(r), 2025',  # 说明信息
    )
    # 位置参数
    parser.add_argument('outfile')
    # 关键字参数 连接地址，默认为 localhost
    parser.add_argument('--host', default='localhost')
    # 关键字参数 连接端口号，默认为 3306 ，int
    parser.add_argument('--port', default='3306', type=int)
    # 关键字参数 用户名
    parser.add_argument('-u', '--user', required=True)
    # 关键词参数 密码
    parser.add_argument('-p', '--password', required=True)
    # 关键词参数 备份数据库
    parser.add_argument('--database', required=True)
    # 如果用户启动时传递了这个参数，就代表要压缩备份数据库，不传就代表不压缩
    parser.add_argument('-gz', '--gzcompress', action='store_true', required=False, help='Compress backup files by gz.')

    # 解析参数
    args = parser.parse_args()

    # 打印命令传参
    print('parsed args: ')
    print('outfile: {}'.format(args.outfile))
    print('host: {}'.format(args.host))
    print('port: {}'.format(args.port))
    print('user: {}'.format(args.user))
    print('password: {}'.format(args.password))
    print('database: {}'.format(args.database))
    print('gzcompress: {}'.format(args.gzcompress))


if __name__ == '__main__':
    main()
