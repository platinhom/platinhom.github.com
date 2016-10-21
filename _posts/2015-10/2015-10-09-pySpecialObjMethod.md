---
layout: post
title: Python对象的特殊属性和方法
date: 2015-10-09 07:36:03
categories: Coding
tags: Python
archive: true
---

Python一切皆对象(object)，每个对象都可能有多个属性(attribute)。Python的属性有一套统一的管理方案。
 
对象的属性可能来自于其类定义，叫做类属性(class attribute)。
类属性可能来自类定义自身，也可能根据类定义继承来的。
一个对象的属性还可能是该对象实例定义的，叫做对象属性(object attribute)。
对象的属性储存在对象的`__dict__`属性中。
`__dict__`为一个词典，键为属性名，对应的值为属性本身。

## 属性

- `__doc__`: 帮助说明, 将字符串写在对象定义声明之下.
- `__module__`: 模组名,就是文件的名字(无后缀)部分
- `__class__`: 返回对象的类信息
- `__dict__`: 储存对象属性/方法的字典.
- `__slots__`: 设置一个元组,限定允许绑定的属性名称(不能动态添加以外的属性). 只能对当前类起效, 对子类不起效(除非在子类中也定义`__slots__`，这样，子类允许定义的属性就是自身的`__slots__`加上父类的`__slots__`。)

## 方法

- `__init__(self, args)`: 对象初始化时执行的函数
- `__getattr__(self,attr)`:在调用获取对象属性执行,只查询在不在`__dict__`中的属性(相当于先在`__dict__`中查找,找不到再用本函数). 如果调用是对象方法, 处理时返回值是函数才OK.
- `__setattr__(self,attr,value)`:在对对象属性赋值时执行
- `__delattr__(self,attr)`:在删除属性时执行 `del obj.attr`.
- `__getattribute__(self,name)`: 在调用获取对象**任意**属性时执行,和getattr比,任意属性都会调用,相当于在`__dict__`查找前执行.
- `__str__(self)`: 在str()时执行相应功能
- `__repr__(self)`: 是输出和打印出来显示的内容.有时可以和`__repr__=__str__`解决
- `__len__(self)`: len()函数时返回长度的行为
- `__iter__(self)`: 作为可迭代对象时返回迭代器本身(或转为迭代器).
- `__call__(self)`: 将实例变得可调用 `obj()`.还可以定义参数.具备该方法,可以用`callable(var)`来判断一个变量是对象还是一个函数(可调用对象).
- `__lt/le/eq/ne/gt/ge__(self,other)`: 二元比较符时调用,对应于`<,<=,==,!=/<>,>,>=`,相当于self<other. 优先于`__cmp__`
- `__getitem__(self,var)`: 可以使用`obj[n]`方式获取值,例如Fib函数可以取其中一项.如果使用list的切片功能,就要判断var是否`slice`对象`isinstance(var,slice)`.slice有start, stop, step属性,负数处理要另外处理..
- `__setitem__(self,var,value)`: 可以用来对值进行赋值时的操作.
- `__delitem__(self,var)`: 删除某个元素的操作.


模组有:

`__name__`: 模组名




判断对象是否有指定属性:

1. `hasattr(obj,attr)`: 返回真假(通过getattr异常与否来实现)
2. `dir(obj)`: 列出对象现有属性
3. 通过`try: obj.attr; except AttributeError: pass`

1. [特殊方法](https://docs.python.org/2/reference/datamodel.html#special-method-names)



> 本博文已合并到[Python语法汇总](/1234/01/01/Python-Language/#more-special-methodprop)中, 不再更新.

------
