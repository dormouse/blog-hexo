---
title: 【Python茴香豆系列】之 PANDAS 获取 DataFrame 的行数
date: 2021-02-03
modified: 2021-02-03
permalink: python-bean-count-dataframe-row
tags:
 - python
 - pandas
 - dataframe
 - row
category: Python 茴香豆
author: Dormouse Young
summary: Python Bean - count row of pandas dataframe
---


用 Python 编程，使用不同的方法来完成同一个目标，有时候是一件很有意思的事情。这让我想起鲁迅笔下的孔乙己。孔乙己对于茴香豆的茴字的四种写法颇有研究。我不敢自比孔乙己，这里搜集一些 Python 的茴香豆，以飨各位码农。

一共有多少条数据？这大概是数据分析工作最基本的内容吧。
这里，我们来聊一聊如何获取 Pandas 中 DataFrame 的行数。
首先准备一个用于测试的 DataFrame 。这个 DataFrame 有 3 列，名称分别为 a 、 b 和 c ：

```python
>>> import numpy as np
>>> import pandas as pd
>>> df = pd.DataFrame({'a':[None,2,3], 'b':[4,5,6], 'c':[7,8,9]})
>>> df
     a  b  c
0  NaN  4  7
1  2.0  5  8
2  3.0  6  9
```

# 茴香豆一： count 

SQL 语句有一个 `SELECT count (*) FROM some_table` ，
DataFrame 同样有一个 `count` 函数可以用来计数，示例如下：

```python
>>> df['a'].count()
2
```

等等，怎么会是 2 ？结果应该是三才对啊！原来， `count` 会把 `NaN` 剔除， a 列中有 `NaN` ，所以结果不对，我们看看 b 列就对了：

```python
>>> df['b'].count()
3
```

可是，我们不能保证每一次碰到的 b 列都没有空值啊，于是我们自己造一列出来：

```python
>>> df['aa'] = 1
>>> df
     a  b  c  aa
0  NaN  4  7   1
1  2.0  5  8   1
2  3.0  6  9   1
>>> df['aa'].count()
3
```

好吧，至此，任务勉强完成了，但是......有一点丑陋。

<!-- more -->


# 茴香豆二： shape

经过艰苦卓绝的学习，我发现 DataFrame 有一个 shape 函数。这是一个奇妙的函数，示例如下：

```python
>>> df.shape
(3, 3)
```
于是，这样就可以得到结果了：

```python
>>> df.shape[0]
3
```

厉害吧，神奇吧。
但是 shape 得到的是两个数字，我们只要一个数字，在这里，是不是有点浪费呢？

# 茴香豆三： len

Python 有一个内置的 len ，一般来说，内置的东西总是高级一点。我们来试试：

```python
>>> len(df)
3
```

那么这个 len 背后又是什么呢？在 IPython 中检查一下：

```python
In [1]: df.__len__??
Signature: df.__len__() -> int
Source:
    def __len__(self) -> int:
        """
        Returns length of info axis, but here we use the index.
        """
        return len(self.index)
```

上面的 shape 又是什么呢？


```python
In [2]: df.shape??
Type:        property
Source:
# df.shape.fget
@property
def shape(self) -> Tuple[int, int]:
    """
    Return a tuple representing the dimensionality of the DataFrame.
    ......
    """
    return len(self.index), len(self.columns)
```

# 茴香豆四： index

从以上两个源代码可以看出，我们应当这样使用 len ：

```python
>>> len(df.index)
3
```

# 茴香豆五： 再来三个

山外青山楼外楼， Python 永远还有茴香豆。再来三个：

```python
df.index.size
len(df.axes[0])
df.pipe(len)
```
