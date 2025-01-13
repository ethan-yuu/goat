import socket

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for data in [b'hello', b'world', b'udp']:
        # 发送数据
        client.sendto(data, ('127.0.0.1', 9999))
        # 接受数据
        print(client.recv(1024).decode('utf-8'))

    client.close()
