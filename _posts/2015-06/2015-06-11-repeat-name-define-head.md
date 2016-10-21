---
layout: post
title: 预编译变量与基础库有重复引发的血案
date: 2015-06-11 07:25:14
categories: Coding
tags: C++
---

今天在MSYS中编译一个程序, 怎么都编译不通.报错为某种`typedef`的迭代器没定义.但是在集群HPCC上正常编译过去了...   
 
奇怪了, 明明在`types.h`头文件里定义了啊. 前几个文件都编译过去了, 就是后面的几个主文件总报错. 
怀疑是MSYS中`#include` 产生冲突或别的问题所致, 将基础库写到新的头文件中再被其他头文件调用, 可以避免重复被调用.  
然后出现了这么一句:

> mingw\include\stdio.h error: 'off64_t' has not been declared

stdio怎么可能出错?! google了一下, 有个帖子提及到, 该基础库可能调用`types.h`

`grep "types.h" /c/mingw/include/*` 去看看MSYS所调用的基础库.  
发现好几个文件需要`#include <sys/types.h>`...   
而sys/types.h 里就有下面这段东东...而我编译的程序types.h 同样存在这个预编译变量的定义..

~~~~ cpp
#ifndef _TYPES_H_
#define _TYPES_H_
.........
#endif
~~~~

所以问题就是:

1. 在编译成功的文件中,调用基础库时就调用到MSYS中的基础库的`sys/types.h`,因此定义了预编译变量_TYPES_H_
2. 当真正需要调用`./types.h`里面的迭代器的时候,实际上因为检查预编译变量而跳过了我自己的头文件,所以报错
解决方法很简单, 将自己的`./types.h`里的预编译变量改掉,如下:
3. Linux中系统的可能不需要使用`/sys/`里的内容,因为该部分内容和MSYS所在Window系统相关.所以标准C++没有该问题.这也是MSYS和一般Linux差别.

~~~~ cpp
#ifndef _SURFACE_TYPES_H_
#define _SURFACE_TYPES_H_
.........
#endif
~~~~

教训就是, 预编译变量名需要起得复杂一些!

---
