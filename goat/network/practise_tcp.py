import socket


def easy_socket():
    # 创建通信socket
    # socket.AF_INET ipv4
    # socket.SOCK_STREAM 使用面向流的TCP协议
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立通信连接
    s.connect(('www.baidu.com', 80))
    # 发送数据
    s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
    # 接受数据
    buffer = []
    while True:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    date = b''.join(buffer)
    # 关闭连接
    s.close()

    header, html = date.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    # 把接收的数据写入文件:
    with open('baidu.html', 'wb') as f:
        f.write(html)


if __name__ == '__main__':
    easy_socket()
