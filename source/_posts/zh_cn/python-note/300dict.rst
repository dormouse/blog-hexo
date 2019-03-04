Python Note 300 - Dict
**********************

:date: 2017-02-13
:modified: 2017-02-13
:slug: python-note-300-dict
:tags: python, note, dict
:category: Development
:author: Dormouse Young
:summary: Python note series 300 - dict


字典推导
========

和列表推导类似，字典同样可以推导::

    teams = ["Packers", "49ers", "Ravens", "Patriots"]
    print {key: value for value, key in enumerate(teams)}
    >>> {'49ers': 1, 'Ravens': 2, 'Patriots': 3, 'Packers': 0}

从字典中获取元素
================

使用字典的 get 方法可以安全的获得字典的值，第二个参数是缺省值::

    data = {'user': 1, 'name': 'Max', 'three': 4}
    is_admin = data.get('admin', False)

在 Dictionary 中元素分组
========================

和上面类似，先创建 Persons::

    class Person(object):
        def __init__(self, age):
            self.age = age

persons = [Person(age) for age in (78, 14, 78, 42, 14)]
如果现在我们要按照年龄分组的话，一种方法是使用 in 操作符::

    persons_by_age = {}

    for person in persons:
        age = person.age
        if age in persons_by_age:
            persons_by_age[age].append(person)
        else:
            persons_by_age[age] = [person]

    assert len(persons_by_age[78]) == 2

相比较之下，使用 collections 模块中 defaultdict 方法的途径可读性更好::

    from collections import defaultdict
    persons_by_age = defaultdict(list)
    for person in persons:
        persons_by_age[person.age].append(person)

defaultdict 将会利用接受的参数为每个不存在的 key 创建对应的值，这里我们传递的是 list，所以它将为每个 key 创建一个 list 类型的值。
假如需要建立嵌套的defaultdict，d = defaultdict(defaultdict)行不通，正确的方法是d = defaultdict(lambda :defaultdict(int))。

list 转 dict
============

将 ['1:a','2:b','3:c'] 转换为 {'1′: 'a', '3′: 'c', '2′: 'b'}::

    dict(item.split(':')[:2] for item in b)

dict 转 class
=============

方法如下::

    class Struct:
        def __init__(self, **entries):
            for k, v in entries.items():
                if isinstance(v, dict):
                    entries[k] = Struct(**v)
                    print entries[k]
            self.__dict__.update(entries)


        if __name__ == '__main__':
            args = {'a': {'cola': ['xm', 'xb']},
                    'b': 2}
            s = Struct(**args)
            print s.a
            print s.a.cola
            print s.b

