# single module
from define import *


class single_module:
    def __init__(self, input):
        self.__cols = input[:-1]
        self.__table = input[-1]

    def naive_aggregation(self, mode):
        format_str = select_str
        select_output = []
        if len(self.__cols) == 1:
            # format_str += LIKE " COUNT(columnName) AS count_num " OR AVG OR SUM OR others
            format_str += blank_str + mode_dict[mode] + left_str + \
                self.__cols[0] + right_str + blank_str + as_str + blank_str + \
                mode_name[mode]+blank_str+from_str + blank_str+self.__table
        else:
            for it in self.__cols[:-1]:
                # format_str += " columnName1, columnName2, ..."
                format_str += blank_str + it + comma_str
            # format_str += LIKE " COUNT(columnName) AS count_num " OR AVG OR SUM OR others
            format_str += blank_str + mode_dict[mode] + left_str + \
                self.__cols[-1] + right_str + blank_str + \
                as_str + blank_str + mode_name[mode]
            # format_str += "  FROM tableName"
            format_str += blank_str + from_str + blank_str + \
                self.__table
            cols_output, format_str = self.naive_group(format_str, mode)
        return cols_output, format_str

    def naive_group(self, from_str, mode):
        cols_output = []
        format_str = from_str + blank_str + group_str
        for it in self.__cols[:-2]:
            cols_output.append(it)
            format_str += blank_str + it + comma_str
        format_str += blank_str + self.__cols[-2]
        cols_output.append(mode_dict[mode])
        return cols_output, format_str

    def naive_where(self,conditions):
        # simple where 
        pass

if __name__ == "__main__":
    #run test for single module
    a = single_module(["regionId","gender","user"])
    print(a.naive_aggregation(1)[1])