class Student(object):
    def __init__(self):
        self._name = 'name'
        self._score = 'score'

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_score(self):
        return self._score

    def set_score(self, score):
        self._score = score

    def print_score(self):
        print('%s: %s' % (self._name, self._score))

    def __str__(self):
        return 'Student object with name {} and score {}'.format(self._name, self._score)

    def __getattr__(self, attr):
        if attr == 'sex':
            return 0
        raise AttributeError("object has no attribute '{}'".format(attr))

    def __call__(self):
        print('Class is Student')


if __name__ == '__main__':
    stu = Student()
    # print(stu.sex)
    # callable(stu)
    print(type((Student)))
    print(type((Student())))
    print(type(stu))
    type.__new__()
