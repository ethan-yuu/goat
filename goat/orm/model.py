from goat.orm.field import Field


# 元类
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model:{}'.format(name))
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: {} ====> {}'.format(k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        # 属性和列的映射关系
        attrs['__mappings__'] = mappings
        # 表名
        attrs['__table__'] = name

        return type.__new__(cls, name, bases, attrs)


# 基类
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(" 'Model' object has no attribute {} ".format(key))

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self, k, None))
        sql = 'insert into {} ({}) values ({})'.format(self.__table__, ','.join(fields), ','.join(params))
        print('SQL: {}'.format(sql))
        print('ARGS: {}'.format(args))
