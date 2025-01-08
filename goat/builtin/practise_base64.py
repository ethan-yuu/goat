import base64

if __name__ == '__main__':
    encoding = base64.b64encode(b'hifnuihsvoh')
    print(encoding)
    decoding = base64.b64decode(encoding)
    print(decoding)

    encoding0 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
    encoding1 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
    print('encoding0 --> {}'.format(encoding0))
    print('encoding1 --> {}'.format(encoding1))
