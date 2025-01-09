import logging
import urllib
from urllib import request, parse


def simple_get():
    # urlopen 抓取接口内容，相当于发送一个GET请求到指定的页面
    with request.urlopen('https://github.com/ethan-yuu?tab=overview&from=2025-01-01&to=2025-01-08') as r:
        data = r.read().decode('utf-8')
        print('data: ')
        print(data)
        print('status code: {} '.format(r.status))
        for k, v in r.getheaders():
            print('%s: %s' % (k, v))


def get():
    # 模拟浏览器发送get请求
    req = request.Request(url='http://www.douban.com/')
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        print('Status: {}, Reason {}'.format(f.status, f.reason))
        for k, v in f.getheaders():
            print('k: {}, v: {}'.format(k, v))
        print('data: ')
        print(f.read().decode('utf-8'))


def post():
    print('Login to 微博')
    # 模拟浏览器发送post请求
    email = input('Email: ')
    password = input('Password: ')
    login_data = parse.urlencode([
        ('username', email),
        ('password', password),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])
    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer',
                   'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
        print('status: {}, reason: {}'.format(f.status, f.reason))
        for k, v in f.getheaders():
            print('k: {}, v: {}'.format(k, v))
        print("data: ")
        resp = f.read().decode('utf-8')
        print(resp)


def proxy_handler():
    proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
    proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
    proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
    opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
    with opener.open('http://www.example.com/login.html') as f:
        pass


if __name__ == '__main__':
    # response = urllib.request.urlopen('http://example.com')
    # # 使用内置的dir()函数查看对象的属性和方法列表
    #  print(dir(response))
    proxy_handler()
