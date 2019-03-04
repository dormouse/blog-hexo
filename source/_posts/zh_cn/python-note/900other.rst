Python Note 900 - Other
***********************

:date: 2017-02-13
:modified: 2017-02-13
:slug: python-note-900-other
:tags: python, note
:category: Development
:author: Dormouse Young
:summary: Python note series 900 - other

ConfigParser Usage
==================

Example::

    conf_file = 'conf.ini'
    conf_parser = ConfigParser.ConfigParser()
    conf_parser.read(conf_file)
    conf = {key: value for key, value in conf_parser.items(section_name)}

Deal with INI file
-------------------

基本的文件示例如下::

    [DEFAULT]
    ServerAliveInterval = 45
    Compression = yes
    CompressionLevel = 9
    ForwardX11 = yes

    [bitbucket.org]
    User = hg

    [topsecret.server.com]
    Port = 50022
    ForwardX11 = no

如何生成 INI 文件
------------------
::

    >>> import configparser
    >>> config = configparser.ConfigParser()
    >>> config['DEFAULT'] = {'ServerAliveInterval': '45',
    ...                      'Compression': 'yes',
    ...                      'CompressionLevel': '9'}
    >>> config['bitbucket.org'] = {}
    >>> config['bitbucket.org']['User'] = 'hg'
    >>> config['topsecret.server.com'] = {}
    >>> topsecret = config['topsecret.server.com']
    >>> topsecret['Port'] = '50022'     # mutates the parser
    >>> topsecret['ForwardX11'] = 'no'  # same here
    >>> config['DEFAULT']['ForwardX11'] = 'yes'
    >>> with open('example.ini', 'w') as configfile:
    ...   config.write(configfile)
    ...

使用方法和字典基本一致。

如何读取 INI 文件
------------------

::

    >>> import configparser
    >>> config = configparser.ConfigParser()
    >>> config.sections()
    []
    >>> config.read('example.ini')
    ['example.ini']
    >>> config.sections()
    ['bitbucket.org', 'topsecret.server.com']
    >>> 'bitbucket.org' in config
    True
    >>> 'bytebong.com' in config
    False
    >>> config['bitbucket.org']['User']
    'hg'
    >>> config['DEFAULT']['Compression']
    'yes'
    >>> topsecret = config['topsecret.server.com']
    >>> topsecret['ForwardX11']
    'no'
    >>> topsecret['Port']
    '50022'
    >>> for key in config['bitbucket.org']: print(key)
    ...
    user
    compressionlevel
    serveraliveinterval
    compression
    forwardx11
    >>> config['bitbucket.org']['ForwardX11']
    'yes'

DEFAULT 一节会自动代入到其他节

支持的数据类型
---------------


Config parsers 不猜测数据类型，都是以文本形式保存的。你要自己转换数据类型::

    >>> int(topsecret['Port'])
    50022
    >>> float(topsecret['CompressionLevel'])
    9.0

提供 getboolean() 、 getint() 和 getfloat() 来读取相应的数据类型。
getboolean 比较方便，因为 bool('False') 的结果为 True ::

    >>> topsecret.getboolean('ForwardX11')
    False
    >>> config['bitbucket.org'].getboolean('ForwardX11')
    True
    >>> config.getboolean('bitbucket.org', 'Compression')
    True

更多内容参见：https://docs.python.org/3/library/configparser.html#module-configparser


读取 Excel 文件内容
===================

::

    import xlrd
    workbook = xlrd.open_workbook(filename) #打开文件
    sheetcount = workbook.nsheets #文件内sheet的数量
    sheet = workbook.sheet_by_index(i) #获得某个sheet，第一个sheet索引为0
    rowcount = sheet.nrows #最大行数
    colcount = sheet.ncols #最大列数

交换变量
========

::

    x = 6
    y = 5
    x, y = y, x
    print x
    >>> 5
    print y
    >>> 6

if 语句在行内
=============

::

    print "Hello" if True else "World"

连接
====

下面的最后一种方式在绑定两个不同类型的对象时显得很cool::

    nfc = ["Packers", "49ers"]
    afc = ["Ravens", "Patriots"]
    print nfc + afc
    >>> ['Packers', '49ers', 'Ravens', 'Patriots']
    print str(1) + " world"
    >>> 1 world
    print `1` + " world"
    >>> 1 world
    print 1, "world"
    >>> 1 world
    print nfc, 1
    >>> ['Packers', '49ers'] 1

数字技巧
========

::

    #除后向下取整
    print 5.0//2
    >>> 2
    # 2的5次方
    print 2**5
    >> 32

    #注意浮点数的除法
    print .3/.1
    >>> 2.9999999999999996
    print .3//.1
    >>> 2.0

数值比较
========

::

    x = 2
    if 3 > x > 1:
        print x
    >>> 2
    if 1 < x > 0:
        print x
    >>> 2

60 个字符解决 FizzBuzz
======================

前段时间Jeff Atwood 推广了一个简单的编程练习叫FizzBuzz，问题引用如下：
写一个程序，打印数字1到100，3的倍数打印Fizz来替换这个数，5的倍数打印Buzz，
对于既是3的倍数又是5的倍数的数字打印FizzBuzz。这里就是一个简短的，有意思
的方法解决这个问题::

    for x in range(101):print"fizz"[x%3*4::]+"buzz"[x%5*4::]or x

计数时使用 Counter 对象
=======================

这听起来显而易见，但经常被人忘记。对于大多数程序员来说，数一个东西是一项
很常见的任务，而且在大多数情况下并不是很有挑战性的事情——这里有几种方法
能更简单的完成这种任务。

