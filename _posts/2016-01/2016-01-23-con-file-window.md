---
layout: post
title: Create Con file in window
date: 2016-01-23 08:25:24
categories: IT
tags: System
---

## Con等保留名的文件/文件夹无法创建!

前段时间程序构建一个叫`con.2`的文件夹, 报错说存在文件不能建立文件夹. 

> mkdir: 'con.2' exists but is not a directory

但进去一看啥都没有啊..ls -a也没有...以为是缓存或者什么的问题, 后来重启后依然无法解决. 可以删掉母文件夹, 证明这里面没有什么空白文件被系统用着..奇怪了...用touch都创建不了这个文件

> touch: setting times of 'con.2': No such file or directory

上网一查, 才知道在Window下不能创建叫con的文件夹或者文件...

由于Window的历史问题, Con等文件被认为是设备(MS-DOS中的键盘和显示,CONsole) ([官方解释](https://support.microsoft.com/en-us/kb/74496)), 因此用户无法建立名字是Con的文件夹或文件(大小写都不行). 上面的case里因为文件夹名字是`con.2`像文件一样所以也不行..

除了con是保留名, 还有以下保留名,像prn, aux:

## Window下保留名

Name    |	Function
----|--------
CON     |	Keyboard and display
PRN     |	System list device, usually a parallel port
AUX     |	Auxiliary device, usually a serial port
CLOCK$  |	System real-time clock
NUL     |	Bit-bucket device
A:-Z:   |	Drive letters
COM1    |	First serial communications port
LPT1    |	First parallel printer port
LPT2    |	Second parallel printer port
LPT3    |	Third parallel printer port
COM2    |	Second serial communications port
COM3    |	Third serial communications port
COM4    |	Fourth serial communications port

网上有说法说什么使用Alt+小键盘的方法, 其实只是输出一些非正常字符罢了, 并不是真正将文件叫做Con. 

真正可以创建的办法是使用命令行一种特殊方式, 使用`\\.\绝对路径`的方法来创建或删除. 但其实他还是个特殊的东东. 可以在图形界面在里面创建子文件夹(不能命令行). 删除只能使用命令行同样形式来删除.

~~~bash
mkdir \\.\C:\Users\me\Desktop\CON
rmdir \\.\C:\Users\me\Desktop\CON
~~~

但注意, 他还是个特殊的家伙!!!! 我尝试把这东东提交到Github里面, Git就挂了..他还是比较特殊, 所以建议不使用..

例如我现在处理`con.2`就把他变成`con%2e2`的url quoted形式..看来还要再改改对prn,aux,nul特殊处理COM2/3/4, LPT1/2/3等特殊处理..


------
