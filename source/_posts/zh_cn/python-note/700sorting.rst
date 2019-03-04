Python Note 700 - Sorting
*************************

:date: 2017-02-13
:modified: 2017-02-13
:slug: python-note-700-sorting
:tags: python, note, sorting
:category: Development
:author: Dormouse Young
:summary: Python note series 700 - sorting


本文基于 Python 2.7.6 [GCC 4.8.2] on linux2 。

Python 中排序常用的有 sort 和 sorted 。
首先来看看定义::

    >>> help(list.sort)
    Help on method_descriptor:

    sort(...)
        L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
        cmp(x, y) -> -1, 0, 1

    >>> help(sorted)
    Help on built-in function sorted in module __builtin__:

    sorted(...)
        sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list

    sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list

从定义中可以看出两者有以下区别：

* sort 只能用于列表，而 sorted 不仅可以用于列表，还可以用于其他可迭代对象。
* sort 会改变列表本身，而 sorted 不会改变可迭代对象本身，而是返回一个新的列表。

http://blog.csdn.net/qins_superlover/article/details/44340447

http://www.cnblogs.com/linyawen/archive/2012/03/15/2398302.html

http://www.cfanz.cn/?c=article&a=read&id=204633
