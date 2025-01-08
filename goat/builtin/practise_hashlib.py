import hashlib

if __name__ == '__main__':
    # md5
    md5 = hashlib.md5()
    md5.update('hello zxy'.encode('utf-8'))
    # 'hello zxy' md5 --> f2473f5f3b4b948e42916b8e171c0975
    print("'hello zxy' md5 --> {}".format(md5.hexdigest()))
    md5.update('hello zzz'.encode('utf-8'))
    # 'hello zxz' md5 --> daaf59cbb31785e971226d8638ca3787
    print("'hello zxz' md5 --> {}".format(md5.hexdigest()))

    # sha1
    sha1 = hashlib.sha1()
    sha1.update('hello zxy'.encode('utf-8'))
    # 'hello zxy' sha1 --> 3620e6ae92ab2fb750b2e4619899d19d613aba5e 32
    print("'hello zxy' sha1 --> {}".format(sha1.hexdigest()))
    sha1.update('hello zxz'.encode('utf-8'))
    # 'hello zxz' sha1 --> ee25254a4557bb82720c44b6e0701a5d9bbf619d 40
    print("'hello zxz' sha1 --> {}".format(sha1.hexdigest()))
