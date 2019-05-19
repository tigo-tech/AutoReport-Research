import pymysql


# 列出表所有的列名
def list_columns_name(cursor, table_name):
    cursor.execute("select * from %s" % table_name)
    col_name_list = [tuple[0] for tuple in cursor.description]
    return col_name_list


# 列出表所有列
def list_columns_detail(cursor, table_name):
    cursor.execute("SELECT * FROM information_schema.columns WHERE TABLE_NAME = %s", table_name)
    col_name_list = [(tuple[3], tuple[7]) for tuple in cursor.fetchall()]
    return col_name_list


# 列出所有的表
def list_table(cursor):
    cursor.execute("show tables")
    table_list = [tuple[0] for tuple in cursor.fetchall()]
    return table_list


# 初始化DB链接
def initial_cursor(host, user, pwd, db_name):
    db = pymysql.connect(host, user, pwd, db_name, charset="utf8")
    cursor = db.cursor()
    return cursor


localhost = '127.0.0.1'
username = 'root'
password = 'root'
database = 'autoreport'


if __name__ == '__main__':
    db_cursor = initial_cursor(localhost, username, password, database);
    tables = list_table(db_cursor)
    for table in tables:
        print(table)
        col_names = list_columns_name(db_cursor, table)
        print(col_names)
        col_details = list_columns_detail(db_cursor, table)
        print(col_details)
