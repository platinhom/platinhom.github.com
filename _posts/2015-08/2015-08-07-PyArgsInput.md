---
layout: post
title: Python传递参数
date: 2015-08-07 06:43:24
categories: Coding
tags: Python
archive: true
---

和C/C++那种传值传址的传递参数不同, Python中函数参数的传递是通过“赋值”来传递的。函数参数的使用可以概括地分为两个方面，一是函数参数如何定义，二是函数在调用时的参数如何解析的。

## 函数形参定义

函数参数的定义有四种形式：

1. F(arg1,arg2,...)  一般形式
2. F(arg2=,arg3=...)  默认值定义
3. F(*arg1) 不定参数个数
4. F(**arg1) 不定的关键字赋值传给字典

实际中, 这四种方式可以组合在一起形成复杂多样的形参定义形式。在定义或调用这种函数时，要遵循以下**参数顺序规则**：

1. `arg=`必须在`arg`后
2. `*arg`必须在`arg=`后
3. `**arg`必须在`*arg`后

否则,python认不出究竟哪个参数打哪个参数,就会报错.

## 函数调用形参赋值

在函数调用过程中，形参赋值的过程是这样的：

1. 按顺序把`arg`这种形式的实参给对应的形参
2. 把`arg=`这种形式的实参赋值给形参
3. 把多出来的`arg`这种形式的实参**组成一个tuple**给带一个星号的形参
4. 把多出来的`key=value`这种形式的实参转为一个dictionary给带两个星号的形参。

支持关健字赋值法,即调用函数赋值时,指定相应形参名和值. 此时仍遵循`arg=`必须在`arg`后的原则, 而同级的`arg=`则不必遵守形式参数的前后顺序.

## 说明和实例

- **“传统”方式只给形参名：F(arg1,arg2,...)**   
一个函数可以定义一定个数参数，参数（形式参数）放在跟在函数名后面的小括号中，各个参数之间以逗号隔开。用这种方式定义的函数在调用的时候也必须在函数名后的小括号中提供相等个数的值（实际参数），不能多也不能少，而且顺序还必须相同。也就是说形参和实参的个数必须一致，而且想给形参1的值必须是实参中的第一位，形参与实参之间是一一对应的关系，即“形参1=实参1 形参2=实参2...”。很明显这是一种非常不灵活的形式。  

如：`def addOn(x,y): return x + y`，可以用addOn(1,2)的形式调用(x=1,y=2),也可以addOn(1,y=2)和addOn(y=1,x=2)。多参addOn(1,2,3), 少参addOn(1), 违反参数顺序规则addOn(y=2,1)都会出错. 

- **形参名和默认值: F(arg2=,arg3=...)**  
在调用这种函数时，如果没有给对应的形式参数传递实参，那么这个形参就将使用默认值。  

如：`def addOn(x=3,y=5): return x + y`，可以addOn(6,8)-->x=6，y=8; addOn(7)-->x=7，y=5; addOn(y=6)-->x=3,y=6; addOn(y=4,x=6)-->x=6,y=4.  
当: `def addOn(x,y=5): return x + y`时,addOn(y=4,6)就会报错,不遵守参数顺序规则,6究竟是给谁的?!

上面两种方式定义的形式参数的个数都是固定的，比如定义函数的时候如果定义了5个形参，那么在调用的时候最多也只能给它传递5个实参。但是在实际编程中并不能总是确定一个函数会有多少个参数。此时要用下述两种方法来捕获未知的输入.

- **不定个数参数: F(*arg1)**  
以一个`*`加上形参名的方式定义形参，这个函数实际参数是不一定的，可以是零个，也可以是N个。不管是多少个，在函数内部都被存放在以形参名为标识符的元组tuple中。比如:

~~~python
def addOn(*arg):
	sum = 0
	if len(arg) == 0: return 0
	else:
		for x in arg: ##迭代元组内的值
			sum += x
	return sum
~~~

对这个函数的调用addOn() addOn(2) addOn(3,4,5,6)等等都是可以的。

有时候，要给`*arg`赋值，但有时又为了方便使用列表，这时加入以下例子中的判断或在**实参前加`*`**:

~~~python
def func(filedir,*strings):
	#The following is the same when use func(dir,*list_subdir)
	if type(strings[0])==list or type(strings[0])==tuple:
		strings=strings[0]

	print filedir+'/'+'/'.join(strings)
~~~
PS: 实际上，Python内部已经加入这种这样处理了,不过需要在前面加`*`,如传递的是list1,则`func(dir,*list1)`就可以了。func("/home/",\*["a","b","c"])和func("/home/",\*"a","b","c")等价。如果不加`*`,func("/home/",["a","b","c"])中strings实际是 *(["a","b","c"],)*.

- **不定个数并指定参数名: F(\*\*arg1)**  
形参名前面加`**`表示，参数在函数内部将被存放在以形参名的字典。这时候调用函数必须采用key1=value1、key2=value2...的形式。该方法的优点是还可以给出相应的参数名,从而通过字典中键值的处理进行一些操作和过滤. 比如：

~~~python
def addOn(**arg):
	sum = 0
	if len(arg) == 0: return 0
	else:
		for x,y in arg.items(): #或用迭代器arg.iteritems(), 迭代字典
			if (x[0] in "abcdefg"):
				sum += y
	return sum
~~~
那么对这个函数的调用可以用addOn()或诸如addOn(a=4,b=5,k=6)等的方式调用(此时返回9)。

听起来好复杂，实际是是很简单的。很直观，来看例子：

~~~python
def testArgs(x,y=5,*a,**b):
	print x,y,a,b

#test arguments
testArgs(1) # 1 5 () {}
testArgs(1,2) # 1 2 () {}
testArgs(1,2,3) # 1 2 (3,) {}
testArgs(1,2,3,4) # 1 2 (3,4)
testArgs(x=1) #1 5 () {}
testArgs(x=1,y=1) # 1 1 () {}
testArgs(x=1,y=1,a=1) # 1 1 () {'a':1}
testArgs(x=1,y=1,a=1,b=1) #1 1 () {'a':1,'b':1}
testArgs(1,y=1) # 1 1 () {}
testArgs(1,2,y=1) # 出错，2和y=1都是赋给y
testArgs(1,2,3,4,a=1) # 1 2 (3,4) {'a':1}
testArgs(1,2,3,4,k=1,t=2,o=3) # 1 2 (3,4) {'k':1,'t':2,'o':3}
~~~

### 形参最好是不变对象

函数在定义的时候,默认参数的值就被计算出来了,也就是说形参赋的值对应的内存对象已定. 当使用可变对象时, 形参也会被改变.因此可能导致函数功能出错!!例如:

~~~python
def add_end(L=[]):
    L.append('END')
    return L
print add_end()
#->['END']
print add_end()
#->['END','END']
print add_end()
#->['END','END','END']
~~~

形参是可变序列, 定义后L指向一个数组, 当执行函数使用形参后,该形参默认参数对应的列表被修改,因此出错!

> 本博文已合并到[Python语法汇总](/1234/01/01/Python-Language/#mid-pass-func-argv)中, 不再更新.

------
