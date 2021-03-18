---
title: 【Python茴香豆系列】之 PANDAS 修改 DataFrame 列名
date: 2021-01-29
modified: 2021-01-29
permalink: python-bean-modify-dataframe-column-name
tags:
 - python
 - pandas
 - dataframe
 - column
category: Python 茴香豆
author: Dormouse Young
summary: Python Bean - modify name of pandas dataframe column 
---


用 Python 编程，使用不同的方法来完成同一个目标，有时候是一件很有意思的事情。这让我想起鲁迅笔下的孔乙己。孔乙己对于茴香豆的茴字的四种写法颇有研究。我不敢自比孔乙己，这里搜集一些 Python 的茴香豆，以飨各位码农。

首先准备一个函数，用来生成用于测试的 DataFrame 。这个 DataFrame 有 3 列，名称分别为 a 、 b 和 c 。


```python
>>> import pandas as pd
>>> def get_df():
>>>    return pd.DataFrame({'a':[1,2,3], 'b':[4,5,6], 'c':[7,8,9]})
>>> get_df()
   a  b  c
0  1  4  7
1  2  5  8
2  3  6  9
```

# 茴香豆一： columns 属性

有一天， BOSS 说要把 DataFrame 的列名都改为大写。于是我简单粗暴地是把一个 List 丢给了 DataFrame 的 columns 属性，任务完成。示例如下：

```python
>>> df = get_df()
>>> df.columns=['A','B','C']
>>> df
   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9
```

<!-- more -->

# 茴香豆二： columns.str

有一天， BOSS 给我一个有 300 列的 DataFrame ，说要把列名都改为大写。显然，使用上面的方法是浪费生命的。于是我使用了 columns.str 。示例如下：


```python
>>> df = get_df()
>>> df.columns = df.columns.str.upper()
>>> df
   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9
```

# 茴香豆三： rename 方法1

有一天， BOSS 给我一个有 300 列的 DataFrame ，说要把列 a 改名为 A ，列 c 改名为 C ，其他列不变。于是我使用了 rename 方法。示例如下：


```python
>>> df = get_df()
>>> df.rename(columns={'a': 'A', 'c': 'C'})
   A  b  C
0  1  4  7
1  2  5  8
2  3  6  9
```

rename 方法有个 inplace 参数，默认值为 False 。上例中， df 并没有改变。


```python
>>> df
   a  b  c
0  1  4  7
1  2  5  8
2  3  6  9
```

如果要改变的话，需要设置 inplace 为 True 。


```python
>>> df.rename(columns={'a': 'A', 'c': 'C'}, inplace=True)
>>> df
   A  b  C
0  1  4  7
1  2  5  8
2  3  6  9
```


# 茴香豆四： rename 方法2

当然，也可以使用函数，例如：


```python
>>> df.rename(columns=lambda x:x.upper())
   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9
```


# 茴香豆五： rename 方法3

这里不使用 columns 参数，例如：


```python
>>> df.rename(str.upper, axis=1)
   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9
```

rename 是一个好东西，详细的用法参见：[官方文档](
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.htmlm) 。
那么使用 rename 有什么好处呢？举个例子吧：


```python
>>> df = get_df()
>>> df.T.rename(columns=lambda x:x+1).T
   a  b  c
1  1  4  7
2  2  5  8
3  3  6  9
```

# 茴香豆六： 删除再添加

如果在心情特别开心的情况下，我也许可能会考虑：


```python
>>> df = get_df()
>>> for k, v in {'a': 'A','b': 'B', 'c': 'C'}.items():
...     df[v] = df.pop(k)
...
>>> df
   A  B  C
0  1  4  7
1  2  5  8
2  3  6  9
```
