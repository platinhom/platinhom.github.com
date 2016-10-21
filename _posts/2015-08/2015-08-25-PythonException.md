---
layout: post
title: Python异常处理
date: 2015-08-25 08:45:57
categories: Coding
tags: Python
archive: true
---

异常处理无外乎几件事: 断言(assert)和抛错(raise), 检查(try), 捕获(except), 处理(except,else,finally).  

- 异常即是一个**事件**，该事件会在程序执行过程中发生，影响了程序的正常执行。一般情况下，在Python无法正常处理程序时就会发生一个异常。当Python脚本发生异常时我们需要捕获处理它，否则程序会终止执行。异常作为事件，不需要在程序里传送结果标志或显式地测试它们。
- 异常是Python**对象**，表示一个错误。异常可以作为类被定义, 也可以人为引发异常.
- 异常可以作为**控制流**, 通过异常情况或人为引发异常, 可以执行代码流控制, 实现比较高级的"goto"效果. 例如在for循环内引发错误,可以跳到外面几层的某个try..except内.

~~~python
# 相关语句
try:
	<statement>        #运行别的代码
except：
	<statement>        #捕获任何在try中引发的异常
except <name>：
	<statement>        #如果在try部份引发了'name'异常
except <name>，<data>:
	<statement>        #如果引发了'name'异常，获得附加的数据
except (<name1>,<name2>...):
	<statement>        #捕获任何列出的错误
else:
	<statement>        #如果没有异常发生
finally:
	<statement>    #退出try时总会执行
raise	#人为引发错误
assert <judgement>  #断言,判断一定要返回True否则会引发AssertionError
~~~

try语句用于检测语句块中的错误,从而让except语句捕获其中的异常信息并处理. finally是无论有错无错都会执行.raise语句可以用于人为制造错误. assert语句是断言条件必为真,否则返回断言异常.

## try语句

try的工作原理是，当开始一个try语句后，python就在当前程序的上下文中作标记，这样当异常出现时就可以回到这里，try子句先执行，接下来会发生什么依赖于执行时是否出现异常。try语句有两种模式,try..except..else和try..finally.

### try..except..else

~~~python
# 最常见的模式 try..except..else模式
try:
	<statement>        #运行别的代码
except <name>：
	<statement>        #如果在try部份引发了'name'异常
else:
	<statement>        #如果没有异常发生
~~~

- 如果当try后的语句执行时发生异常，python就跳回到try并执行**最近匹配**该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。
- 如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被**递交到上层的try**，或者到程序的最上层（这样将结束程序，并打印缺省的出错信息）。
- 如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。

except语句有几种形式,包括捕获所有异常的`except: `,某个异常的`except ErrorName:`或几种异常`except (Error1,Error2,Error3):`, `except ErrorName,e:`和`except Error as e: `可以将异常传给变量e,收集作为数据进行处理.

### try..finally

~~~python
# try..finally模式
try:
	<statement>        #运行别的代码
finally:
	<statement>        #不管有无异常都会执行
~~~

try..finally模式是:  

1. 没有异常就先运行try所有语句,再运行finally所有语句. 
2. 要是有异常,try执行到异常就跳到finally,然后直接跳出将异常递交给上层的try.控制流并不通过所有try语句.
3. finally能跟在except/else后,优先先执行except/else再执行finally.

由此可知, try...finally 模式更适合于嵌套在try..except内作为保证某些代码一定执行.因为try..except...else要是执行了except就不会执行else,无法保证某个代码必须执行.所以常见的整合模式为:

~~~python
# 两种模式的嵌套和结合
try:
	<statement1>        #运行测试代码1
	try:
		<statement2>        #运行测试代码2
	finally:
		<statement3>        #不管测试代码2有无异常都会执行
except <name>：
	<statement>        #测试代码1或2发生错误而被捕获,就会执行异常
else:
	<statement>        #测试代码1和2都没有发生错误就会执行
finally:
	<statement4>        #无论两个try有无异常,都会运行一次.
