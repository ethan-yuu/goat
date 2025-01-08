import struct

if __name__ == '__main__':
    d = struct.pack('>I', 10240099)
    # d --> b'\x00\x9c@c', type --> <class 'bytes'>
    print('d --> {}, type --> {}'.format(d, type(d)))

    dd = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
    # dd --> (4042322160, 32896), type --> <class 'tuple'>
    print('dd --> {}, type --> {}'.format(dd, type(dd)))
