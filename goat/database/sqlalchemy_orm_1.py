from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# 创建对象的基类
Base = declarative_base()


# book表
class Book(Base):
    # 表名
    __tablename__ = 't_book'

    # 表结构字段
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    user_id = Column(String(20), ForeignKey('user.id'))  # 设置外键做关联


# 用户表
class User(Base):
    # 表名
    __tablename__ = 't_user'

    # 表结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    books = relationship('Book')  # books 是 t_user 的一个属性，books属性将返回一个包含若干个Book对象的list


# 学校表
class School(Base):
    # 表名
    __tablename__ = 't_school'

    # 表结构
    id = Column(String(20), primary_key=True)
    address = Column(String(20))


if __name__ == '__main__':
    # 初始化数据库连接 '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
    engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
    # 初始化DBSession类型
    DBSession = sessionmaker(bind=engine)

    # 当前会话-用于新增用户
    session = DBSession()
    new_user = User(id='1', name='一吱小fei鹅_gaga')
    # 新增用户（相当于执行sql: insert into t_user (id,name) value (%s,%s), ('1', '一吱小fei鹅_gaga')）
    session.add(new_user)
    # 提交保存至数据库
    session.commit()
    # 关闭当前会话
    session.close()

    # 当前会话-用于查询用户
    session = DBSession()
    user = session.query(User).filter(User.id == '1').one()
    print("user's type: {}".format(type(user)))
    print("user's value: {}".format(user))
    session.close()
