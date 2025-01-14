import sqlite3


def create_table():
    return 'create table t_user (id varchar(20) primary key, name varchar(20))'


def insert_user(id):
    return 'insert into t_user (id,name) values (\'{}\',\'一吱小fei鹅\')'.format(id)


def update_user():
    return 'update t_user set name = \'一吱小fei鹅_gaga\' where id = \'1\''


def delete_user():
    return 'delete from t_user where id = \'2\''


def get_user():
    return 'select * from user where id=?', ('1',)


def list_user():
    return 'select * from t_user'


if __name__ == '__main__':
    # 连接到数据库，数据库文件是test.db，如果数据库文件不存在，就会自己创建
    conn = sqlite3.connect('test.db')

    # 创建一个游标 Cursor，用于执行sql语句
    cursor = conn.cursor()

    # # 执行 sql 创建user表
    # result = cursor.execute(create_table())
    # print('create_table() --> {}'.format(result))

    # 新增用户
    # result = cursor.execute(insert_user(1))
    # print('insert_user(1) --> {}'.format(result))
    # result = cursor.execute(insert_user(2))
    # print('insert_user(2) --> {}'.format(result))

    # 编辑用户
    cursor.execute(update_user())
    # # 获取用户
    # cursor.execute(get_user())
    # 删除用户
    # cursor.execute(delete_user())
    # 获取用户列表
    result = cursor.execute(list_user())
    print('list_user() --> {}'.format(result))
    # rowcount 返回 影响的行数
    print(cursor.rowcount)

    # 必须要提交事物，不然不会存到数据库里
    conn.commit()

    # 获得查询结果集
    values = cursor.fetchall()
    print('fetchall() : {}'.format(values))

    # 及时释放关闭资源
    cursor.close()
    conn.close()
