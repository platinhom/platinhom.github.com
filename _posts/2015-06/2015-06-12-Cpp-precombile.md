---
layout: post
title: C++ 预处理(预编译)命令
date: 2015-06-12 04:51:37
categories: Coding
tags: C++
---

预处理技术就是在正式代码编译前提前进行的简单的处理,而正常代码的编译则在预处理之后再进行.可以做简单的判断,定义宏,定义宏变量等. 可以认为是提前将相应部分进行替换和选择语句块. 最常见的预处理命令是`#include`了. 其次, 可以在编译器中用`-D`选项定义变量来影响编译.

 `#`预处理命令抬头, 在编译前进行预处理. 预处理命令**没有**`;`结束符.

### define
- `#define macro`: 只定义一个宏名,对`ifdef/ifndef`影响大.效果和编译选项`-Dmacro`差不多.
- `#define macro replacement` : macro就是宏常量,将代码中宏常量的部分替换为后面的内容.现在一般用`const`代替. 效果和编译选项`-Dmacro=rep`差不多.
- `#define macro(argv) replacement`: 如S(a,b) a*b.会将()内的参数去代替后面replacement部分.可用于简易定义函数现常被`inline`代替.例如下面的例子就是.
  - `#define toString(s) #s`: `#define #`结构,原来define中的s(任意内容)被取代时前为普通形式如Hello,用了#s后返回的是"Hello",自动加了引号进行字符串化.
  - `#define toChar(s) #@s`: `#define #@`结构, 表示字符化,相当于返回`'s'`,返回类型`const char`.注意单字符.
  - `#define Conn(x,y) x##y`: `#define ##`结构,##表示串接,将前后两个参数串接在一起.即 toString(x,y) == xy

### undef
- `#undef macro`:    取消宏定义.

### ifdef, ifndef, if
- `#if 条件 代码块 else 代码块 #endif`:预处理的判断选择
- `#ifdef macro #elif 条件 代码块 #else 代码块 #endif`: 根据是否已定义宏变量进行选择性执行代码块.
- `#ifndef macro #define macro #endif`: 是否未定义宏变量,一般在头文件开头用于判断,紧跟对宏变量的定义,来避免重复加载头文件  
条件语句的宏, `#ifdef macro`等价于`#if define(macro)`

### include
- `#include <iostream>或"hi.h"`    载入头文件,头文件内容将插入到此处.<>和""区别在于前者首先搜索系统路径,后者搜索当前文件夹. C++新的标准头文件没有.h后缀.

### error
- `#error token-sequence` : 编译时输出编译错误信息token-sequence

### line
- `#line 行号 "文件名"`: 重定义当前行号和文件名,文件名是可选参数.方便调试.

### pragma
- `#pragma 参数`: 让编译者做某些事,不同编译器有所不同.
- `#pragma once` : 写在头文件,就是保证头文件只被编译一次.
- `#pragma warning( warning-specifier : warning-number-list [; warning-specifier : warning-number-list...]`:警告处理. 例如`#pragma warning( disable : 4507 34; once : 4385; error : 164 )`. 不同警告空格隔开.
`#pragma message("提示")`: 在编译信息输出框显示提示的信息.

### 预定义变量
~~~~
__LINE__    当前被处理的行数
__FILE__    当前处理的文件名(带路径)
__DATE__    当前日期    month/day/year格式
__TIME__    当前时间    hour:minute:second格式
__FUNCTION__    当前处理的函数名
_cplusplus    编译C++程序时定义
__STDC__    编译C时定义(C++也可能定义,编译器相关)
~~~~

TODO: to finish all the commands and options.

---
