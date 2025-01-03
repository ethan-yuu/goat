from goat.orm.field import IntegerField, StringField
from goat.orm.model import Model


class User(Model):
    id = IntegerField('id')
    name = StringField('name')
    email = StringField('email')
    password = StringField('password')


if __name__ == '__main__':
    # 用户实例
    u = User(id=1, name='test', email='<EMAIL>', password='<PASSWORD>')
    # 保存到数据库
    u.save()
