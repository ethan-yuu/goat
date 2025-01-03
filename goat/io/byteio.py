from io import BytesIO

if __name__ == '__main__':
    f = BytesIO()
    f.write(b'hello')
    print(f.read())
