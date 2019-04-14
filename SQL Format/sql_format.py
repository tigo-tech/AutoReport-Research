import pymysql

select_str = "SELECT"
from_str = "FROM"
group_str = "GROUP BY"
order_str = "ORDER BY"
blank_str = " "
comma_str = ","
as_str = "AS"
t_str = "t"
left_str = "("
right_str = ")"
join_str = "JOIN"
on_str = "ON"
all_str = "*"
equal_str = "="

def base_step(input_arr):
    #input_arr 输入表名及列名
    #循环生成语句 eg: SELECT col_1, col_2 FROM table_1
    #返回生成语句
    format_str = select_str
    for it in input_arr[:-2]:
        format_str += blank_str + it+comma_str
    format_str += blank_str +input_arr[-2]
    format_str += blank_str + from_str + blank_str + input_arr[-1]
    return format_str


def join_step(query_1, query_2, n, col_1, col_2,input_arr1,input_arr2):
    #query_n 为base_step生成的语句,
    #参数n代表第n次join
    #col_n为join on参数中需要的两张表的列名
    #input_arrn 为join两张表的所有列名的array
    #format_n 为标准化语句，format结束后eg:(SELECT col_1,col_2 FROM table_1) AS tn
    #select_col 为select * from join结果（去除一列关联的列名），避免形成duplicate column name
    #join_end 形成最终的join查询语句
    format_1 = left_str + query_1
    format_2 = left_str + query_2
    table_1 = t_str+str(2*n-1)+"."
    table_2 = t_str+str(2*n)+"."
    format_1 += blank_str + right_str + blank_str + as_str +blank_str+ t_str + str(2 * n - 1)
    format_2 += blank_str + right_str + blank_str + as_str +blank_str+ t_str + str(2 * n)
    join_mid = format_1 +blank_str+ join_str +blank_str +format_2
    select_col = ""
    select_output = []
    for i in input_arr1:
        if i != col_1:
            select_output.append(i)
            select_col += table_1+i+comma_str+blank_str
    for i in input_arr2:
        if i != col_2:
            select_output.append(i)
            select_col += table_2 + i+comma_str+blank_str
    select_col += table_1+col_1
    select_output.append(col_1)
    join_end = select_str +blank_str + select_col+blank_str + from_str +join_mid +blank_str+ on_str +blank_str+ table_1+col_1 +blank_str + equal_str +table_2+col_2
    print(join_end)
    return select_output,join_end


if __name__ == '__main__':
    #input_n 用户输入的各张表及想要的列名，eg:["col_1","col_2","table_1"]
    #input_coln input_n中除去表名
    join_num = 2
    n = 1
    input_1 = ["userId", "regionId", "user"]
    input_2 = ["regionName","regionId","region"]
    input_3 = ["userId","sellNum","sell"]
    input_col1 = input_1[:-1]
    input_col2 = input_2[:-1]
    input_col3 = input_3[:-1]
    query_1 = base_step(input_1)
    query_2 = base_step(input_2)
    out_put_1,join_1 = join_step(query_1,query_2,n,"regionId","regionId",input_col1,input_col2)
    n +=1
    query_3 = base_step(input_3)
    out_put2,join_2 = join_step(join_1,query_3,n,"userId","userId",out_put_1,input_col3)
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd="970115", db='test')
    cur = conn.cursor()
    cur.execute(join_2)
    for r in cur:
        print(r)