Python Note 600 - Functional Programming
========================================


:date: 2017-02-13
:modified: 2017-02-13
:slug: python-note-600-functional-programming
:tags: python, note, functional-programming
:category: Development
:author: Dormouse Young
:summary: Python note series 600 - functional-programming


lambda
-------

lambda 语句中，冒号前是参数，可以有多个，用逗号隔开，冒号右边的返回值。
lambda 语句构建是一个函数对象::

    In [1]: f = lambda x: x * 2

    In [2]: f(8)
    Out[2]: 16

    In [3]: f
    Out[3]: <function __main__.<lambda>>

filter
-------

filter(function or None, sequence) -> list, tuple, or string

返回序列中 function(item) 为 true 的项目。如果 fuction 为 None ，那么就返回
测试结果为 true 的项目。如果序列的类型为 tuple 或者 string ，那么返回相同的
类型；其他的则返回 list::

    In [4]: foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

    In [5]: filter(lambda x: x % 3 == 0, foo)
    Out[5]: [18, 9, 24, 12, 27]

map
----

map(function, sequence[, sequence, ...]) -> list

返回一个 list ，其内容为把序列中的每一个值作为函数的参数得到的函数的返回值::

    In [6]: map(lambda x: x * 2 + 10, foo)
    Out[6]: [14, 46, 28, 54, 44, 58, 26, 34, 64]

如果使用序列，那么函数会把每个序列相应的值作为参数，序列长度不够的则会以
None 来补充::

    In [1]: lista = [1, 2, 3, 4, 5]
    In [2]: listb = [1] * 4
    In [3]: map(lambda x,y:"%s|%s"%(x,y), lista, listb)
    Out[3]: ['1|1', '2|1', '3|1', '4|1', '5|None']

如果 function 为 None ，那么返回一个由序列项目组成的 list （如果是多个序列，
那么返回一个 list ， 其每个项目为由每个序列相应项目组成的 tuple::

    In [9]: nfc = ["Packers", "49ers"]

    In [10]: afc = ["Ravens", "Patriots"]

    In [11]: map(None, nfc, afc)
    Out[11]: [('Packers', 'Ravens'), ('49ers', 'Patriots')]

reduce
-------

reduce(function, sequence[, initial]) -> value

Apply a function of two arguments cumulatively to the items of a sequence,
from left to right, so as to reduce the sequence to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
of the sequence in the calculation, and serves as a default when the
sequence is empty::

    In [9]: reduce(lambda x, y: x + y, foo)
    Out[9]: 139

reduce 函数在 python3 中已经不属于 build-in 了，而是在 functools 模块下，
如需使用，需要从functools模块中引入。

