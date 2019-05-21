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
distin_str = "DISTINCT"
where_str = "WHERE"
desc_str = "DESC"
like_str = "LIKE"
like_border = "%"
not_str = "NOT"
quation_str = "\'"

aggregation_str = {
    "count_str": "COUNT",
    "avg_str": "AVG",
    "sum_str": "SUM",
    "max_str": "MAX",
    "min_str": "MIN",
}

aggregation_name = {
    "count_num": "cout_num",
    "avg_num": "avg_num",
    "sum_num": "sum_num",
    "max_num": "max_num",
    "min_num": "min_num",
}

# mode_dict = {
#     1: aggregation_str["count_str"],
#     2: aggregation_str["avg_str"],
#     3: aggregation_str["sum_str"],
#     4: aggregation_str["max_str"],
#     5: aggregation_str["min_str"],
# }

# mode_name = {
#     1: aggregation_name["count_num"],
#     2: aggregation_name["avg_num"],
#     3: aggregation_name["sum_num"],
#     4: aggregation_name["max_num"],
#     5: aggregation_name["min_num"],
# }

mode_dict = {
    'count': aggregation_str["count_str"],
    'avg': aggregation_str["avg_str"],
    'sum': aggregation_str["sum_str"],
    'max': aggregation_str["max_str"],
    'min': aggregation_str["min_str"],
}
mode_name = {
    'count': aggregation_name["count_num"],
    'avg': aggregation_name["avg_num"],
    'sum': aggregation_name["sum_num"],
    'max': aggregation_name["max_num"],
    'min': aggregation_name["min_num"],
}
