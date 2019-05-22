# muti module
from single_module import *


class muti_module:
    """
    modifiedby:彭于晏 2019/5/22

    该module做多表嵌套(join)查询

    """

    def __init__(self, data):
        self.__data = data
        self.__root = self.create_trees(data)

    def naive_join(self):
        node = self.__root
        while node is not None:
            while node is not None:
                if node.lchild is not None:
                    node = node.lchild
            if node.parent.rchild is not None:
                single_module()

    def create_trees(self, data):
        '''
            构建二叉生成树
        :return:
        '''
        tree = Tree(data)
        return tree.root


class Node:
    def __init__(self, data=-1, lchild=None, rchild=None, parent=None):
        self.lchild = lchild  # 表示左子树
        self.rchild = rchild  # 表示右子树
        self.data = data  # 表示数据域
        self.parent = parent


class Tree:
    def __init__(self, data):
        self.root = Node(data=data[-1])
        data.pop()
        if data is not None:
            layer = int(len(data) / 2)
            node = self.root
            for i in range(layer, 0, -1):
                node.lchild = Node(data=data[i * 2 - 2], parent=node)
                node.rchild = Node(data=data[i * 2 - 1], parent=node)
                node = node.lchild
