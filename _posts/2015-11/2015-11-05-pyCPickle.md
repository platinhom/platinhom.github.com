---
layout: post
title: Python:序列化模块pickle和cpickle
date: 2015-11-05 12:33:03
categories: Coding
tags: Python
---

Python的序列化是指把**变量**从内存中变为可以储存/传输的数据/文件的过程. 在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

在Python中最基础的实现序列化的两个模块是`cPickle`和`pickle`模块, 功能基本一样, 前者是C写的更快, 后者是python写的会慢点. 一般优先使用cPickle. 这里只介绍cPickle, 一般用其四个函数也就OK了, pickle包含了类和另外一些内容, 更多细节可以看ref1.

~~~python
try:
    import cPickle as pickle
except ImportError:
    import pickle
~~~

## dump 导出数据(序列化)

主要有两个函数:

- dump(data,file_handle[, protocol]) : 将数据序列化到文件.
- dumps(data[, protocol]) : 将数据序列化成字符串.

protocol是数据流处理策略:

- `0`: ascii串保存, 默认形式, 方便人读取 
- `1`: 旧式兼容性较强2进制形式
- `2`: 支持新式类的2进制模式,Python2.3开始引入.

~~~python
a=[1,2,3]
# dumps() to string
cPickle.dumps(a)
'(lp1\nI1\naI2\naI3\na.'

# dump() to file
f=open('data.txt','wb')
cPickle.dump(a,f)
f.close
~~~

## load 载入数据(反序列化)

主要有两个函数:

- load(file) : 将序列化数据从文件读入返回数据.
- loads(string) : 将字符串的序列化数据读入并返回数据.

~~~python
# loads() from string to data
d=cPickle.loads('(lp1\nI1\naI2\naI3\na.')
# load() from file to data
df=cPickle.load('data.txt')
~~~

## cPickle模块

只要有Pickler函数(类),Unpickler函数(类),dump[s],load[s]函数以及几个错误类组成.一般只用那四个函数. 

~~~
# CLASS
exceptions.Exception(exceptions.BaseException)
    PickleError
        PicklingError
            UnpickleableError
        UnpicklingError
            BadPickleGet
# FUNCTION
Pickler(...)
    Pickler(file, protocol=0) -- Create a pickler.

    This takes a file-like object for writing a pickle data stream.
    The optional proto argument tells the pickler to use the given
    protocol; supported protocols are 0, 1, 2.  The default
    protocol is 0, to be backwards compatible.  (Protocol 0 is the
    only protocol that can be written to a file opened in text
    mode and read back successfully.  When using a protocol higher
    than 0, make sure the file is opened in binary mode, both when
    pickling and unpickling.)

    Protocol 1 is more efficient than protocol 0; protocol 2 is
    more efficient than protocol 1.
    protocol; supported protocols are 0, 1, 2.  The default
    protocol is 0, to be backwards compatible.  (Protocol 0 is the
    only protocol that can be written to a file opened in text
    mode and read back successfully.  When using a protocol higher
    than 0, make sure the file is opened in binary mode, both when
    pickling and unpickling.)

    Protocol 1 is more efficient than protocol 0; protocol 2 is
    more efficient than protocol 1.

    Specifying a negative protocol version selects the highest
    protocol version supported.  The higher the protocol used, the
    more recent the version of Python needed to read the pickle
    produced.

    The file parameter must have a write() method that accepts a single
    string argument.  It can thus be an open file object, a StringIO
    object, or any other custom object that meets this interface.

Unpickler(...)
    Unpickler(file) -- Create an unpickler.

dump(...)
    dump(obj, file, protocol=0) -- Write an object in pickle format to the given file.

    See the Pickler docstring for the meaning of optional argument proto.

dumps(...)
    dumps(obj, protocol=0) -- Return a string containing an object in pickle format.

    See the Pickler docstring for the meaning of optional argument proto.

load(...)
    load(file) -- Load a pickle from the given file

loads(...)
    loads(string) -- Load a pickle from the given string
~~~

## Reference

1. [Python2 pickle/cPickle](https://docs.python.org/2/library/pickle.html)

------
