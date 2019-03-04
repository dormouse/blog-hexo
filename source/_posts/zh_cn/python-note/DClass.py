#!/usr/bin/python
# -*- coding: utf8 -*-
"""
动态生成类的属性
================

正确的操作应该是：
setattr( A, 'd', 1)
或者
setattr( a1.__class__, 'd', 1)

如果要取得模块中的一个属性的话:可以用getattr(),比如:
c = getattr(m, 'myclass')
myobject = c()

动态生成类
================

方法一
------
def getObj(name):
    return eval(name+'()')

方法二
------

m = __import__('mymodule')
但是要注意：如果myclass并不在mymodule的自动导出列表中（__all__），
则必须显式地导入，例如：
m = __import__('mymodule', globals(), locals(), ['myclass'])
c = getattr(m, 'myclass')
myobject = c()
"""

# 动态生成类


def create_object(object_attribute):
    class o:
        pass
    if '#class' in object_attribute.keys():
        (module_name, class_name) = object_attribute['#class'].rsplit('.', 1)
        module_meta = __import__(module_name)
        class_meta = getattr(module_meta, class_name)
        o = class_meta()
    for k in object_attribute:
        # maybe should be, need test!!!!:
        # if str(type(object_attribute[k])) == '<type \'dict\'>':
        if str(type(object_attribute[k])) == '<class \'dict\'>':
            setattr(o, k, create_object(object_attribute[k]))
        else:
            setattr(o, k, object_attribute[k])
    return o

==========
example.py
==========

class class1:

    def __init__(self):
        pass

    def print1(self):
        print('studio_name:' + str(self.studio))


class class2:

    def __init__(self):
        pass

    def print2(self):
        print('room:' + str(self.room))


==========
test.py
==========

def test():
    dict_object = {"#class": "example.class1",
                   "studio": "demonstudio",
                   "office": {"#class": "example.class2",
                              "floor": 5,
                              "room": "501"
                              }
                   }
    o = create_object(dict_object)
    o.print1()
    o.office.print2()
    print(o.studio)
    print(o.office.floor)

test()