Python的collections类库里有个内置的dict类的子类，是专门来干这种事情的::

    >>> from collections import Counter
    >>> c = Counter('hello world')
    >>> c
    Counter({'l': 3, 'o': 2, ' ': 1, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})
    >>> c.most_common(2)
    [('l', 3), ('o', 2)]

集合
====

除了python内置的数据类型外，在collection模块同样还包括一些特别的用例，在
有些场合Counter非常实用。如果你参加过在这一年的Facebook HackerCup，你甚至
也能找到他的实用之处::

    from collections import Counter
    print Counter("hello")
    >>> Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

迭代工具
========

和collections库一样，还有一个库叫itertools，对某些问题真能高效地解决。
其中一个用例是查找所有组合，他能告诉你在一个组中元素的所有不能的组合方式::

    from itertools import combinations
    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    for game in combinations(teams, 2):
    print game
    >>> ('Packers', '49ers')
    >>> ('Packers', 'Ravens')
    >>> ('Packers', 'Patriots')
    >>> ('49ers', 'Ravens')
    >>> ('49ers', 'Patriots')
    >>> ('Ravens', 'Patriots')

False == True
=============

比起实用技术来说这是一个很有趣的事，在python中，True和False是全局变量，因此::

    False = True
    if False:
        print "Hello"
    else:
        print "World"
    >>> Hello

创建一次性的、快速的小型web服务
===============================

python 内置模块可以创建 Web 服务:

- For python 3.x : ``python3 -m http.server``

- For python 2.x : ``python -m SimpleHTTPServer``

有时候，我们需要在两台机器或服务之间做一些简便的、很基础的RPC之类的交互。
我们希望用一种简单的方式使用B程序调用A程序里的一个方法——有时是在另一台
机器上。仅内部使用。

我并不鼓励将这里介绍的方法用在非内部的、一次性的编程中。我们可以使用一种
叫做XML-RPC的协议 (相对应的是这个Python库)，来做这种事情。

下面是一个使用SimpleXMLRPCServer模块建立一个快速的小的文件读取服务器的例子::

    from SimpleXMLRPCServer import SimpleXMLRPCServer

    def file_reader(file_name):
        with open(file_name, 'r') as f:
            return f.read()

    server = SimpleXMLRPCServer(('localhost', 8000))
    server.register_introspection_functions()
    server.register_function(file_reader)
    server.serve_forever()

客户端::

    import xmlrpclib
    proxy = xmlrpclib.ServerProxy('http://localhost:8000/')
    proxy.file_reader('/tmp/secret.txt')

漂亮的打印出JSON
================

为了能让JSON数据表现的更友好，我们可以使用indent参数来输出漂亮的JSON。
当在控制台交互式编程或做日志时，这尤其有用::

    >>> import json
    >>> print(json.dumps(data))  # No indention
    {"status": "OK", "count": 2, "results": [{"age": 27, "name": "Oz", "lactose_intolerant": true}, {"age": 29, "name": "Joe", "lactose_intolerant": false}]}
    >>> print(json.dumps(data, indent=2))  # With indention
    {
      "status": "OK",
      "count": 2,
      "results": [
        {
          "age": 27,
          "name": "Oz",
          "lactose_intolerant": true
        },
        {
          "age": 29,
          "name": "Joe",
          "lactose_intolerant": false
        }
      ]
    }

同样，使用内置的pprint模块，也可以让其它任何东西打印输出的更漂亮。


动态生成类的属性
================

正确的操作应该是 ``setattr( A, 'd', 1)`` 或者
``setattr( a1.__class__, 'd', 1)``

要取得模块中的某个属性可以用 ``getattr()`` ，比如::

    c = getattr(m, 'myclass')
    myobject = c()

动态生成类
================

.. IMPORTANT::
    This section is copy from http://www.python8.org/a/fenleiwenzhang/yuyanjichu/2010/1001/566.html

方法一::

    def getObj(name):
        return eval(name+'()')

方法二::

    m = __import__('mymodule')

但是要注意：如果myclass并不在mymodule的自动导出列表中（__all__），
则必须显式地导入，例如::

    m = __import__('mymodule', globals(), locals(), ['myclass'])
    c = getattr(m, 'myclass')
    myobject = c()

实例
----
::

    # 动态生成类
    def create_object(object_attribute):
        class o:
            pass
        if '#class' in object_attribute.keys():
            (module_name, class_name) = object_attribute['#class'].rsplit('.', 1)
            module_meta = __import__(module_name)
            class_meta = getattr(module_meta, class_name)
            o = class_meta()
        for k in object_attribute:
            # maybe should be, need test!!!!:
            # if str(type(object_attribute[k])) == '<type \'dict\'>':
            if str(type(object_attribute[k])) == '<class \'dict\'>':
                setattr(o, k, create_object(object_attribute[k]))
            else:
                setattr(o, k, object_attribute[k])
        return o

example.py::

    class class1:

        def __init__(self):
            pass

        def print1(self):
            print('studio_name:' + str(self.studio))


    class class2:

        def __init__(self):
            pass

        def print2(self):
            print('room:' + str(self.room))


test.py::

    def test():
        dict_object = {"#class": "example.class1",
                       "studio": "demonstudio",
                       "office": {"#class": "example.class2",
                                  "floor": 5,
                                  "room": "501"
                                  }
                       }
        o = create_object(dict_object)
        o.print1()
        o.office.print2()
        print(o.studio)
        print(o.office.floor)

    test()
