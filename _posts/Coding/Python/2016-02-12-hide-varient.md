---
layout: post
title: 高度隐藏对象的属性
date: 2016-02-12 06:43:10
categories: Coding
tags: Python
---

这是Stackoverflow看到的一个问题:[Python private instance data revisited](http://stackoverflow.com/questions/35333721/python-private-instance-data-revisited), 挺有意思的.

-----

有以下一段一个类:

~~~python
import codecs

class Secret:
    def __private():
        secret_data = None

        def __init__(self, string):
            nonlocal secret_data
            if secret_data is None:
                secret_data = string

        def getSecret(self):
            return codecs.encode(secret_data, 'rot_13')

        return __init__, getSecret

    __init__, getSecret = __private()
~~~

在这个类里面, 通过一个函数将对象的属性藏在函数的局部变量内,调用时可以简单加密处理. 而类的方法也通过这个函数在对象构建时来构建. 这样, 初始化方法所调用的对象"属性"其实也是藏在这个函数的内部. Python是无法真正实现隐藏属性等变量的. 所以问题来了, **怎么查看这个secret_data的真实值呢?**

如果按以下操作:

~~~python
>>> thing = Secret("gibberish")
>>> thing.getSecret()
'tvoorevfu'
>>> dir(thing)
['_Secret__private', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'getSecret']
~~~

你是看不到里面的属性的.

我尝试过对`_Secret__private`进行`__function__`来调出类函数, `__dir__`, `__dict__`查看内容,不成功,空白. 主要是对象生成时动态生成的值, 在内存某处, 查看类的是无效的. 也尝试过对对象进行类似操作, 因为是局部变量, 也是查看不出来的, 藏得有点深了.

### 解法

SOF里面高手就是多! 给了两个解法:

#### 通过查看闭包`__closure__`

闭包介绍可以查看[wiki](https://zh.wikipedia.org/wiki/%E9%97%AD%E5%8C%85_(%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6)). 通过查看函数闭包就可以查看这个隐藏的变量! Python果然是无法真正隐藏啊~~

~~~python
thing = Secret("gibberish")
# __init__ doesn't need to be used here; anything defined within the closure will do
thing.__init__.__func__.__closure__[0].cell_contents
# following just test:
thing.__init__.__func__.__closure__
>>> (<cell at 0x102775558: str object at 0x1027e3430>,)
~~~

这里是通过初始化函数的函数对象的闭包分析(用`cell_contents`才能查看, 否则得到是个`cell`对象的描述). 这个cell对象在Cpython可以通过ctype来解释和重新设置 (里面介绍了这个[帖子](https://dzone.com/articles/nothing-private-python)):

~~~python
import ctypes
...

thing = Secret("gibberish")
cell = ctypes.py_object(thing.__init__.__func__.__closure__[0])
new_value = ctypes.py_object('whatever')
ctypes.pythonapi.PyCell_Set(cell, new_value)

thing.getSecret()
~~~

OK, 通过闭包和ctypes来解PyCell就可以实现对藏在闭包内东西的查看和设置了~ 学习了~

#### 通过inspect模块

~~~python
>>> thing = Secret("gibberish")
>>> thing.getSecret()
'tvoorevfu'
>>> import inspect
>>> inspect.getclosurevars(thing.getSecret).nonlocals['secret_data']
'gibberish'
>>> inspect.getclosurevars(thing.__init__).nonlocals['secret_data']
'gibberish'
~~~

这种方法其实也是通过对闭包的分析, 使用`inspect`模块的`getclosurevars`来查看闭包对象的内容, 需要指明变量名. 另外也不能实现设置.

------
