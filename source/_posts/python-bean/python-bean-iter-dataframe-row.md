---
title: 【Python茴香豆系列】之 PANDAS 如何遍历 DataFrame 的所有行
date: 2021-02-05
modified: 2021-02-05
tags:
 - python
 - pandas
 - dataframe
 - row
category: Python 茴香豆
author: Dormouse Young
summary: Python Bean - iter dataframe rows
---


用 Python 编程，使用不同的方法来完成同一个目标，有时候是一件很有意思的事情。这让我想起鲁迅笔下的孔乙己。孔乙己对于茴香豆的茴字的四种写法颇有研究。我不敢自比孔乙己，这里搜集一些 Python 的茴香豆，以飨各位码农。

首先准备一个函数，用来生成用于测试的 DataFrame 。这个 DataFrame 有 3 列，名称分别为 a 、 b 和 c 。

```python
>>> import numpy as np
>>> import pandas as pd

>>> df = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6], 'c':[7,8,9]})
>>> df
   a  b  c
0  1  4  7
1  2  5  8
2  3  6  9
```

BOSS 的要求是把每一行的 a ， b 打印出来，例如：

```
1 4
2 5
3 6
```

# 茴香豆一： iterrows

DataFrame 有一个函数，专门就是用来遍历所有的行的：

```python
>>> for index, row in df.iterrows():
>>>    print(row['a'], row['b'])
1 4
2 5
3 6
```

这个函数简单明了，似乎不错，但是有一个致命的弱点：一般情况下会比较慢，在行数较多的情况下，那个什么，会怀疑人生。

<!-- more -->

# 茴香豆二： itertuples

iterrows 有一个兄弟 itertuples ，可以把 DataFrame 变成 namedtuples ，这样速度上就更快了。

```python
>>> for row in df.itertuples(index=True, name='hxd'):
>>>    print(row.a, row.b)
1 4
2 5
3 6
```

当然金无足赤，在使用的时候也有要注意的地方，最主要的是当 DataFrame 的列名称有 Python 保留字的时候，列名会被自动转变，例如：

```python
>>> df = pd.DataFrame({'in':[1,2,33], 'b':[4,5,6], 'c':[7,8,9]})
>>> for row in df.itertuples(name='hxd'):
>>>    print(row)
hxd(Index=0, _1=1, b=4, c=7)
hxd(Index=1, _1=2, b=5, c=8)
hxd(Index=2, _1=33, b=6, c=9)
```
这个例子中， `in` 是 Python 的保留字，被自动变更为 `_1` 。


# 茴香豆三： iloc

这个有点，嗯，大拙若巧吧。

```python
>>> for i in range(0, len(df)):
>>>    print (df.iloc[i]['a'], df.iloc[i]['b'])
1 4
2 5
3 6
```


# 茴香豆四： to_***

DataFrame 有很多 `to_` 开头的函数，通过这些函数可以把 DataFrame 转换成其他形式，然后再加以处理，这样就可以衍生出许许多多的方法，例如：

```python
>>> for row in df.to_dict(orient='records'):
>>>    print(row['a'], row['b'])
```

当然， DataFrame 还有各种各样的 to_ 开头的方法，有兴趣的朋友可以尝试一下。

# 茴香豆五： 不遍历

其实对于 BOSS 的要求，有时候我们要学会说不。当然如何说不，是一门手艺，不在本文的范围之内。

如果只是要显示 DataFrame 的内容，那么如下的方式就足够了：

```python
>>> print(df[['a', 'b']].to_string(index=False, header=False))
1  4
2  5
3  6
```

如果要对每一行数据进行计算，那么应当使用 Pandas 提供的函数或者运算方法，而不是去遍历每一行数据。这是因为 Pandas 的函数是向量化的，其处理效率远高于遍历。示例如下：

```python
df = pd.DataFrame(np.random.randn(100000, 4), columns=list('abcd'))
timeit [row.a + row.b for row in df.itertuples(index=False)]
72 ms ± 1.01 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
timeit [x+y for x,y in zip(df['a'], df['b'])]
20.3 ms ± 132 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
timeit df['a'] + df['b']
1.27 ms ± 83.2 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

从以上示例可以看出，遍历是最慢的，列表推导其次， pandas 自带的是最快的。
其实道理也很简单，专业的事交给专业的人去做，不要作。
