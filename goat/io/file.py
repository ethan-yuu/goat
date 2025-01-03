if __name__ == '__main__':
    # 写发一 读
    # try:
    #     f = open('/Users/zhangxinyu/Desktop/python/goat/README.md', 'r', encoding='utf-8')
    #     print(f.read())
    # finally:
    #     if f:
    #         f.close()

    # 写法二 读
    # with open('/Users/zhangxinyu/Desktop/python/goat/README.md', 'r', encoding='utf-8') as f:
    #     # 一次性读取全部
    #     # print(f.read())
    #     for line in f.readlines():
    #         print(line)

    # 写
    with open('/Users/zhangxinyu/Desktop/python/goat/test.txt', 'a', encoding='utf-8') as f:
        f.write('hello world from python')
