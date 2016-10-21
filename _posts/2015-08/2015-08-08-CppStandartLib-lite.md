---
layout: post
title: C++标准库简要介绍(ZZ)
date: 2015-08-08 08:18:36
categories: Coding
tags: C++ ZZ
---

c++程序通常可以调用标准c++库中的大量函数。这些函数完成一些基本的服务，如输入和输出等，同时也为一些经常使用的操作提供了高效的实现代码。这些函数中含有大量的函数和类定义，以帮助程序员更好地使用标准c++库。

标准c++库包含以下内容：  

\<algorithm\>,\<bitset\>,\<complex\>,\<deque\>,\<exception\>,\<fstream\>,\<functionl\>,\<iomanip\>,\<ios\>,\<iosfwd\>,\<iostream\>,\<isteam\>,\<iterator\>,\<limits\>,\<list\>,\<locale\>,\<map\>,\<memory\>,\<numeric\>,\<ostream\>,\<queue\>,\<set\>,\<sstream\>,\<stack\>,\<stdxcept\>,\<streambuf\>,\<strinig\>,\<strstream\>,\<utility\>

,\<valarray\>,\<vector\>,\<cassert\>,\<cctype\>,\<cerron\>,\<cfloat\>,\<ciso646\>,\<climits\>,\<clocale\>,\<cmath\>,\<csetjmp\>,\<csignal\>,\<cstdrag\>,\<cstddef\>,\<cstdio\>,\<cstdlibn\>,\<cstring\>,\<ctime\>,\<cwchar\>,\<iso646.h\>和\<cwchar.h\>

------

标准c++库的详细消息均在其对应的头文件进行了说明。主要标准c++库头文件如下所示。其中13项为标准模板库（STL),在其说明文字的前面标有（STL)的为标准模板库。

- \<algorithm\>---（STL）用于定义实现常用、实用算法的大量模板
- \<bitset\>----- 用于定义官位位集合的模板类
- \<cassert\>-----用于在程序执行时执行断言
- \<cctype\>-----用于对字符进行分类
- \<cerrno\>-----用于测试有库函数提交的错误代码
- \<cfloat\>------用于测试浮点类型属性
- \<cios646\>----用于在ISO646变体字符集中编程
- \<climits\>-----用于测试整数类型属性
- \<clocale\>-----用于使程序适应不同的文化风俗
- \<cmath\>———用于计算常用的数学函数
- \<complex\>-----用于定义支持复杂算法的模板类
- \<csetjmp\>-----用于执行非局部的goto语句
- \<csignal\>------用于控制各种异常情况
- \<cstdrag\>-----用于访问参数数量文化的函数
- \<cstdarg\>-----用于访问参数数量变化的函数
- \<cstddef\>----用于定义实用的类型和宏
- \<cstdio\>-----用于执行输入和输出
- \<cstdlib\>----用于执行同一操作的不同版本
- \<string\>-----用于处理几种不同的字符串类型
- \<ctime\>------用于在几种不同的时间和日期格式间进行转换
- \<cwchar\>----用于处理宽流（wide stream)和字符串
- \<cwctype\>---用于对宽字符（wide character是）分类
- \<deque\>---(STL)用于定义实现双向队列容器的模板类
- \<exception\>---用于定义控制异常处理的几个函数
- \<fstream\>-----用于定义处理外部文件的几个iostream模板类
- \<functional\>-----（STL)用于定义几个模板，该模板将帮助在\<algorithm\>和\<numeric\>中定义的模板构造谓词
- \<iomapip\>---- 用于声明一个带有参数的iostreams控制器
- \<ios\>-----用于定义用作大量iostreams类的基类的模板类
- \<iosfwd\>-----用于定义iostreams模板类（在需要定义之前）
- \<iostream\>---用于声明处理标准流的iostreams对象
- \<istream\>---用于定义执行析取操作的模板类
- \<iterator\>----（STL)用于定义帮助定义和管理迭代器的模板
- \<limits\>---用于测试数字类属性
- \<list\>---（STL)用于定义实现list容器的模板类
- \<locale\>----用于定义在iostreams类中控制与特定位置相关的行为的类和模板
- \<map\>------(STL)用于定义实现关联容器的模板类
- \<memoery\>-----（STL)用于定义对不同容器分配和释放内存的模板
- \<numeric\>-----（STL)用于定义实现实用数字函数的模板
- \<ostream\>----用于定义管理字符串容器的iostreamas模板类
- \<queque\>----(STL)用于实现队列容器的模板类
- \<set\>-----（STL)用于定义实现只有唯一元素的关联容器的模板类
- \<sstream\>----用于定义管理字符串容器的iostreams模板类
- \<stack\>-----（STL)用于定义实现堆栈容器的模板类
- \<stdexcept\>----用于定义提交异常的类
- \<streambuf\>----用于定义为iostreams操作分配缓冲区的模板类
- \<string\>------用于定义是实现字符串容器的模板类
- \<strstream\>-----用于定义处理非内存（in-memory)字符系列的iostreams类
- \<utility\>-----（STL)用于定义通用工具的模板
- \<valarray\>----用于定义支持值（value-oriented）数组的类和模板类
- \<vector\>----（STL)用于定义实现向量容器的模板类

标准c++库还包括18个标准C库中的头文件，但其中有些变化。我们暂时不讨论，这些头文件为：

- \<assert.h\>---用于在程序运行时执行断言
- \<ctype.h\>----用于对字符分类
- \<errno.h\>----用于测试用库函数提交的错误代码
- \<float.h\>----用于测试浮点类型属性
- \<ios646.h\>-----用于在IOS646变体字符集中编程
- \<limits.h\>-----用于测试整数类型属性
- \<locale.h\>-----用于适应不同的文化习俗
- \<math.h\>----用于计算常见的数学函数
- \<setjmp.h\>----用于执行非局部的goto语句
- \<signal.h\>----用于控制各种异常情况
- \<stdrag.h\>-----用于访问参数数量变化的函数
- \<stddef.h\>-----用于定义类型和宏
- \<stdio.h\>------用于执行输入和输出
- \<stdlib.h\>------用于执行各种操作
- \<string.h\>-----用于处理字符串
- \<time.h\>-------用于在不同的时间和日期格式之间转换
- \<wcchar.h\>-----用于处理宽流(wide stream)和字符类
- \<wctype.h\>-----用于对宽字符（wide character）分类


------
