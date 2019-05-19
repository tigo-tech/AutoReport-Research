import pymysql

def create_table():
    sql = """
    CREATE TABLE USER1 (
    id INT auto_increment PRIMARY KEY ,
    name CHAR(20) NOT NULL,
    amount INT,
    price INT,
    sale INT,
    date DATE NOT NULL
    )ENGINE=innodb DEFAULT CHARSET=utf8;
    """
    return sql

def insert_table():
    pass

if __name__ == '__main__':
    conn = pymysql.connect(host='127.0.0.1', user='root',
                           passwd="970115", db='test')
    cur = conn.cursor()
    cur.execute(create_table())
    for r in cur:
        print(r)