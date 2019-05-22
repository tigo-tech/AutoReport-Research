from single_module import *
from muti_module import *

if __name__ == "__main__":
    a = single_module({'column': ['A'],
                       'table': 'user',
                       })
    b = single_module({'column': ['B'],
                       'table': 'user',
                       })
    c = single_module({'column': ['C'],
                       'table': 'user',
                       })
    d = single_module({'column': ['D'],
                       'table': 'user',
                       })
    T1 = T2 = T3 = {}
    data = [a, b, T1, c, T2, d, T3]
    muti = Tree(data)
