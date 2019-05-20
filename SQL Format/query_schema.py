import pymysql
import string


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


# 查询单表外键关系
def list_fk(cursor, table_name):
    cursor.execute("SELECT * FROM information_schema.INNODB_FOREIGN WHERE FOR_NAME LIKE %s OR REF_NAME LIKE %s"
                   % ('%' + table_name, '%' + table_name))
    table_relation_list = cursor.fetchall()
    relation_dict = {}
    table_relations = {}
    for relation in table_relation_list:
        relation_dict['fk_name'] = str(relation[0])[str(relation[0]).index("/")]
        relation_dict['from_table'] = str(relation[1])[str(relation[1]).index("/")]
        relation_dict['to_table'] = str(relation[2])[str(relation[2]).index("/")]
        cursor.execute("SELECT * FROM information_schema.INNODB_FOREIGN_COLS WHERE ID = %s", relation_dict['fk_name'])
        columns_list = cursor.fetchall
        for columns in columns_list:
            relation_dict['from_field'] = columns[1]
            relation_dict['to_field'] = columns[2]
        table_relations[relation_dict['fk_name']] = relation_dict
    return table_relations


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
        # relations = list_fk(db_cursor, table)
        # print(relations)
