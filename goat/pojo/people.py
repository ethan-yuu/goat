class People(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an int')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 and 100')
        self._score = value

    def __init__(self, name):
        self._name = name
        self._score = 0

    def __str__(self):
        return 'People object with name {} and score {}'.format(self._name, self._score)

    __repr__ = __str__

