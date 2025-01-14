import mysql


def create_table():
    return 'create table t_user(id varchar(20) primary key, name varchar(20))'


def insert_user():
    return 'insert into t_user(id,name) values (%s,%s)', ('1', '一吱小fei鹅')


def update_user():
    return 'update t_user set name=%s where id=%s', ('1', '一吱小fei鹅_gaga')


def get_user():
    return 'select * from t_user where id=%s', ('1',)


def delete_user():
    return 'delete from t_user where id=%s', ('1',)


if __name__ == '__main__':
    # 连接数据库
    conn = mysql.connector.connect(user='root', password='<PASSWORD>', host='localhost', database='test')
    # 获得操作数据库的游标
    cursor = conn.cursor()

    # 创建表
    cursor.execute(create_table())
    # 新增用户
    cursor.execute(insert_user())

    print(cursor.fetchall())

    # 更新用户
    cursor.execute(update_user())
    # 获取用户
    cursor.execute(get_user())
    # 删除用户
    cursor.execute(delete_user())

    cursor.commit()

    # 释放资源
    cursor.close()
    conn.close()
