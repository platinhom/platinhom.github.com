---
layout: post
title: Python基于内建字符串进行继承
date: 2016-01-05 05:04:58
categories: Coding
tags: Python
---

基于内建字符串进行继承并不难, 只要 `class newclass(str): codes`{:.language-python}就可以继承了. 

这里我以DOI为例. 当DOI对象初始化时我想对其进行处理:

- 必须含有`10.`否则为空
- 小写化
- 分解为前缀prefix和后缀suffix属性

## 关于初始化和构造函数

使用 `def __init__(self,string=""): codes`{:.language-python} 可以初始化字符串, 例如进行prefix和suffix处理. 然而, 当我想处理当输入不合规格时转为空并且小写化(实际要修改其内容)时, 无论怎么变, 哪怕self=newstring, 都是不行的..因为str是**不可变序列**.

实际上`__init__`只是初始化时的预处理, 而字符串的值储存在对象内的是在构造时构建的, 不能修改. 所以, 真正要实现目的要使用`__new__`这个少见的真正的构造函数.实际上, `__new__`是在`__init__`之前执行的, 是真正的构造函数, 最后会返回真正的对象. 可以认为实际上是执行 `__init__(__new__(self,params))`{:.language-python}, 传递给init的params也是new的params.

另外, 因为继承自字符串类型, 返回的应该是str的`__new__(self,params)`后的对象.所以就是`__init__(str.__new__(self,params))`{:.language-python}, 当然这里是可以自行调整的啦并不是直接`__init__(str.__new__(self,params))`{:.language-python}.

另外注意初始化`__init__(self)`要显式调用`str.__init__(self,string)`.

--------

这是DOI这个类的初始化和构造函数的部分:

~~~python
################ DOI class ############################
class DOI(str):
	'''A class for standard DOI. 
	It should contain "10." and / or @, Else: it will be blank 
	if doi is quote, it will unquote when generate'''
	pdoi=re.compile("\\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?![\|\"&\'<>])\\S)+)(?:\+?|\\b)")
	def __new__(self,doi=""):
		'''Should be 10.*/ or 10.*@ 
		Normalize(lower,strip)
		Unquote it (@ to /)'''
		if "10." in doi:
			doi=doi.lower().strip()
			if ("/" in doi):
				return str.__new__(self,doi)
			elif("@" in doi):
				return str.__new__(self,requests.utils.unquote(doi.replace('@','/')))
			else:
				return str.__new__(self,"")
		else:
			return str.__new__(self,"")

	def __init__(self,doi=""):
		'''Generate prefix/suffix'''
		str.__init__(self)
		tmp=self.split('/',1)
		self.prefix=tmp[0]
		if (len(tmp)>1):
			self.suffix=tmp[1]
		else:
			self.suffix=""
		#article object
		self.record=None
		self.url=""
~~~

如果新类是两个传入参数, 由于str只有一个传入参数, 此时更需要`__new__`否则直接就报错了..

例如:

~~~python
class newstring(str):
	def __new__(self, value, othervalue, *args, **keywargs):
		self.other=othervalue
		return str.__new__(self, value)
	def __init__(self, value, othervalue):
		self.othervalue = othervalue
~~~

继承自str的对象有str的方法, 当然就可以支持str一样操作, 并且和str对象进行互通, 例如:

- `doi+str`
- `for i in doi:`
- `def func(string): code ; func(doi)`

------
