---
layout: post
title: Python迭代器和生成器
date: 2015-09-06 20:49:30
categories: Coding
tags: Python
archive: true
---

## 可迭代对象Iterable

凡是可以用作for循环的都是可迭代对象,包括一般的list,tuple,set,dict,迭代器和生成器(或生成器函数)等.

可迭代对象具有`__iter__`方法返回迭代器. 可迭代对象可以通过`iter(obj)`生成迭代器(本质调用`__iter__`方法). 

可迭代对象本质是数据流,一个接一个的数据,但不一定像迭代器和生成器一样记住迭代到那个点, 下一个是什么, 利用iter()函数可以将list等转变为迭代器(其实是生成器), 逐个元素投出.

可以通过`isinstance(obj, Iterable)` (需要事先`from collections import Iterable`)来判断对象是否可迭代对象.

## 迭代器(Iterator)对象：

凡是可以通过next()方法返回下一个值的可迭代对象就是迭代器. 生成器是一种迭代器.enumurate也是迭代器(本质生成器)

可以通过`isinstance(obj, Iterator)` (需要事先`from collections import Iterable`) 来判断对象是否迭代器.

迭代到没有值了返回`StopIteration`错误.

迭代器拥有`__iter__`方法和`next`方法,有时隐藏掉(如生产器).但本质具备该两种方法.`__iter__`方法返回迭代且对象本身, 而next方法则调用下一个元素. 在自定义迭代器时需要定义该两种方法.for循环本质是通过调用可迭代对象的`__iter__`方法获取迭代器对象,再用next方法遍历元素.

### 可迭代对象和迭代器的分开自定义

分开定义的好处在于, 当对可迭代对象使用iter()转变时,返回一个新的迭代器对象, 这时不受先前产生的相应迭代器对象影响.

~~~python
class Zrange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return ZrangeIterator(self.n)

class ZrangeIterator:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()    

            
zrange = Zrange(3)
print zrange is iter(zrange)   
#>>> True  
print [i for i in zrange]
#>>>[1,2,3]
print [i for i in zrange]
#>>>[1,2,3]

# 若不区分可迭代对象和迭代器, 即这里列表生成式中使用ZrangeIterator的话, 
# 第二次调用时迭代器已被迭代完,第二次会为空集.
zzrange=ZrangeIterator(3);
print [i for i in zzrange]
#>>>[1,2,3]
print [i for i in zzrange]
#>>>[]
~~~

## generator生成器对象

生成器通过`生成器函数`产生, 生成器函数可以通过常规的def语句来定义, 不用return而是使用`yield`一次返回一个结果, 返回后停在相应位置, 再次调用时继续执行生成下一个结果, 当生成器结束没有下次执行时, 返回`StopIteration`.

`(x for x in range(10))`该表达式产生的是生成器对象,而非列表.

生成器有`close()`方法,可以关闭生成器. 另有`send(obj)`方法,定义`yield`表达式执行后返回的值. 如`val=yield i`,正常情况下用next返回的值为None,所以`send(None)`和next()等价.也可以另外赋值,从而追踪某些情况.另外注意send第一次使用要在执行过yield以后(即最少一次执行迭代)才能使用,否则没有yield的返回值可以定义就会报错.

~~~python
# 生成器函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #生成器关键一步yield,每次执行到此返回,下次从此开始.
        yield b
        a, b = b, a + b
        n = n + 1
# 通过生成器函数产生生成器对象
g=fib(6);
# 单独调用生成器对象
print g.next();
# 利用循环迭代生成器
for i in g:
    print i
~~~

## list等的迭代器.

将list/dict等转化为迭代器使用`iter(obj)`函数.

`i.next()`方法或`next(i)` 函数遍历迭代器

`enumerate(i)`

### 通过iter()函数将list/dict等数据组组转为迭代器.

~~~python
# 创建一个列表迭代器(listiterator)
i1 = iter([1, 2, 3])  # iter是Python BIF，用于生成迭代器，文档见底部
type(i1)
<type 'listiterator'>
i1
<listiterator object at 0x1cedf50>

# 创建一个字典项迭代器(dictionary-itemiterator)
d = dict(a = 1, b = 2)
i2 = d.iteritems()  # 生成iterator对象，对于字典来说还有iterkeys, itervalues等方法可用
i2
<dictionary-itemiterator object at 0x1dfe208>
[e for e in d.iteritems()]  # dict.iteritems方法生成的是迭代器元素为键值对形式
[('a', 1), ('b', 2)]

# 另外还有tuple/set等都可使用iter函数返回iterator对象
~~~

### 步进式访问迭代器中元素

obj.next()

~~~python
i = iter(range[3])
i.next()
0
i.next()
1
next(i)  # next() - python2.6新增BIF，作用同iterator.next()
2
next(i)  # 无元素可迭代时，抛出StopIteration异常，可以通过捕获此异常判断是否迭代完毕
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
~~~

### 循环访问遍历迭代器：

~~~python
# 手动循环
try:
    while True:
        next(i)  # python2.6之前版本使用iterator.next()方法
except StopIteration:
    print 'Done'

# for循环
>>> i = iter(range(3))
# 以下句法叫做列表解析，这与生成器表达式类似，之后文章介绍生成器时再记
>>> [e for e in i]  # for在这里不断调用next函数，直到捕获StopIteration异常后退出
[0, 1, 2]
~~~

### 将迭代器传递给其他函数使用：

~~~python
>>> list(iter(range(3)))
[0, 1, 2]
~~~

### 帮助迭代器实现索引功能：

使用enumerate函数返回一个迭代器对象, 该对象能够生产一个元组包括`(索引,值)`.

`enumerate(iterable, start=0)`

第一参数是可迭代对象包括list/dict/迭代器等, 第二个参数是索引开始的号.

~~~python
>>> i = iter('abc')  # python中字符串也是可迭代对象
>>> [(k, v) for k, v in enumerate(i)]  # enumerate返回一个元素为tuple的iterator，文档见底部
[(0, 'a'), (1, 'b'), (2, 'c')]
~~~

## Reference
1. iter函数 - [文档](https://docs.python.org/2/library/functions.html#iter)
2. enumerate函数 - [文档](https://docs.python.org/2/library/functions.html#enumerate)
3. [Python迭代器和生成器](http://www.cnblogs.com/wilber2013/p/4652531.html)

> 本博文已合并到[Python语法汇总](/1234/01/01/Python-Language/#iterator)中, 不再更新.

------
