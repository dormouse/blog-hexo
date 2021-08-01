---
title: 【Python茴香豆系列】之 PANDAS 变更列的类型
date: 2021-03-26
modified: 2021-03-26
tags:
 - python
 - pandas
 - dataframe
 - column
category: Python 茴香豆
author: Dormouse Young
summary: Python Bean - how to change the type of pandas dataframe column 
---

用 Python 编程，使用不同的方法来完成同一个目标，有时候是一件很有意思的事情。这让我想起鲁迅笔下的孔乙己。孔乙己对于茴香豆的茴字的四种写法颇有研究。我不敢自比孔乙己，这里搜集一些 Python 的茴香豆，以飨各位码农。

首先准备一个函数，用来生成用于测试的 DataFrame 。这个 DataFrame 有 3 列，名称分别为 a 、 b 和 c 。

```python
>>> import numpy as np
>>> import pandas as pd
```

## 茴香豆一： to_numeric()

这个函数可以把 scalar 、 list 、tuple 、 1-d array 或者 Series 类型的数据转换为数字类型的数据。
默认根据输入的参数返回 `float64` 或者 `int64` 类型。

把一个序列转换为数字，序列中的数据的数据类型不要求一致。

```python
>>> s = pd.Series(["1", 2, "3"])
>>> pd.to_numeric(s)
0    1
1    2
2    3
dtype: int64
```

生成一个有三个列的示例 DataFrame

```python
>>> df = pd.DataFrame({
...     'a':['1','2','3'],
...     'b':[4,'5.0',6],
...     'c':['7',8,9]})
>>> df.dtypes
a    object
b    object
c    object
dtype: object
```

转换所有的列

```python
>>> df.apply(pd.to_numeric).dtypes
a      int64
b    float64
c      int64
dtype: object
```
<!-- more -->

只转换 a 列和 b 列

```python
>>> df[["a", "b"]] = df[["a", "b"]].apply(pd.to_numeric)
>>> df.dtypes
a      int64
b    float64
c     object
dtype: object
```

`to_numeric` 的函数原型是 `to_numeric(arg, errors='raise', downcast=None)` 。 `errors` 可以控制类型转换中的出错处理。详细内容参见文档。
类似类型的函数还有 `to_datetime()` 和 `to_timedelta()` 。

## 茴香豆二： astype()

Dataframe 和 Series 的实例均有 astype 方法，可用于类型转换。

```python
>>> s = pd.Series(["1", 2, "3"])
>>>s.astype(int)
0    1
1    2
2    3
dtype: int64

>>> df = pd.DataFrame({
...     'a':['1','2','3'],
...     'b':[4,'5.0',6],
...     'c':['7',8,9]})
>>> df.astype('int32', errors='ignore').dtypes
a    object
b    object
c    object
dtype: object

>>> df.astype({'a': 'int32'}).dtypes
a     int32
b    object
c    object
dtype: object
```

`astype` 方法的定义是 `astype(dtype, copy: bool = True, errors: str = 'raise')` ，详细内容参见文档。

## 茴香豆三： infer_objects()

此方法的作用是尝试把 object 类型的列转换为更合适的类型，于 0.21.0 版本新增。示例：

```python
>>> df = pd.DataFrame({"A": ["a", 1, 2, 3],
...                    "B": ["a", 1, 2.0, 3]})
>>> df.dtypes
A    object
B    object
dtype: object

>>> df = df.iloc[1:]
>>> df.infer_objects().dtypes
A      int64
B    float64
dtype: object
```

## 茴香豆四： convert_dtypes()

此方法的作用是尝试把列的数据类型转换为更合适的类型，于 1.0.0 版本新增。官方示例：

```python
>>> df = pd.DataFrame(
...     {
...         "a": pd.Series([1, 2, 3], dtype=np.dtype("int32")),
...         "b": pd.Series(["x", "y", "z"], dtype=np.dtype("O")),
...         "c": pd.Series([True, False, np.nan], dtype=np.dtype("O")),
...         "d": pd.Series(["h", "i", np.nan], dtype=np.dtype("O")),
...         "e": pd.Series([10, np.nan, 20], dtype=np.dtype("float")),
...         "f": pd.Series([np.nan, 100.5, 200], dtype=np.dtype("float")),
...     }
... )

>>> df
   a  b      c    d     e      f
0  1  x   True    h  10.0    NaN
1  2  y  False    i   NaN  100.5
2  3  z    NaN  NaN  20.0  200.0
```

新建一个 DataFrame ，默认的 dtype 如下：

```python
>>> df.dtypes
a      int32
b     object
c     object
d     object
e    float64
f    float64
dtype: object
```

把类型转换为最优解。

```python
>>> dfn = df.convert_dtypes()
>>> dfn
   a  b      c     d     e      f
0  1  x   True     h    10    NaN
1  2  y  False     i  <NA>  100.5
2  3  z   <NA>  <NA>    20  200.0

>>> dfn.dtypes
a      Int32
b     string
c    boolean
d     string
e      Int64
f    float64
dtype: object
```

新建一个字符串组成的 Series ，缺失的数据用 ``np.nan`` 表示。

```python
>>> s = pd.Series(["a", "b", np.nan])
>>> s
0      a
1      b
2    NaN
dtype: object
```

得到一个 dtype 为 ``StringDtype`` 的 Series 。

```python
>>> s.convert_dtypes()
0       a
1       b
2    <NA>
dtype: string
```