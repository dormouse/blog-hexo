---
title: Python 与 JSON 共舞
auto_excerpt:
  enable: true
  length: 150
tags:
- python
- json
---

# 简介

在 Python 开发中，尤其是在涉及 web 开发时，不可避免会与 [JSON （JavaScript Object Notation）](http://json.org) 打交道。本文主要尝试介绍如何在 Python 中使用 JSON 。

在 Python 3 的官方文档中关于 JSON 操作的函数主要有 4 个，它们分别是 `json.dump()` 、 `json.load()` 、 `json.dumps()` 和`json.loads()` 。 `json.dump()` 和 `json.dumps()` 的功能是将 Python 对象进行编码（ encoder ） ，转化为 JSON 格式；而 `json.load()` 和 `json.loads()` 则反之，对 JSON 格式对象解码（ ecoder ），转化为 Python 对象。
<!-- more -->

# json.dump() 与 json.dumps() 的区别

`json.dump()` 与 `json.dumps()` 的作用都是把 Python 对象序列化为 JSON 格式，不同之处在哪里呢？先来看一下两者的定义：

``` python
json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
```

两者的定义基本相同，但是 `json.dump()` 多了一个 `fp` 参数。它们的主要区别是： `json.dumps()` 把 Python 对象序列化为一个 JSON 格式的字符串，而 `json.dump()` 则是把 Python 对象序列化为一个 JSON 格式的流，这个流可以直接写入到文件或者类似文件的对象。

听起来可能有一些拗口，下面来看个例子：

``` bash
>>> import json
>>> person = {"name":"dormouse", "age":40}
>>> json.dumps(person)
'{"name": "dormouse", "age": 40}'
>>> type(json.dumps(person))
<class 'str'>
```

从上例中可以看出， `json.dumps()` 返回了一个 JSON 格式的字符串。

``` bash
>>> from pathlib import Path
>>> with Path("/tmp/person.txt").open('w') as fp:
...     json.dump(person, fp)
```

上例中的代码生成一个名为 `/tmp/person.txt` 的文件，其内容为： `{"name": "dormouse", "age": 40}` 。

`json.load()` 与 `json.loads()` 的区别与之类似。

# 编码

把 Python 对象序列化为 JSON 格式对象称为编码，主要使用 `json.dump()` 和 `json.dumps()` 函数。根据前文所述，这两个函数基本相同，下面主要以 `json.dumps()` 函数为例，`json.dump()` 函数的用法基本类似。

`json.dumps()` 用法示例：

``` bash
>>> import json
>>> person = {"name":"dormouse", "age":40, "blog":["blog1", "其他"]}
>>> json.dumps(person)
'{"name": "dormouse", "age": 40, "blog": ["blog1", "\\u5176\\u4ed6"]}'
```

编码数据类型对应规则如下表：

| Python                                 | JSON   |
| -------------------------------------- | ------ |
| dict                                   | object |
| list, tuple                            | array  |
| str                                    | string |
| int, float, int- & float-derived Enums | number |
| True                                   | true   |
| False                                  | false  |
| None                                   | null   |

## 常用参数

`json.dumps()` 和  `json.dump()` 可以使用许多参数，下面介绍几个常用的参数：

### ensure_ascii 参数

该参数如默认值是 `True` ，在编码时，非 ASCII 字符会被转义，例如在上文的例子中，“其他”两个字被编码为 `\\u5176\\u4ed6` 。如果该参数设置为 `Fasle` ，
那么就不会转义。例如：

``` bash
>>> json.dumps(person, ensure_ascii=False)
'{"name": "dormouse", "age": 40, "blog": ["blog1", "其他"]}'
```

### indent 参数

该参数控制编码结果的缩进，默认值是 `None` 。默认情况下会编码结果会紧缩在一起。如果该参数设置为一个正整数或者 `\t` ，那么会使编码结果具有更好的可读性。
例如：

``` bash
>>> print(json.dumps(person, ensure_ascii=False, indent=4))
{
    "name": "dormouse",
    "age": 40,
    "blog": [
        "blog1",
        "其他"
    ]
}
```
### sort_keys 参数

该参数控制编码结果是否按键值排序，默认值是 `False` 。如果该参数设置为 `Ture` ，那么编码结果的字典的键值会进行排序。示例：

``` bash
>>> print(json.dumps(person, ensure_ascii=False, indent=4, sort_keys=True))
{
    "age": 40,
    "blog": [
        "blog1",
        "其他"
    ],
    "name": "dormouse"
}
```

更多参数请参阅：[Python 3 的官方文档][Python 3 的官方文档]

# 解码

把 JSON 格式对象转换为 Python 对象称为解码，主要使用 `json.load()` 和 `json.loads()` 函数。这两个函数基本相同，区别类似于 `json.dump()` 和 `json.dumps()` 函数。下面主要以 `json.loads()` 函数为例，`json.load()` 函数的用法基本类似。

`json.loads()` 用法示例：

``` bash
>>> json.loads(json.dumps(person))
{'name': 'dormouse', 'age': 40, 'blog': ['blog1', '其他']}
```

解码数据类型对应规则如下表：

| JSON          | Python |
| ------------- | ------ |
| object        | dict   |
| array         | list   |
| string        | str    |
| number (int)  | int    |
| number (real) | float  |
| true          | True   |
| false         | False  |
| null          | None   |

# 自定义类型处理

有时候，我们需要处理一些自定义的类型，例如有如下这个类：

``` python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "x:{}, y:{}".format(self.x, self.y)
```

当我们要对其实例进行编码时会产生类似如下异常（文件路径有所省略）：

``` bash
>>> person = {
...    "name":"dormouse",
...    "point": Point(1,2)
}
>>> json.dumps(person)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File ".../lib/python3.6/json/__init__.py", line 231, in dumps
    return _default_encoder.encode(obj)
  File ".../lib/python3.6/json/encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File ".../lib/python3.6/json/encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File ".../lib/python3.6/json/encoder.py", line 180, in default
    o.__class__.__name__)
TypeError: Object of type 'Point' is not JSON serializable
```

产生异常的原因是 JSON 默认的方法无法对这种 Python 对象进行编码。那么如何解决这个问题呢？主要有两种方法：

## 使用函数

``` python
def my_default(o):
    """ 自定义编码函数 """
    if isinstance(o, Point):
        return (o.x, o.y)
def my_hook(t):
    """ 自定义解码函数 """
    for k in t:
        if k == 'point':
            x, y = t[k]
            t[k] = Point(x, y)
    return t

# 编码
encode_str = json.dumps(person, default=my_default)
print(encode_str)
# 解码
decode_obj = json.loads(encode_str, object_hook=my_hook)
print(decode_obj)
```

输出结果如下：

``` python
{"name": "dormouse", "point": [1, 2]}
{'name': 'dormouse', 'point': x:1, y:2}
```

## 使用类

``` python
class MyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Point):
            return (o.x, o.y)
        return json.JSONEncoder.default(o)
encode_str = json.dumps(person, cls=MyEncoder)
print(encode_str)

class MyDecoder(json.JSONDecoder):
    def decode(self, s):
        t = super().decode(s);
        for k in t:
            if k == 'point':
                x, y = t[k]
                t[k] = Point(x, y)
        return t
decode_obj = json.loads(encode_str, cls=MyDecoder)
print(decode_obj)
```

输出结果如下：

``` python
{"name": "dormouse", "point": [1, 2]}
{'name': 'dormouse', 'point': x:1, y:2}
```



# 参考资料

1. [Python 3 的官方文档][Python 3 的官方文档]



注：

本文的 Python 环境为：

Python 3.6.2 |Continuum Analytics, Inc.| (default, Jul 20 2017, 13:51:32)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux

[Python 3 的官方文档]: https://docs.python.org/3/library/json.html
