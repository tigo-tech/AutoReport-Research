from single_module import *
from sqlite_control import ControlSqlite
def test_case():
    control = ControlSqlite("../database/classtable.db")
    table = control.get_tables()
    column = control.get_columns(table[0][0])
    module = single_module({
        'column':column,
        'table':table[0][0],
        'function':{'count':[1]},
        'where':[{
            'symbol':'=',
            'left':column[2],
            'right':"\'Matlab语言\'"
        }],
    })
    sql = module.splice_sql()
    print(sql)
    results = control.execute(sql)
    for result in results:
        print(result)


if __name__ == "__main__":
    test_case()





    # # run test for single module
    # a = single_module({'column': ['A', 'B', 'C', 'D'],
    #                    'function': {'count': [0, 1], 'sum': [2, 3]},
    #                    # 'function': {},
    #                    'table': 'user',
    #                    'group': [0, 1, 2],
    #                    'where': [{'symbol': '=',
    #                               'left': 'user.id',
    #                               'right': 'sell.id',
    #                               },
    #                              {'symbol': '=',
    #                               'left': 'user.id',
    #                               'right': '舔狗们',
    #                               },
    #                              {'symbol': '=',
    #                               'left': 'user.id',
    #                               'right': '张世俊',
    #                               },
    #                              {'symbol': '=',
    #                               'left': 'user.id',
    #                               'right': '张建顺',
    #                               }
    #                              ],
    #                    'connect': ['and', 'or', 'and'],
    #                    'order_by': [{'item': 2,
    #                                  'order_type':""
    #                                  },
    #                                 {'item': 3,
    #                                  'order_type':desc_str
    #                                 }],
    #                    'like': [{'item': 0,
    #                              'item_type':not_str,
    #                              'like_type':'front',
    #                              'like_condition':'张'
    #                              },
    #                             {'item': 1,
    #                              'item_type':"",
    #                              'like_type':'back',
    #                              'like_condition':'张'
    #                              },
    #                             {'item': 0,
    #                              'item_type':"",
    #                              'like_type':'contain',
    #                              'like_condition':'张'
    #                              }
    #                             ]
    #                    })
    # print(a.splice_sql())
