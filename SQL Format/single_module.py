# single module
from define import *
import copy


class single_module:
    """
    modifiedby:彭于晏 2019/4/29

    该module做单表查询,完成的工作
    1.无聚合函数的普通列
    2.包含一些聚合函数,比如count,avg,sum,abs关键字,普通列和聚合函数的混合
    3.group by关键字
    4.where关键字

    to do:1.聚合函数只是内置函数的一部分，内置函数的返回可能就不是一个结果
          2.加上之前sql_format的东西,整合成single和mutiply
    """

    def __init__(self, dict):
        """
        :param dict:数据字典,格式如test example
        """
        self.__cols = dict.get('column',None)
        self.__table = dict.get('table',None)
        self.__function = dict.get('function',None)
        self.__group = dict.get('group',None)
        self.__where = dict.get('where',None)
        self.__like = dict.get('like',None)
        self.__connect = dict.get('connect',None)
        self.__orderby = dict.get('order_by',None)

    def splice_sql(self):
        """
            该函数用来选择怎么拼接sql,把每个功能的拼接当成一个模块
            该函数的作用是整合模块
        :return: 最终的sql
        """
        if self.__function is not None:
            # 有聚合函数
            sql = self.naive_aggregation()
        else:
            # 无聚合函数,构建普通列的select
            sql = select_str + blank_str
            for col in self.__cols:
                sql += col + comma_str
            sql = sql[:-1] + blank_str
            sql += from_str + blank_str + self.__table
        if self.__group is not None:
            # 有group by
            sql = self.naive_group(sql)
        if self.__where is not None:
            # 有where
            sql = self.naive_where(sql)
        if self.__orderby is not None:
            sql = self.naive_order(sql)
        return sql

    def naive_aggregation(self):
        """
        :return:format_str 返回最后拼接的sql字符串
        """
        format_str = select_str
        function_list = list(self.__function.keys())
        # select只有一个单独的聚合函数会只返回一个结果,由聚合函数性质决定
        # example:select count(A),count(B) from table_name
        if len(function_list) == 1:
            # format_str example:select count(A)  as cout_num from table_name
            # count可以替换为其他聚合函数
            for col in self.__cols:
                format_str += blank_str + mode_dict[function_list[0]] + left_str + \
                              col + right_str + blank_str + as_str + blank_str + \
                              mode_name[function_list[0]] + comma_str
            # 去掉最后多余的,
            format_str = format_str[:-1]
            format_str += blank_str + from_str + blank_str + self.__table
        # 聚合函数和普通列混杂类型,example:select count(A),sum(B),C from table_name
        else:
            cols = copy.deepcopy(self.__cols)
            for function, index_list in self.__function.items():
                for index in index_list:
                    # 对每个聚合函数,根据指定的列,先对聚合函数影响的列进行迭代拼接
                    format_str += blank_str + mode_dict[function] + left_str + \
                                  self.__cols[index] + right_str + blank_str + \
                                  as_str + blank_str + mode_name[function] + comma_str
                    # 每次remove一个聚合函数影响的列,剩下的为普通列
                    cols.remove(self.__cols[index])
            # 迭代普通列拼接
            for col in cols:
                format_str += blank_str + col + comma_str
            # 去掉最后多余的,
            format_str = format_str[:-1]
            format_str += blank_str + from_str + blank_str + self.__table
        return format_str

    def naive_group(self, from_str):
        """
        该函数用来拼接group by条件
        :param from_str: from之前的所有拼接的字符串
        :return: 加上group之后的字符串
        """
        format_str = from_str + blank_str + group_str
        # 对group by的列迭代拼接
        for index in self.__group:
            format_str += blank_str + self.__cols[index] + comma_str
        # 去掉最后多余的,
        return format_str[:-1]

    def naive_where(self, group_str):
        """
        该函数用来拼接where条件
        :param group_str: 完成group by之后的语句
        :return: 完成where之后的sql
        """
        group_str += blank_str + where_str + blank_str + self.__where[0]['left'] + \
                     blank_str + self.__where[0]['symbol'] + blank_str + \
                     self.__where[0]['right']
        if self.__connect is not None:
            for index, connect in enumerate(self.__connect):
                group_str = self.splice_where(group_str, self.__where[index + 1], connect)
        if self.__like is not None:
            group_str = self.naive_like(group_str)
        return group_str

    def splice_where(self, str, where_item, connect):
        """
        :param str: 拼接的字符串
        :param where_item: 每次拼接的where字典
        :param connect: and,or,or others
        :return: 拼接后的字符串
        """
        str += blank_str + connect + blank_str + where_item['left'] + \
               blank_str + where_item['symbol'] + blank_str + where_item['right']
        return str

    def naive_like(self,str):
        '''
        :param str:拼接的字符串
        :return: 返回完成拼接的like
        '''
        str += blank_str
        for item in self.__like:
            col = self.__cols[item['item']]
            if item['item_type'] == not_str:
                str += col + blank_str + not_str + blank_str + like_str
            else:
                str += col + blank_str + like_str
            if item['like_type'] == "front":
                str += blank_str + quation_str + item['like_condition'] + like_border + quation_str
            if item['like_type'] == "back":
                str += blank_str + quation_str + like_border + item['like_condition'] + quation_str
            if item['like_type'] == "contain":
                str += blank_str + quation_str + like_border + item['like_condition'] +\
                       like_border + quation_str
            str += comma_str
        str = str[:-1]
        return str

    def naive_order(self, str):
        '''
        :param str: 拼接的字符串
        :return: 返回完成拼接的order_by
        '''
        str += blank_str + order_str
        for item in self.__orderby:
            col = self.__cols[item['item']]
            if item['order_type'] == desc_str:
                str += blank_str + col + blank_str + item['order_type'] + comma_str
        str = str[:-1]
        return str



