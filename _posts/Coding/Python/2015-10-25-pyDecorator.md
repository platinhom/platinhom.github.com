---
layout: post
title: Python装饰器和符号@
date: 2015-10-25 12:50:54
categories: Coding
tags: Python
archive: true
---


## 装饰器 Decorator 

在代码运行期间动态增加功能的方式，称之为“装饰器”。装饰器本质是高阶函数, 就是将函数作为参数进行相应运作,最后返回一个闭包代替原有函数. 装饰器本质就是将原函数修饰为一个闭包(一个返回函数).

装饰器在python中在函数/对象方法定义前使用`@`符号调用. 装饰器可以在函数运行前进行一些预处理, 例如检查类型等.

~~~python
@dec1
@dec2(arg1,arg2)
def test(arg):
    pass
~~~

以上代码等于`dec1(dec2(arg1,arg2)(test(arg)))`

## 简单的装饰器及其运行机制

例如:

~~~python
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
    print '2015-10-26'
    return "done"
now()
# 实际调用wrapper()
#>>> call now()
#>>> 2015-10-26
~~~

### 装饰器运行机制

机制就是,调用now()实际调用log(now)() (前面`@`写法后,实际运行now=log(now)),也就是运行了wrapper(),并把now函数原有参数传递给了wrapper函数. wrapper在运行时,加入了新的处理`print 'call %s():' % func.__name__`一句, 并运行相应传递参数的`func(*args,**kw)`并把原有结果返回.

~~~python
now=log(now) #->now=wrapper
result=now() #->wrapper()
>>>call now() #-> wrapper修饰部分
>>>2015-10-26 #-> 原函数部分执行部分
print result
>>>done #-> 原函数的返回部分
~~~

所以装饰器机制简单地说就是要:

1. 将原来函数通过装饰器变成一个传递函数本身的高阶函数(`@log`部分,`now=log(now)`)
2. 新的高阶函数要返回一个修饰函数,从而使调用原函数时实际调用该部分. (`def wrapper()..return wrapper`部分)
3. 新修饰函数进行相应修饰处理(print语句)后,执行原函数并返回原函数值.

## 传递参数的装饰器

~~~python
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print '2015-10-26'
    return "done"
now()
#>>> excute now()
#>>> 2015-10-26
~~~

装饰器本身可以传入参数.不要小看这个传入参数, 传入的参数因为占据了本身装饰器的参数, 所以需要**新的一层装饰器**来处理原函数. 上述机制:

~~~python
now=log('execute')(now) #-> now=wrapper
#或者可以说f=log('execute')  -> f=decorator
#          f(now) -> decorator(now) -> wrapper
#          now=wrapper
result=now() #wrapper()
~~~

实际`now=log('execute')(now)`两个参数表就是执行了一次闭包decorator(now).执行该闭包后返回的才是真正的装饰器wrapper.

两层闭包的机制可以保证传递参数给内在的装饰器wrapper.第一层将参数传进行生成第一层闭包对应返回函数,第二层则将该参数继续留给真正的装饰器闭包.

## 继承原有函数信息

在以上装饰器中, 其实质都是`now=wrapper`, 此时我们要是输出`now.__name__`得到的将是装饰器wrapper的名字.可以用`wrapper.__name__=func.__name__` 加在装饰器内部进行原函数信息的继承, 也可以使用`functools.wraps`来实现.

~~~python
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
~~~

对于带参数的装饰器, 依然将`@functools.wraps(func)`写在实质装饰器wrapper前面.

其机制:

~~~python
wrapper=functools.wraps(func)(wrapper) 
#将原函数func信息给返回函数f=functools.wraps(func), f 闭包含有相应func信息.
#用f 返回函数来修饰wrapper, 此时实际可以将wrapper的一些信息替换为原函数
~~~

对于很复杂的体系, 需要经常定义一些高阶函数对新函数进行一系列处理, 此时定义装饰器就可以省很多功夫. 但缺点是初学比较难以理解, 要对OOP十分熟悉.

## 对象方法变对象属性的装饰器@property和@*.setter

该装饰器是python内置的,是类中一个高级用法,作用是将一个**方法名变成一个对象属性**. 类需要继承于**object**相应的类.    
构建相应`@property def prop(self):return self._prop`就可以直接`obj.prop`来将方法变成获取对象属性的调用形式.而相应`@prop.setter def prop(self,value): self._prop=value` 就可以实现`obj.prop=value`将方法转为对象属性的赋值.而且好处还可以在此加入属性的值的检查. *obj._prop*只是相应储存的储存地方,名字也是无限制的.  
不定义setter而只定义property的话,该**属性就是只读的**不能修改的!!

例如:

~~~python
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def fail(self):
        return True if (self.score <60) else False
        # (self.score <60) and return True or return False

s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
s.score # OK，实际转化为s.get_score()
### 60
s.score = 9999
### Traceback (most recent call last):
###   ...
### ValueError: score must between 0 ~ 100!
s.fail
### False
s.fail=True
### Traceback (most recent call last)
### ...
### AttributeError: can't set attribute
~~~

> 本博文已合并到[Python语法汇总](/1234/01/01/Python-Language/#more-decorater)中, 不再更新.

------
