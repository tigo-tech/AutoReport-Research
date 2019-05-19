from single_module import *

if __name__ == "__main__":
    # run test for single module
    a = single_module({'column': ['A', 'B', 'C', 'D'],
                       'function': {'count': [0, 1], 'sum': [2, 3]},
                       # 'function': {},
                       'table': 'user',
                       'group': [0, 1, 2],
                       'where': [{'symbol': '=',
                                  'left': 'user.id',
                                  'right': 'sell.id',
                                  },
                                 {'symbol': '=',
                                  'left': 'user.id',
                                  'right': '舔狗们',
                                  },
                                 {'symbol': '=',
                                  'left': 'user.id',
                                  'right': '张世俊',
                                  },
                                 {'symbol': '=',
                                  'left': 'user.id',
                                  'right': '张建顺',
                                  }
                                 ],
                       'connect': ['and', 'or', 'and'],
                       'order_by': [{'item':'age',
                                     'order_type':""
                                     },
                                    {'item': 'grade',
                                     'order_type':asc_str
                                    }],
                       'like': [{'item':'name',
                                 'item_type':not_str,
                                 'like_type':'front',
                                 'like_condition':'张'
                                 },
                                {'item': 'name',
                                 'item_type':"",
                                 'like_type':'back',
                                 'like_condition':'张'
                                 },
                                {'item': 'name',
                                 'item_type':"",
                                 'like_type':'contain',
                                 'like_condition':'张'
                                 }
                                ]
                       })
    print(a.splice_sql())