~~~

PS: 要是finally在except/else前面肯定会报错.因为try后直接给finally,然后会交给上层try.但没有上层try...

实例:

~~~python
#!/usr/bin/python

try:
   fh = open("testfile", "w")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print "Going to close the file"
      fh.close()
except IOError:
   print "Error: can't find file or read data"
~~~

## raise语句

raise语句可以很好地用于抛出某个异常从而被try捕获. 更常用于结合if等进行条件检查.例如某变量假定[0,10],<0时抛出一个错,>10抛出另一个错误.

raise一般是`raise exception,args`,args一般采用一个值,来初始化异常类的args属性,也可以直接使用元组来初始化args.

~~~python
raise <name>    #手工地引发异常
raise <name>,<data>    #传递一个附加的数据(一个值或者一个元组),要是不指定参数,则为None.
raise Exception(data)    #和上面等效.
raise [Exception [, args [, traceback]]]  # 第三个参数是用于跟踪异常对象,基本不用.

try:
	if (i>10):
		raise TypeError(i)
	elif (i<0):
		raise ValueError,i
#下面的e实际是返回错误的对象实例.
except TypeError,e:
	print str(e)+" for i is larger than 10!"
except ValueError,e:
	print str(e)+" for i is less than 0!"
else:
	print "i is between 0 and 10~"
~~~


## assert语句

Python的assert是用来检查一个条件，如果它为真，就不做任何事。如果它为假，则会抛出AssertError并且包含错误信息。

`assert expression[,argument]`

表达式部分返回真/假, argument部分一般是引发时传递的标示,一般用于输出,或者进一步用于控制.  

断言一般用于检查条件(像使用if语句再抛错或退出), 而不是用于抛错, 抛错请使用raise. 更多使用技巧参考ref1. 

~~~python
try:
	assert 1 == 0,'one does not equal zero'
except AssertionError,args:
	print '%s:%s' % (args.__class__.__name__,args)
# AssertionError:one does not equal zero 
~~~

## 异常

当一个未捕获的异常发生时，python将结束程序并打印一个堆栈跟踪信息，以及异常名和附加信息。如

~~~python
 Traceback (innermost last):
      File "test.py", line 3, in ?
      a = 1 /0
      ZeroDivisionError: integer division or modulo
~~~

这里异常是ZeroDivisionError, 后面是附加信息.

一般异常类是Except(args), args是一个元组可以接收给予的参数. 字符串化一个异常类就是将这些赋予的参数印出来, 当只有一个参数时,就直接将内容输出,例如上述一些例子在`raise error,string`,`assert exp, string; except AssertionError, e:print e` 都是直接将参数打印出来罢了.如果是多个参数, 就是把元组字符串化. 

异常是一个类. 可以用系统定义的类或者自定义的类.有教程说raise..except可以用字符串作为异常是错误的.会这么说:

~~~python
Traceback (most recent call last):
  File "test.py", line 9, in <module>
    raise "Error1"
TypeError: exceptions must be old-style classes or derived from BaseException, not str
~~~

异常最好直接或间接继承自异常的类, 例如以下:

~~~python
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.argsm = arg
try:
   raise Networkerror("Bad hostname")
except Networkerror,e:
   print e.argsm
#经测试,要是args的话,返回的是一个元组
~~~

上面的测试时,要是把argsm变为args,输出是个元组.why? 因为默认的BaseException里的\_\_init\_\_也是使用args属性来储存所有参数,其本质是个元组,当字符串给了这个元组时就分解为字符元组了.

一般地, 自定义异常类就是写好`__init__`就好了, 也可以自定义一些新属性用于输出.但意义不大, 一般错误就是message和args两个主要属性,还有个`__dict__`属性. 方法里有如`__str__`这种字符串化输出的方法.

### 常见异常

