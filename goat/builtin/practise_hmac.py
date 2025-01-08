import hmac
from random import random


def practise_hmac():
    message = b'hello world'
    key = b'k'
    h = hmac.new(key, message, digestmod='MD5')
    h1 = hmac.new(key, message, digestmod='sha1')
    print(h.hexdigest())
    print(h1.hexdigest())


def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), digestmod='MD5')


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)


db = {
    'z11': User('z11', 'z11'),
    'z22': User('z22', 'z22'),
    'z33': User('z33', 'z33')
}


def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)


if __name__ == '__main__':
    practise_hmac()
