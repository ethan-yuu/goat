from io import StringIO

if __name__ == '__main__':
    f = StringIO()
    print(f.write('hello world'))
    print(f.write('hello zxy'))
    print(f.getvalue())

    ff = StringIO("jcgbdavhfdvwib\nbchikbcdfhjvuebvhj\nfre] =\nfrefhui")
    while True:
        s = ff.readline()
        if s == '':
            break
        print(s.strip())
