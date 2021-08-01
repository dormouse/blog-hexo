---
title: Python Note 600 - Functional Programming
author: Dormouse Young
category: Development
date: 2017-02-13
modified: 2019-03-17
tags:
 - python
 - note
 - functional-programming
---

# lambda

lambda 语句中，冒号前是参数，可以有多个，用逗号隔开，冒号右边的返回值。 lambda 语句构建是一个函数对象:

```python
In [1]: f = lambda x: x * 2

In [2]: f(8)
Out[2]: 16

In [3]: f
Out[3]: <function __main__.<lambda>(x)>
```

<!-- more -->
# filter

## python2

filter(function or None, sequence) -> list, tuple, or string

返回序列中 function(item) 为 true 的项目。如果 fuction 为 None ，那么就返回 测试结果为 true 的项目。如果序列的类型为 tuple 或者 string ，那么返回相同的 类型；其他的则返回 list

## python3

filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true.

```python
In [4]: foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
   ...: list(filter(lambda x: x % 3 == 0, foo))
Out[4]: [18, 9, 24, 12, 27]
```

# map

## python 2

map(function, sequence[, sequence, …]) -> list

返回一个 list ，其内容为把序列中的每一个值作为函数的参数得到的函数的返回值

## python 3

map(func, *iterables) --> map object

Make an iterator that computes the function using arguments from each of the iterables.  Stops when the shortest iterable is exhausted.

```python
In [5]: list(map(lambda x: x * 2 + 10, foo))
Out[5]: [14, 46, 28, 54, 44, 58, 26, 34, 64]
```

在 python 2 中，如果使用序列，那么函数会把每个序列相应的值作为参数，序列长度不够的则会以 None 来补充。 在 python 3 中，如果函数使用的参数有多个可迭代对象，那么以最短的那个为准。

```python
list_a = [1, 2, 3, 4, 5]
list_b = [1] * 4
list(map(lambda x,y:"%s|%s"%(x,y), list_a, list_b))
Out[6]: ['1|1', '2|1', '3|1', '4|1']
```

# reduce

reduce 函数在 python3 中已经不属于 build-in 了，而是在 functools 模块下，需要从functools模块中引入。

reduce(function, sequence[, initial]) -> value

Apply a function of two arguments cumulatively to the items of a sequence,from left to right, so as to reduce the sequence to a single value.For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).  If initial is present, it is placed before the itemsof the sequence in the calculation, and serves as a default when thesequence is empty.

```python
In [7]: from functools import reduce
   ...: reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
Out[7]: 15
```

# partial

partial函数可用来修改函数的默认参数值，增加额外的位置参数（positional arguments）或名称参数（ named arguments），你不需再重新定义函数，只需像使用原函数一样的使用partial包裹后的函数。

```python
In [8]: from functools import partial

In [9]: def add(a,b):
   ...:     return a+b
   ...:     

In [10]: add(1,3)
Out[10]: 4

In [11]: plus1 = partial(add, 1)

In [12]: plus1(3)
Out[12]: 4

In [13]: plus3 = partial(add, 3)

In [14]: plus3(7)
Out[14]: 10
```

用途：

在 pyqt 中，控件的 `connect` 函数只接受函数名，不接受函数参数，这种情况下就可以使用 `partial` ：


```python
from functools import partial
button.clicked.connect(partial(self.btn_clicked, name))
def btn_clicked(self, name):
    if name == 'some_a':
        # do some a
    if name == 'some_b':
        # do some b

```

参考：https://blog.csdn.net/xdfyoga1/article/details/80517108
