import subprocess

if __name__ == '__main__':
    print('演示子进程的执行')

    # print('$ nslookup www.google.com')
    # r = subprocess.call(['nslookup', 'www.google.com'])
    # print('Exit code:{}'.format(r))


    # 写法一
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)

    # 写法二
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    if err is None:
        print('error {}'.format(err))
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)
