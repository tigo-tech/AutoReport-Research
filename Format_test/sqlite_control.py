import sqlite3

class ControlSqlite:
    def __init__(self,database):
        self.__database = database
        self.__conn = sqlite3.connect(self.__database)
        self.__cursor  = None

    def execute(self,sql_str):
        '''
        :param sql_str: 传入生成的sql语句
        :return: 返回查询结果元组
        '''
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute(sql_str)
        result = self.cursor.fetchall()
        # print(result)
        self.__cursor.close()
        return result

    def get_columns(self,tablename):
        '''
        :param tablename: 表名
        :return: 返回列名列表
        '''
        self.__cursor = self.__conn.cursor()
        str = "PRAGMA table_info("+ tablename +");"
        self.__cursor.execute(str)
        result = self.__cursor.fetchall()
        # print(result)
        self.__cursor.close()
        column_list = []
        for col in result:
            column_list.append(col[1])
        return column_list

    def get_tables(self):
        '''
        :return:返回数据库内所有表元组
        '''
        self.__cursor = self.__conn.cursor()
        self.__cursor.execute("SELECT name FROM sqlite_master WHERE type=\'table\' ORDER BY name;")
        result = self.__cursor.fetchall()
        # print(result)
        self.__cursor.close()
        return result



if __name__ == '__main__':
    # conn = sqlite3.connect('../database/classtable.db')
    # cursor = conn.cursor()
    # # cursor.execute("SELECT name FROM sqlite_master WHERE type=\'table\' ORDER BY name;")
    # # cursor.execute("PRAGMA table_info(CLASSINFORMATION)")
    # # cursor.execute("select * from sqlite_master where type=\"table\" and name=\"CLASSINFORMATION\";")
    # table = cursor.fetchall()
    # print(table)
    # cursor.close()
    # conn.commit()
    # conn.close()
    control = ControlSqlite('../database/classtable.db')
    tablelist = control.get_tables()
    print(tablelist[0][0])
    columns = control.get_columns(tablelist[0][0])
    print(columns)