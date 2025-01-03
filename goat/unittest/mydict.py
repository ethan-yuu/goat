class Dict(dict):
    def __init__(self, **kwargs):
        super(Dict, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as e:
            raise AttributeError("'Dict' object has no attribute {}".format(key))

    def __setattr__(self, key, value):
        self[key] = value
