import socket
import threading
import time


def tcp_link(sock, addr):
    print('Accept new connection from {}'.format(addr))
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, {}!'.format(data.decode('utf-8'))).encode('utf-8'))
    sock.close()
    print('Connection from {} closed'.format(addr))


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 服务端绑定监听端口
    server.bind(('127.0.0.1', 9999))
    # 监听客户端连接，只允许最多连接5个
    server.listen(5)
    print('泥嚎啊，我是server，监听连接 forever......')

    # 设置死循环 永远监听
    while True:
        # 接受一个新连接
        sock, addr = server.accept()
        # 创建新线程来处理客户端的TCP连接
        conn = threading.Thread(target=tcp_link, args=(sock, addr))
        conn.start()

    # 服务器须按Ctrl+C退出程序
