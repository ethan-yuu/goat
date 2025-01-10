import chardet


# 检测文本内容的编码格式
def check_encoding(content=b"a beauty"):
    result_dict = chardet.detect(content)
    print('check_encoding: content --> {}, resultDict: {}'.format(content, result_dict))


if __name__ == '__main__':
    check_encoding()
    check_encoding("泥嚎啊 嘻嘻".encode('utf-8'))
    check_encoding('离离原上草，一岁一枯荣'.encode('gbk'))
    check_encoding('最新の主要ニュース'.encode('euc-jp'))
