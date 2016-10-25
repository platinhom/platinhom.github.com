---
layout: post
title: Python:with statement
date: 2016-02-03 12:07:59
categories: Coding
tags: Python
---

经常看到 `with open('filename') as f:....` 的用法. 就是打开文件嘛. 和平时的有啥不同呢? `with`语句是干嘛的??

`with`语句是Python2.5以后引进的, 主要是作为一种特殊的`try...finally..`来处理对象, 需要联系上两个特殊方法: `__enter__`和`__exit__`. 他又叫做**上下文管理协议**(with语句).

----

- 一般地, 我们要处理一些事,为防漏掉或者出错, 有时必须做些手尾功夫, 这时经常用到`try .. finally...`. 例如

~~~python
f=open('hi.txt')
try:
	#some codes
	os.renames('hello.txt','hi2.txt')
finally:
	f.close()

 #set things up
try:
    #do something
finally:
    #tear things down
~~~

上面的写法可以避免中间代码执行时出错 (例如不存在hello.txt或者已存在hi2.txt 或者别的状况) 忘了关闭文件. 类似地, 我们建立一些东西, 最后要销毁他. 也是这么回事.

- 如果要经常上述那么干, 可以包装到函数里面, 例如:

~~~python
def controlled_execution(callback):
    #set things up
    try:
        callback(thing)
    finally:
        #tear things down

def my_function(thing):
    #do something

controlled_execution(my_function)
~~~

我们将上面的#some codes和改名放到`my_function`, 而打开`hi.txt`文件操作放到`controlled_execution`, 这样就可以反复利用这个try..finally文件操作了.

如果我们要返回一个对象并且该对象作为局部变量可能将会被修改, 用完后还是这样tear收拾掉. 可以:

~~~python
def controlled_execution():
    #set things up
    try:
        yield thing
    finally:
        #tear things down

for thing in controlled_execution():
    #do something with thing
~~~

这里需要使用for循环来生成该对象..怪怪的..例如上面的例子, 我们将hi.txt的文件对象返回并被操作, 就要这么干...为了简化这个 *进去干点什么甚至返回值, 最后还要撕毁掉* 的过错, 引入了两个新的类的特殊方法:`__enter__`和`__exit__`以及`with`语句, 一个是进去时干点什么(可以生成返回), 一个是退出时撕毁掉. 例如:

~~~python
class controlled_execution:
    def __enter__(self):
        #set things up
        return thing
    def __exit__(self, type, value, traceback):
        #tear things down

with controlled_execution() as thing:
     #do something with thing
~~~

`__enter__` 相当于之前的设置并try的过程, `__exit__`相当于finally的过程, 而 `with ... as var` 则相当于利用该类两个方法并可以返回对象给`as`后的变量. 这个`with`相当于上上面例子的`controlled_execution`函数的打包. 

### with语句的执行过程是:

1. 当`with`语句并调用时, 后面的表达式会被执行, 表达式的返回值(例如文件对象)的`__enter__`方法会被调用
2. `__enter__`调用的返回结果递给`as`后的变量, 用于日后执行操作
3. 随后会执行`with`内的语句块block (`#do something with thing`), 如果出了问题, 就执行`__exit__`部分(相当于`finally`)
4. 如果没有出错, 最后语句块结束时, 也会执行`__exit__`部分.

`__exit__`部分可以接受参数, 分别是异常类型、异常值和追溯信息(如果有的话). 在异常发生时会自动传给`__exit__`方法, 方便处理 (例如忽略某种异常, 返回一些值). 例如:

~~~python
def __exit__(self, type, value, traceback):
    return isinstance(value, TypeError)
~~~

从上面可以知道, 使用`with`语句需要几个条件 (如创建可以使用`with`的类时要注意):

- with后的表达式返回一个对象
- 对象含有`__enter__`和`__exit__` 方法
- 一般这个对象要被进一步被处理, 这时在`__enter__`中要使用`return` 语句来返回给`as`后的变量(返回自身就 `return self`, 还可以使用生成器生成别的玩意)

一定要注意这三个条件才能写出`with`的使用对象!

### 文件对象的with

文件对象自带`__enter__`和`__exit__` 方法, 前者返回文件对象自身, 后者就是关闭文件咯.

~~~python
>>> f = open("x.txt")
>>> f
<open file 'x.txt', mode 'r' at 0x00AE82F0>
>>> f.__enter__()
<open file 'x.txt', mode 'r' at 0x00AE82F0>
>>> f.read(1)
'X'
>>> f.__exit__(None, None, None)
>>> f.read(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file
~~~

使用时就可以简化为下面的语句, 打开的文件对象被返回为`as`后的变量, 随后文件被操作, 最后不用写关闭自动关闭文件: 

~~~python
with open("x.txt") as f:
    data = f.read()
    #do something with data
~~~

这种写法的好处是把原来的 `f=open(); try: .. finally: f.close()` 简化为一行了~

## Reference

1. [让对象支持上下文管理协议](http://python3-cookbook.readthedocs.org/zh_CN/latest/c08/p03_make_objects_support_context_management_protocol.html)

------
