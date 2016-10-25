---
layout: post
title: Python:StringIO模块模拟文件对象
date: 2016-02-25 03:36:48
categories: Coding
tags: Python
---

StringIO模块和相应C版本的cStringIO模块是产生一个类似于文件对象的对象, 具有文件对象的方法, 但本质是一个储存式的字符串. 

什么时候需要用到这玩意呢? 当你使用某个包的函数, 该函数需要文件对象作为操作对象, 而你并不想使用文件而是使用字符串来代替的时候. 举例, `pdfminer`模块一些方法(最基础的打开pdf文件操作)需要使用文件对象进行读取`read`和文件指针定位`seek`, 但我想使用网络的pdf数据存到内存作为输入, 不想写到硬盘. 这时StringIO就起作用了.

简而言之, 已有的方法/函数需要文件对象(尤其内部会调用文件对象的方法), 但只想用字符串代替, 就可以用StringIO.

StringIO主要就是一个StringIO类. 创建StringIO对象:

~~~python
from StringIO import StringIO
sio=StringIO()
sio.write("Hello world")
sio.getvalue()
# Hello world
~~~

- **buf** : 缓冲区内容                          
- **buflist** : 一个list, 不明                         
- close()  : 关闭SIO对象的方法                      
- closed : 属性, 返回是否已关闭.
- flush() : 刷新缓存.
- **getvalue**() : 获取当前SIO对象储存的所有文档内容. 不改变文件指针. 特有方法.    
- isatty() : 文件是否连接到tty设备. 对StringIO永远False. 
- **len** : 总长度(字符串)
- next() : 下一行.
- **pos** : 文件指针位置        
- read() : 读取当前指针起所有内容
- readline() : 读取当前行
- readlines() : 读取所有行返回列表.   
- seek(pos, mode=0) : 设置文件指针位置到pos. 默认模式mode=0是从开头算起, 1是当前位置算起, 2是文件末算起
- softspace
- tell() : 当前文件指针位置.
- truncate
- write
- writelines

------
