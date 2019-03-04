Python Note 200 - List
**********************

:date: 2017-02-13
:modified: 2017-02-13
:slug: python-note-200-list
:tags: python, note, list
:category: Development
:author: Dormouse Young
:summary: Python note series 200 - list


列表推导（过滤）
================

以过滤偶数为例，一般方法::

    numbers = [1,2,3,4,5,6]
    even = []
    for number in numbers:
        if number%2 == 0:
            even.append(number)

推导方式过滤::

    numbers = [1,2,3,4,5,6]
    even = [number for number in numbers if number%2 == 0]

倒序列表
========

::

    >>> lst = [1, 2, 3, 4, 5]
    >>> lst.reverse()
    >>> lst
    [5, 4, 3, 2, 1]

::

    >>> a = [1,2,3]
    >>> a[::-1]
    [3, 2, 1]

::

    >>> lst = [1, 2, 3, 4, 5]
    >>> list(reversed(lst))
    [5, 4, 3, 2, 1]

判断一个列表是否为空
====================

::

    if mylist:
        # Do something with my list
    else:
        # The list is empty

排序
====

列表排序有两种方式，一种是列表自带的方式 sort，一种是内建函数 sorted 。
复杂的数据类型可通过指定 key 参数进行排序。
由字典构成的列表，根据字典元素中的 age 字段进行排序::

    items = [{'name': 'Homer', 'age': 39},
             {'name': 'Bart', 'age': 10},
             {"name": 'cater', 'age': 20}]
    items.sort(key=lambda item: item.get("age"))
    print(items)

    >>> [{'age': 10, 'name': 'Bart'}, {'age': 20, 'name': 'cater'}, {'age': 39, 'name': 'Homer'}]

sort 方法用于对原列表进行重新排序，指定 key 参数，key 是匿名函数，
item 是列表中的字典元素，我们根据字典中的age进行排序，默认是按升序排列，
指定 reverse=True 按降序排列::

    items.sort(key=lambda item: item.get("age"), reverse=True)

    >>> [{'name': 'Homer', 'age': 39}, {'name': 'cater', 'age': 20}, {'name': 'Bart', 'age': 10}]

如果不希望改变原列表，而是生成一个新的有序列表对象，那么可以内置函数 sorted ，
该函数返回新列表::

    items = [{'name': 'Homer', 'age': 39},
             {'name': 'Bart', 'age': 10},
             {"name": 'cater', 'age': 20}]
    new_items = sorted(items, key=lambda item: item.get("age"))
    print(items)

    >>> [{'name': 'Homer', 'age': 39}, {'name': 'Bart', 'age': 10}, {'name': 'cater', 'age': 20}]

    print(new_items)
    >>> [{'name': 'Bart', 'age': 10}, {'name': 'cater', 'age': 20}, {'name': 'Homer', 'age': 39}]


同时迭代两个列表
================

::

    nfc = ["Packers", "49ers"]
    afc = ["Ravens", "Patriots"]
    for teama, teamb in zip(nfc, afc):
        print teama + " vs. " + teamb
    >>> Packers vs. Ravens
    >>> 49ers vs. Patriots

带索引的列表迭代
================

::

    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    for index, team in enumerate(teams):
        print index, team
    >>> 0 Packers
    >>> 1 49ers
    >>> 2 Ravens
    >>> 3 Patriots

    enumerate 还可以指定元素的第一个元素从几开始，默认是0，也可以指定从1开始：

    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    for index, team in enumerate(teams, start=1):
        print index, team
    >>> 1 Packers
    >>> 2 49ers
    >>> 3 Ravens
    >>> 4 Patriots

初始化列表的值
==============

::

    items = [0]*3
    print items
    >>> [0,0,0]

列表转换为字符串
================

::

    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    print ", ".join(teams)
    >>> 'Packers, 49ers, Ravens, Patriots'

获取列表的子集
==============

有时，你只需要列表中的部分元素，这里是一些获取列表子集的方法::

    x = [1,2,3,4,5,6]
    #前3个
    print x[:3]
    >>> [1,2,3]
    #中间4个
    print x[1:5]
    >>> [2,3,4,5]
    #最后3个
    print x[3:]
    >>> [4,5,6]
    #奇数项
    print x[::2]
    >>> [1,3,5]
    #偶数项
    print x[1::2]
    >>> [2,4,6]

获取两个列表的差
================

示例::

    >>> lista = [1,3,5,7,9,1]
    >>> listb = [1,2,5]
    >>> list(set(lista)-set(listb))
    [9, 3, 7]

拷贝一个列表
============

第一种方法::

    new_list = old_list[:]

第二种方法::

    new_list = list(old_list)

第三种方法::

    import copy
    # 浅拷贝
    new_list = copy.copy(old_list)
    # 深拷贝
    new_list = copy.deepcopy(old_list)

移除列表中的元素
================

删除列表中的元素有三种方式

remove 移除某个元素，而且只能移除第一次出现的元素::

    >>> a = [0, 2, 2, 3]
    >>> a.remove(2)
    >>> a
    [0, 2, 3]

    # 如果要移除的元素不在列表中，则抛出 ValueError 异常
    >>> a.remove(7)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: list.remove(x): x not in list·

del 根据指定的位置移除某元素::

    >>> a = [3, 2, 2, 1]
    # 移除第一个元素
    >>> del a[1]
    [3, 2, 1]

    # 当超出列表的下表索引时，抛出IndexError的异常
    >>> del a[7]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list assignment index out of range

pop 与 del 类似，但是 pop 方法可以返回移除的元素::

    >>> a = [4, 3, 5]
    >>> a.pop(1)
    3
    >>> a
    [4, 5]

    # 同样，当超出列表的下表索引时，抛出IndexError的异常
    >>> a.pop(7)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: pop index out of range


连接两个列表
============

::

    listone = [1, 2, 3]
    listtwo = [4, 5, 6]

    mergedlist = listone + listtwo

    print(mergelist)
    >>>
    [1, 2, 3, 4, 5, 6]

随机获取列表中的某个元素
========================
::

    import random
    items = [8, 23, 45, 12, 78]

    >>> random.choice(items)
    78
    >>> random.choice(items)
    45
    >>> random.choice(items)
    12
