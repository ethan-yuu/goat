import socket

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    server.bind(('127.0.0.1', 9999))
    print('我是UDP 快来给我发消息吧～～')

    while True:
        data, addr = server.recvfrom(1024)
        print('我收到消息啦！是 {} 发嘟'.format(addr))
        server.sendto(b'Hello, %s!' % data, addr)
