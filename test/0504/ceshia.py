# -*- coding: utf-8 -*-
# @Author: ChenYuan
# @Date  : 2020/5/4 14:54
class Test():
    def __init__(self,age,name):
        self.age = age
        self.name = name

    def des(self):
        print('你的儿子多大年纪了？{}岁'.format(self.age))

    def jieshao(self):
        print('#' * 10)

    def jieshu(self):
        print('结束了,heihie')

t = Test(18,'dada')
t.des()
t.jieshu()

