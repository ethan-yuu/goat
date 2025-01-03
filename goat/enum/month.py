from enum import Enum

Month = Enum('M', ('J1', 'F', 'M', 'J2', 'J3', 'A', 'S', 'O', 'N', 'D'))

if __name__ == '__main__':
    for name, member in Month.__members__.items():
        print( name, member.value)
