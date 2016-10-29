---
layout: post
title: Python捕获所有异常
date: 2015-08-26 08:45:57
categories: Coding
tags: Python
archive: true
---

有关异常的东东可以参考前篇[Python异常处理](http://platinhom.github.io/2015/08/25/PythonException/).

前篇已经提及可以使用`except: statement`来捕获所有异常, 但是你不知道那个是什么异常..但我们很多时候也想知道究竟是啥异常在哪里发生.其实是有方法通抓错误并分析的. 当然, 使用异常处理还是最好使用好针对某种异常的处理啦.推荐记住`except:traceback.print_exc()`

## 使用traceback模块

回溯模块可以回溯运行记录. `traceback.print_exc()`可以印出最后的异常情况.

~~~python
import traceback
try:
	print b[1]
except:
	traceback.print_exc()
print "hello world"
raw_input()
#输出:
#Traceback (most recent call last):
#  File "C:\Users\Hom\Desktop\test.py", line 17, in <module>
#    print b[1];
#NameError: name 'b' is not defined
#hello world
~~~

还可以使用文件来保存异常信息用于日后分析,例如:

~~~python
import traceback
try:
	print b[1]
except:
	ferr=open("errorlog.txt",'a')
	traceback.print_exc(file=ferr)#实名指定参数
	f.flush()#刷新
	f.close()
raw_input()
~~~


## 使用sys模块

使用`sys.exc_info()` 方法会返回一个三元元组, 第一个是错误类型, 第二个是错误信息,第三个是回溯对象信息. 信息差不多,但是不如traceback.print_exc()来得干脆.

~~~python
import traceback
try:
	print b[1]
except:
	print sys.exc_info()
print "hello world"
raw_input()
#输出:
#(<type 'exceptions.NameError'>, NameError("name 'b' is not defined",), <traceback object at 0x02582288>)
#hello world
~~~

## 使用基类:

~~~python
try:
	statement
except Exception,ex:
	print Exception,":",ex
~~~

这里使用了基类Exception来通捕获错误. 其实第一个只是告诉自己是什么类型异常(肯定是*<type 'exceptions.Exception'>*了),意义不大,而后面实例化抓回来的ex就可以储存信息了,究竟是啥错误~ 这种应用基类的方法可以捕获各种错误并且实例化,但是缺点是不知道异常类型, 靠猜.


> 本博文已合并到[Python语法汇总](/1234/01/01/Python-Language/#catch-all-exception)中, 不再更新.

-----