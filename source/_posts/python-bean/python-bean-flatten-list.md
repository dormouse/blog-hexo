---
title: 【Python茴香豆系列】之 拍扁列表
date: 2021-02-01
modified: 2021-02-01
permalink: python-bean-flatten-list
tags:
 - python
 - list
category: Python 茴香豆
author: Dormouse Young
summary: Python Bean - flatten list
---


用 Python 编程，使用不同的方法来完成同一个目标，有时候是一件很有意思的事情。这让我想起鲁迅笔下的孔乙己。孔乙己对于茴香豆的茴字的四种写法颇有研究。我不敢自比孔乙己，这里搜集一些 Python 的茴香豆，以飨各位码农。

假设有一个列表：`source_list = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]` ，要求把这个列表拍扁，变成：`[1, 2, 3, 4, 5, 6, 7, 8, 9]` 。

这里我们先做一点准备工作：

```python
import functools
import itertools
import numpy
import operator

source_list = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
```

# 茴香豆一： for for

如果第一次面对这种问题，可能首先想到的就是 for ，基本的思路如下：

```python
>>> flatten_list = []
>>> for sublist in source_list:
>>>    for item in sublist:
>>>        flatten_list.append(item)
>>> flatten_list
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

嗯，工作完成。

当然，如果你熟悉列表的推导的话，上面的一堆可以浓缩成：

```python
[item for sublist in source_list for item in sublist]
```
<!-- more -->

# 茴香豆二： sum

python 有一个内置函数 sum ，这个函数本来是用来给我们做算术的，恰巧列表也是可以求和的，因此下面这句也能用：

```python
sum(source_list, [])
```

numpy 也有类型的功能的 sum ，效果相同：

```python
numpy.sum(numpy.array(source_list, dtype=object))
```

# 茴香豆三： numpy

numpy 还有专业拼接数组的工具，可以用来大炮打蚊子：

```python
list(numpy.concatenate(source_list))
```

# 茴香豆四： numpy

多个东东变成一个东东，这不能不让我怀念起 reduce 的好：

```python
functools.reduce(lambda x,y: x+y, source_list)
functools.reduce(operator.concat, source_list)
functools.reduce(operator.iconcat, source_list, [])
```

殊途同归，以上三条语句实现了同样的效果。

# 茴香豆五： chain

遇到列表的问题，高手们一般会亮出 chain ，以区别于一般俗手：

```python
list(itertools.chain(*source_list))
list(itertools.chain.from_iterable(source_list))
```

# 茴香豆六： flatten

最后，请大家不要小看这个问题，但凡玩列表的，估计总有一天会遇到这个问题，不然前辈高人不会造这么多轮子的：

```python
from pandas.core.common import flatten
list(flatten(source_list))

from matplotlib.cbook import flatten
list(flatten(source_list))

from setuptools.namespaces import flatten
list(flatten(source_list))
```
