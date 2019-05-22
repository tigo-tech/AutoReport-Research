import pymysql

class ControlMysql:
    def __init__(self):
        self.__host = '203.195.154.244'
        self.__username = 'admin'
        self.__database = 'AutoReport'
        self.__cursor = None
        self.__password = self.get_password()
        self.__conn = pymysql.connect(self.__host, self.__username, self.__password
                                      , self.__database, charset="utf8")

    def get_password(self):
        password = input('Enter the password：')
        return password



    # 列出表所有的列名
    def list_columns_name(self,table_name):
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute("select * from %s" % table_name)
        col_name_list = [tuple[0] for tuple in self.__cursor.description]
        self.__cursor.close()
        return col_name_list


    # 列出表所有列
    def list_columns_detail(self,table_name):
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute("SELECT * FROM information_schema.columns WHERE TABLE_NAME = %s", table_name)
        col_name_list = [(tuple[3], tuple[7]) for tuple in self.__cursor.fetchall()]
        self.__cursor.close()
        return col_name_list


    # 列出所有的表
    def list_table(self):
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute("show tables")
        table_list = [tuple[0] for tuple in self.__cursor.fetchall()]
        self.__cursor.close()
        return table_list


# 查询单表外键关系
    def list_fk(self, table_name):
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute("SELECT * FROM information_schema.INNODB_SYS_FOREIGN WHERE FOR_NAME = %s OR REF_NAME = %s"
                              % ("'" + self.__database + "/" + table_name + "'", "'" + self.__database + "/" + table_name + "'"))
        table_relation_list = self.__cursor.fetchall()
        relation_dict = {}
        table_relations = {}
        for relation in table_relation_list:
            relation_dict['fk_name'] = relation[0]
            relation_dict['from_table'] = str(relation[1])[str(relation[1]).index("/") + 1:]
            relation_dict['to_table'] = str(relation[2])[str(relation[2]).index("/") + 1:]
            self.__cursor.execute("SELECT * FROM information_schema.INNODB_SYS_FOREIGN_COLS WHERE ID = %s", relation_dict['fk_name'])
            columns_list = self.__cursor.fetchall()
            for columns in columns_list:
                relation_dict['from_field'] = columns[1]
                relation_dict['to_field'] = columns[2]
            table_relations[relation_dict['fk_name']] = relation_dict
        return table_relations



if __name__ == '__main__':
    a = ControlMysql()
    tables = a.list_table()
    for table in tables:
        print(table)
        col_names = a.list_columns_name(table)
        print(col_names)
        col_details = a.list_columns_detail(table)
        print(col_details)
        relations = a.list_fk(table)
        print(relations)
