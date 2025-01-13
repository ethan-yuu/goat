import socket

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 和 服务器server建立连接
    client.connect(('127.0.0.1', 9999))
    print("client socket info {}:".format(client.getsockname()))
    # 接受到消息
    message = client.recv(1024).decode('utf-8')
    print('client recv: {}'.format(message))
    for data in [b'hello', b'world', b'1111']:
        # 发送数据
        client.send(data)
        # 接受数据
        print(client.recv(1024).decode('utf-8'))
    # 发送 exit 断开连接
    client.send(b'exit')
    # 关闭通信通道
    client.close()
