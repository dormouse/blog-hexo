---
title: 【Python茴香豆系列】之 PANDAS 如何根据列的值来选取 DataFrame 的行
date: 2021-03-12
modified: 2021-03-12
tags:
 - python
 - pandas
 - dataframe
 - row
category: Python 茴香豆
authors:
  - Dormouse Young
summary: Python Bean - select rows from dataframe base on columns value
toc: true
---


用 Python 编程，使用不同的方法来完成同一个目标，有时候是一件很有意思的事情。
这让我想起鲁迅笔下的孔乙己。孔乙己对于茴香豆的茴字的四种写法颇有研究。我不
敢自比孔乙己，这里搜集一些 Python 的茴香豆，以飨各位码农。

```sql
SELECT *
FROM table_name
WHERE column_name = value
```

上面的 SQL 语句可以用来在数据库中根据字段的值选取符合条件的记录，那么在 DataFrame 中如何根据列的值来选取行呢？

本文测试数据来源：https://raw.github.com/pandas-dev/pandas/master/pandas/tests/io/data/csv/tips.csv

```python
>>> import pandas as pd
>>> import numpy as np
>>> df = pd.read_csv('tips.csv')
>>> df.head()
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
```

## 茴香豆一： []索引

最直观的方法是通过逻辑条件来筛选行。 在逻辑条件中，等于用 `==` ，不等于用 `!=` ，还有 `>` 、 `<` 、 `>=` 和 `<=` 。 多个条件组合的情况下，与用 `&` ， 或用 `|` ，非用 `~` 。 是否在某个范围内用 `isin` 。 示例如下：

```python
>>> mask = [False] * 244
>>> mask[1] = True
>>> mask[3] = True
>>> df[mask]
   total_bill   tip   sex smoker  day    time  size
1       10.34  1.66  Male     No  Sun  Dinner     3
3       23.68  3.31  Male     No  Sun  Dinner     2

>>> # 选取性别为男性的行
>>> df[df['sex'] == 'Male'].head()
   total_bill   tip   sex smoker  day    time  size
1       10.34  1.66  Male     No  Sun  Dinner     3
2       21.01  3.50  Male     No  Sun  Dinner     3
3       23.68  3.31  Male     No  Sun  Dinner     2
5       25.29  4.71  Male     No  Sun  Dinner     4
6        8.77  2.00  Male     No  Sun  Dinner     2

>>> # 选取小费超过 2 ，或者性别为女性的行
>>> df[(df['tip']>2) | (df['sex']=='Female')].head()
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
5       25.29  4.71    Male     No  Sun  Dinner     4
```
<!-- more -->

## 茴香豆二： 标签索引

标签索引接受布尔数组作为输入，所以使用行索引的标签可以筛选行。

```python
>>> # 选取性别为男性的行
>>> df.loc[df['sex'] == 'Male'].head()
   total_bill   tip   sex smoker  day    time  size
1       10.34  1.66  Male     No  Sun  Dinner     3
2       21.01  3.50  Male     No  Sun  Dinner     3
3       23.68  3.31  Male     No  Sun  Dinner     2
5       25.29  4.71  Male     No  Sun  Dinner     4
6        8.77  2.00  Male     No  Sun  Dinner     2

>>> # 选取小费超过 2 ，或者性别为女性的行
>>> df.loc[(df['tip']>2) | (df['sex']=='Female')].head()
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
5       25.29  4.71    Male     No  Sun  Dinner     4

>>> # 选择不是周末，且小费大于 5 的行
>>> df.loc[~df['day'].isin(['Sun', 'Sat']) & (df['tip']>5)]
     total_bill   tip     sex smoker   day   time  size
85        34.83  5.17  Female     No  Thur  Lunch     4
88        24.71  5.85    Male     No  Thur  Lunch     2
141       34.30  6.70    Male     No  Thur  Lunch     6
```

## 茴香豆三： 位置索引

位置索引接受布尔数组作为输入，所以使用行索引的位置可以筛选行。

```python
>>> mask = list(df['sex'] == 'Male')
>>> df.iloc[mask].head()
   total_bill   tip   sex smoker  day    time  size
1       10.34  1.66  Male     No  Sun  Dinner     3
2       21.01  3.50  Male     No  Sun  Dinner     3
3       23.68  3.31  Male     No  Sun  Dinner     2
5       25.29  4.71  Male     No  Sun  Dinner     4
6        8.77  2.00  Male     No  Sun  Dinner     2
```

## 茴香豆四： 调用函数

以上三种索引都可以使用函数，函数你懂的。

```python
>>> df[lambda df: df['tip']>5].head()
    total_bill   tip     sex smoker  day    time  size
23       39.42  7.58    Male     No  Sat  Dinner     4
44       30.40  5.60    Male     No  Sun  Dinner     4
47       32.40  6.00    Male     No  Sun  Dinner     4
52       34.81  5.20  Female     No  Sun  Dinner     4
59       48.27  6.73    Male     No  Sat  Dinner     4
```

## 茴香豆五： query

这个嘛，熟悉 SQL 的一定喜欢。

```python
>>> # 选取小费超过 2 ，或者性别为女性的行
>>> df.query('tip>2 | sex=="Female"').head()
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
5       25.29  4.71    Male     No  Sun  Dinner     4

>>> # 选择不是周末，且小费大于 5 的行
>>> # @可以引用当前环境中的变量
>>> weekday = ['Sun', 'Sat']
>>> df.query('day not in @weekday & tip>5')
     total_bill   tip     sex smoker   day   time  size
85        34.83  5.17  Female     No  Thur  Lunch     4
88        24.71  5.85    Male     No  Thur  Lunch     2
141       34.30  6.70    Male     No  Thur  Lunch     6
```

## 茴香豆六： where

where 可以把不符合条件的变为 NaN，然后来一个 dropna 吧。

```python
>>> df.where(df.tip>5).dropna().head()
    total_bill   tip     sex smoker  day    time  size
23       39.42  7.58    Male     No  Sat  Dinner   4.0
44       30.40  5.60    Male     No  Sun  Dinner   4.0
47       32.40  6.00    Male     No  Sun  Dinner   4.0
52       34.81  5.20  Female     No  Sun  Dinner   4.0
59       48.27  6.73    Male     No  Sat  Dinner   4.0
```

选择行的方法五花八门，这里只是列出一些关于单索引 DataFrame 的砖头而已，见笑了。详细的文档还是请移步：https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html
