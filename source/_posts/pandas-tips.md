---
title: Pandas Notes
date: 2021-02-01
modified: 2021-02-01
tags:
 - python
 - pandas
 - dataframe
 - excel
category: Python
author: Dormouse Young
summary: Python Install
---

# Tips

- 合并一个EXCEL 文件中的所有SHEET

```python
df=pd.concat(pd.read_excel(workbook_url,sheet_name=None),ignore_index=True)
```

- 合并一个目录下所有 EXCEL 文件中的所有SHEET

```python
df = pd.concat(
    [pd.concat(pd.read_excel(wb, sheet_name=None), ignore_index=True) for wb in wbs],
    ignore_index=True)
```

- 看列属性

```python
df.dtypes
```

<!-- more -->

- 分类计数

```python
gp = df[df['时间']>'2021-01-18'].groupby('目的地')
gp['姓名'].count()
```

- 数据透视

```python
pd.pivot_table(
    df0118,
    index=['区'],
    values=['姓名'],
    columns=['分类'],
    aggfunc=[len],
    fill_value=0)
```

- 按规定行和列输出

```python
df = pd.DataFrame(
    np.arange(12).reshape((4,3)),
    columns=['c','a','b'],index=['D','B','C','A'])
```

- 根据条件新建列并赋值

```python
df['some_col'] = df['one_col'].apply(lambda x: x if len(x) == 18 else None)
```

- 修改列名
```python
df.rename(columns={'a':'A','b':'B'},inplace=True)
df.rename(str.lower, axis='columns')
df.columns = ['A', 'B']
```

# 日期时间

- 从日期属性中提取年月日

```python
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
```

- 只保留日期，不要时间，即把日期置为0点

```python
df['日期'] = pd.to_datetime(df['开始日期'].dt.date)
# OR
df['日期'] = df['开始日期'].dt.normalize()
```

- 按照指定格式打印时间，注意类型会由 `datetime64[ns]` 变为 `object`

```python
df['dd'].dt.strftime("%Y-%m-%d")
```

- 给日期加一天

```python
df['two_date'] = df['one_date'] + datetime.timedelta(days=1)
```

1. dt.date 和 dt.normalize()，他们都返回一个日期的 日期部分，即只包含年月日。但不同的是date返回的Series是object类型的，normalize()返回的Series是datetime64类型的。
1. dt.year、dt.month、dt.day、dt.hour、dt.minute、dt.second、dt.week (dt.weekofyear和dt.week一样)分别返回日期的年、月、日、小时、分、秒及一年中的第几周
1. dt.weekday（dt.dayofweek一样）返回一周中的星期几，0代表星期一，6代表星期天，dt.weekday_name返回星期几的英文。
1. dt.dayofyear 返回一年的第几天，dt.quarter得到每个日期分别是第几个季度。
1. dt.is_month_start和dt.is_month_end 判断日期是否是每月的第一天或最后一天，可以将month换成year和quarter相应的判断日期是否是每年或季度的第一天或最后一天.
1. dt.is_leap_year 判断是否是闰年
1. dt.month_name() 返回月份的英文名称.

# 字符串

## 替换

* str.replace():替换字符串

Series.str.replace(pat, repl, n=- 1, case=None, flags=0, regex=None)

Replace each occurrence of pattern/regex in the Series/Index.

Equivalent to str.replace() or re.sub(), depending on the regex value.

## 去空白

* str.strip():删除左右两侧的空白（开始/结束）
* str.lstrip():删除左侧空白
* str.rstrip():删除右侧空白

## 大小写変换

* str.lower():转换为小写
* str.upper():转换为大写
* str.capitalize():将第一个字母转换为大写，将其他字母转换为小写
* str.title():将单词的首字母转换为大写，其余转换为小写
将描述每个示例。