异常名称	 | 	描述
BaseException	 | 	所有异常的基类
SystemExit	 | 	解释器请求退出
KeyboardInterrupt	 | 	用户中断执行(通常是输入^C)
Exception	 | 	常规错误的基类
StopIteration	 | 	迭代器没有更多的值
GeneratorExit	 | 	生成器(generator)发生异常来通知退出
StandardError	 | 	所有的内建标准异常的基类
ArithmeticError	 | 	所有数值计算错误的基类
FloatingPointError	 | 	浮点计算错误
OverflowError	 | 	数值运算超出最大限制
ZeroDivisionError	 | 	除(或取模)零 (所有数据类型)
AssertionError	 | 	断言语句失败
AttributeError	 | 	对象没有这个属性
EOFError	 | 	没有内建输入,到达EOF 标记
EnvironmentError	 | 	操作系统错误的基类
IOError	 | 	输入/输出操作失败
OSError	 | 	操作系统错误
WindowsError	 | 	系统调用失败
ImportError	 | 	导入模块/对象失败
LookupError	 | 	无效数据查询的基类
IndexError	 | 	序列中没有此索引(index)
KeyError	 | 	映射中没有这个键
MemoryError	 | 	内存溢出错误(对于Python 解释器不是致命的)
NameError	 | 	未声明/初始化对象 (没有属性)
UnboundLocalError	 | 	访问未初始化的本地变量
ReferenceError	 | 	弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError	 | 	一般的运行时错误
NotImplementedError	 | 	尚未实现的方法
SyntaxError	 | 	Python 语法错误
IndentationError	 | 	缩进错误
TabError	 | 	Tab 和空格混用
SystemError	 | 	一般的解释器系统错误
TypeError	 | 	对类型无效的操作
ValueError	 | 	传入无效的参数
UnicodeError	 | 	Unicode 相关的错误
UnicodeDecodeError	 | 	Unicode 解码时的错误
UnicodeEncodeError	 | 	Unicode 编码时错误
UnicodeTranslateError	 | 	Unicode 转换时错误
Warning	 | 	警告的基类
DeprecationWarning	 | 	关于被弃用的特征的警告
FutureWarning	 | 	关于构造将来语义会有改变的警告
OverflowWarning	 | 	旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning	 | 	关于特性将会被废弃的警告
RuntimeWarning	 | 	可疑的运行时行为(runtime behavior)的警告
SyntaxWarning	 | 	可疑的语法的警告
UserWarning	 | 	用户代码生成的警告

### Python内建异常体系结构

~~~
BaseException
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- Exception
+-- StopIteration
+-- StandardError
|    +-- BufferError
|    +-- ArithmeticError
|    |    +-- FloatingPointError
|    |    +-- OverflowError
|    |    +-- ZeroDivisionError
|    +-- AssertionError
|    +-- AttributeError
|    +-- EnvironmentError
|    |    +-- IOError
|    |    +-- OSError
|    |         +-- WindowsError (Windows)
|    |         +-- VMSError (VMS)
|    +-- EOFError
|    +-- ImportError
|    +-- LookupError
|    |    +-- IndexError
|    |    +-- KeyError
|    +-- MemoryError
|    +-- NameError
|    |    +-- UnboundLocalError
|    +-- ReferenceError
|    +-- RuntimeError
|    |    +-- NotImplementedError
|    +-- SyntaxError
|    |    +-- IndentationError
|    |         +-- TabError
|    +-- SystemError
|    +-- TypeError
|    +-- ValueError
|         +-- UnicodeError
|              +-- UnicodeDecodeError
|              +-- UnicodeEncodeError
|              +-- UnicodeTranslateError
+-- Warning
+-- DeprecationWarning
+-- PendingDeprecationWarning
+-- RuntimeWarning
+-- SyntaxWarning
+-- UserWarning
+-- FutureWarning
+-- ImportWarning
+-- UnicodeWarning
+-- BytesWarning
~~~


## Reference

1. [Python中何时使用断言](http://blog.jobbole.com/76285/)

> 本博文已合并到[Python语法汇总](/1234/01/01/Python-Language/#Exception-debug)中, 不再更新.

------
