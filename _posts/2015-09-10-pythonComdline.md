---
layout: post
title: Python调用外部命令
date: 2015-09-09 21:02:06
categories: Coding
tags: Python
---

### 方法1: os.system

直接使用 `os.system("command")` 来执行外部程序,返回程序结束返回码(正常0/1错误),这实际上是使用C标准库函数system()实现的。这个函数在执行command命令时需要重新打开一个终端，并且无法保存command命令的执行结果。

缺点: 不能获取程序输出stdout.不能像PHP的`exec(string $command [, array &$output [, int &$return_var ]] )`来用数组储存输出stdout.

### 方法2: os.popen

popen实际是获取命令运行后的输出结果,储存在临时文件当中. 使用命令: 

`os.popen(command [, mode, bufsize])`

实际原理是打开一个与command进程之间的管道。这个函数的返回值是一个文件对象，可以读或者写(由mode决定，mode默认是’r')。如果mode为’r'，可以使用此函数的返回值调用read()来获取command命令的执行结果。

支持逐行分析如下例代码:

~~~python
import os
p = os.popen('command',"r")
while 1:
    line = p.readline()
    if not line: break
    print line
~~~

也支持 `p.readlines()`, `for line in p`等文件处理方法.

### 方法3: commands.getstatusoutput

使用命令: `status, output = commands.getstatusoutput(command)`

实际使用os.popen()函数执行command命令并返回一个元组*(status,output)*，分别表示command命令执行的返回状态和执行结果。对command的执行实际上是按照`{command;} 2<&1`的方式，所以output中包含控制台输出信息或者错误信息。output中不包含尾部的换行符。

~~~python
import commands
status, output = commands.getstatusoutput('ls -l')
~~~

### 方法4: subprocess.Popen/check_output/call 
subprocess模块提供子进程处理方法.使用subprocess模块可以创建新的进程，可以与新建进程的输入/输出/错误管道连通，并可以获得新建进程执行的返回状态。使用subprocess模块的目的是替代os.system()、os.popen.\*()、commands.\*等旧的函数或模块。

#### Popen

实际上是创建一个类对象, `class subprocess.Popen`, 其初始化函数(构造函数)参数如下:

~~~python
__init__(self, args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)
~~~

实际上初始化后就可以使用该对象的属性和方法来处理命令的执行结果.常用的是args(就是具体命令), stdin, stdout, stderr, shell这几个.
如果command不是一个可执行文件，*shell=True*不可省。

~~~python
import subprocess as sub
handle = sub.Popen('your command',stdout=sub.PIPE,stderr=sub.PIPE)
handle = sub.Popen('ls -l', stdout=sub.PIPE, shell=True)
handle = sub.Popen(['ls','-l'], stdout=sub.PIPE, shell=True)
handle = sub.Popen(args='ls -l', stdout=sub.PIPE, shell=True)
output, errors = p.communicate() ##返回值是(stdout,stderr).还可以带参数input作为stdin
print output
print handle.stdout.read()
~~~

#### call

`subprocess.call(["some_command","some_argument","another_argument_or_path"..])`

调用命令并等待命令执行,返回其返回值,类似于os.system().

#### check_output

另外也可以更方便地使用使用**check_output**函数, 返回值是stdout. 若要同时返回输出值,加入`stderr=STDOUT`(否则可忽略): 

`output = subprocess.check_output(["command", "arg1", "arg2", ....],stderr=STDOUT);` 

### 方法4: webbrowser.open

前面三个方法只能用于执行程序和打开文件，不能处理URL，打开URL地址可用webbrowser模块提供的功能。

使用命令: `webbrowser.open(url)`来调用系统缺省浏览器打开URL地址，也可以利用该方法来
来执行支持的程序。这样可以不必区分是文件名还是URL，不知道在Linux下是否可行。

~~~python
import webbrowser
webbrowser.open('http://www.google.com') ##URL地址
webbrowser.open('h:\python.zip') ##打开文件
~~~


### 其余方法: 

#### wx.Execute

在wxPython中, 可以使用`wx.Execute(command, syn=wx.EXEC_ASYNC, callback=None)`.wx为该版本中的自带库.相应不同的编译器也可能有类似方法.非标准,只是一提.

若置syn为wx.EXEC\_ASYNC则wx.Excute函数立即返回，若syn=wx.EXEC\_SYNC则等待调用的程序结束后再返回。

callback是一个wx.Process变量，如果callback不为None且syn=wx.EXEC_ASYNC，则程序结束后将调用wx.Process.OnTerminate()函数。

os.system()和wx.Execute()都利用系统的shell，执行时会出现shell窗口。如在Windows下会弹出控制台窗口，不美观。




















------
