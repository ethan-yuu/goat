from datetime import datetime

import requests

post_url = 'https://accounts.douban.com/login'
post_data = {'form_email': '<EMAIL>', 'form_password': '123456'}
date_format = '%a, %d %b %Y %H:%M:%S GMT'


def get():
    response = requests.get('https://www.google.com/', params={})  # 豆瓣首页
    print('response encoding: {}'.format(response.encoding))
    print('response status code: {}'.format(response.status_code))
    print('response text: {}'.format(response.text))


def get_json():
    response = requests.get(
        'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
    print('response encoding: {}'.format(response.encoding))
    print('response json: {}'.format(response.json()))


def get_headers():
    response = requests.get('https://www.douban.com/', headers={
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
    print('response encoding: {}'.format(response.encoding))


def post():
    response = requests.post('https://accounts.douban.com/login',
                             data={'form_email': '<EMAIL>', 'form_password': '123456'})
    # requests 默认使用 application/x-www-form-urlencoded 的编码方式
    print('response status_code: {}'.format(response.status_code))


def post_json():
    params = {'key': 'value'}
    response = requests.post('https://accounts.douban.com/login',
                             data={'form_email': '<EMAIL>', 'form_password': '123456'},
                             json=params)
    print('response status_code: {}'.format(response.status_code))
    print('response headers: {}'.format(response.headers))
    response_date = response.headers['date']
    print("response headers['date'] type: {}".format(type(response_date)))
    date_datetime = datetime.strptime(response_date, date_format)
    print('response headers[date]-format: {}'.format(date_datetime))
    print('response headers[date]-format-date: {}'.format(date_datetime.date()))


def post_file():
    # rb 二进制读取文件
    upload_file = {'file': open('file.txt', 'rb')}
    response = requests.post(post_url,
                             data=post_data,
                             files=upload_file)
    print('response headers: {}'.format(response.headers))


if __name__ == '__main__':
    # get()
    # get_json()
    # post()
    post_json()
    # post_file()
