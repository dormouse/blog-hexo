---
title: 【Python茴香豆系列】之 字典合并
date: 2021-01-31
modified: 2021-01-31
tags:
 - python
 - dict
category: Python 茴香豆
author: Dormouse Young
summary: Python Bean - update dict
---


用 Python 编程，使用不同的方法来完成同一个目标，有时候是一件很有意思的事情。这让我想起鲁迅笔下的孔乙己。孔乙己对于茴香豆的茴字的四种写法颇有研究。我不敢自比孔乙己，这里搜集一些 Python 的茴香豆，以飨各位码农。

假设有字典 x 和字典 y ， BOSS 需要把他们合并，生成一个新的字典 z ， x 和 y 保持不变。要实现的效果如下：

```python
x = {'a': 1, 'b': 2}
y = {'b': 8, 'c': 9}
```

经过处理后

```python
z = {'a': 1, 'b': 8, 'c': 9}
```

作为一个超级初学者，可能的做法是：


```python
>>> x = {'a': 1, 'b': 2}
>>> y = {'b': 8, 'c': 9}
>>> z = {}
>>> for k, v in x.items():
        z[k] = v
>>> for k, v in y.items():
        z[k] = v
>>> z
{'a': 1, 'b': 8, 'c': 9}
```

任务完成！
但是，这样的解法显然是不入孔乙己法眼的，于是开始数茴香豆。

<!-- more -->

# 茴香豆一： update

如果你的 Python 版本小于等于 3.4 ，那么如下方法应该是最常见的：

```python
>>> z = x.copy()
>>> z.update(y)
>>> z
{'a': 1, 'b': 8, 'c': 9}
```

# 茴香豆二： 两个小星星

如果你已经完全抛弃了 2 ，并且 Python 版本已经大于等于 3.5 ，那么可以这样：

```python
>>> z = {**x, **y}
>>> z
{'a': 1, 'b': 8, 'c': 9}
```

# 茴香豆三： 一条竖杠

什么？你的 Python 版本已经大于等于 3.9 了？好吧：

```python
>>> z = x | y
>>> z
{'a': 1, 'b': 8, 'c': 9}
```

# 茴香豆四： ChainMap

ChainMap 可能对大多数开发者来说有点陌生，其特点是：“先入为主”，所以要注意两个字典的顺序。

```python
>>> from collections import ChainMap
>>> z = dict(ChainMap(y, x))
>>> z
{'a': 1, 'b': 8, 'c': 9}
```

# 茴香豆五： Dict

Dict 是个好东西，下面是一些示例。但是，本人并不推荐使用。

为什么？不够优雅。

```python
>>> z = dict(x, **y)  # 仅限于字典的 Key 均为 string 时有效
>>> z = dict(x.items() + y.items())  # Python 2
>>> z = dict(x.items() | y.items())
```
