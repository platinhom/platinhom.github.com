---
layout: post_small
title: Python标准库小结
date: 2015-09-11 19:23:42
categories: Coding
tags: Python
---

以前总结的一些库及用到的函数.

## 加载库

- import module
- import module1,module2,module3.....
- import module as abc
- from module import function
- from module import *

## 各种库

### import os 
普遍的操作系统功能。如果你希望你的程序能够与平台无关的话，这个模块是尤为重要的。

- os.sep 返回系统路径分隔符
- os.altsep 另外可用的系统路径的分隔符,win是/ linux是None(没有可替换)
- os.name 返回系统名称window是nt linux是poxit
- os.curdir 返回当前文件夹的缩写(有用:的)
- os.pairdir 返回母文件夹缩写(有用::)
- os.pathsep 如环境变量path中的分隔符,win下; linux下: 
- os.extsep 文件扩展名标识符,win和linux都是. 还有用/的
- os.linesep 行分隔符，win:'\r\n' linux'\n' os '\r'
- os.defpath 执行文件所在路径，默认.和/bin/
- os.devnull nul设备所在位置
- os.environ 获得系统的所有环境变量. 
- os.getcwd() 返回当前工作目录，即当前Python脚本工作的目录路径。
- os.chdir('path') 改变当前路径,行为语句.
- os.mkdir('dirname') 创建一个文件夹,行为语句.
- os.makedirs('abc/def') 创建递归的文件夹,mkdir不能创建内子文件夹,行为语句.
- os.rmdir('dir') 删除一个文件夹,非空出错,行为语句.
- os.remove('file') 删除文件
- os.removedirs('dir/abc') 删除abc,若dir为空,往上再递归删除.非空出错,行为语句.
- os.listdir() 返回指定目录下的所有文件和目录名。os.listdir('.')列出当前文件夹
- os.rename(old,new) 重命名文件夹或文件,行为语句.
- os.renames(old,abc/new) 重命名文件夹或文件,中间的文件夹可创建,行为语句.
- os.getenv(ENV)和os.putenv(ENV, value)函数分别用来读取和设置环境变量。
- os.system('command') shell下执行一句命令,可以用&串联dos命令(dos下成功运行返回0)
- os.popen(command [, mode='r' [, bufsize]]) -> pipe  执行shell的指令并将其在shell中返回的结果转为一个文件,用个变量保存,用read来读值

常用的路径相关的os.path:

- os.path 返回模组path和其路径path内有很多方法
- os.path.basename('d:/a.txt') 返回文件名‘a.txt’
- os.path.dirname('d:/a.txt') 返回目录名
- os.path.basename(os.path.dirname(p)) 返回上一层的文件夹名字
- os.path.abspath('d:/a.txt') 返回绝对路径=os.path.realpath
- os.path.relpath('d:/a.txt') 返回相对路径
- os.path.split('d:/a.txt') 返回路径和文件名的元组,第一个为path第二个为文件名
- os.path.splitext('d:/a.txt') 返回二元元组,第二个是'.txt'
- os.path.splitdrive('d:/a.txt') 返回二元元组,第一个是'd:'
- os.path.exists(file or path) 是否存在文件，符号链接丢失返回false
- os.path.exists(file or path) 是否存在文件，符号链接丢失返回也返回True
- os.path.isdir(file or path) 返回是否一个文件夹
- os.path.isfile(file or path) 返回是否一个文件
- os.path.join(dir,filename) 返回连接后的名字.使用os.sep作连接
- os.path.walk(path,visit,arg)


### import pexpect 
实现shell命令之间的交互


### import re
正则表达式

- re.match(pattern, string,flags)
- re.search(pattern, string,flags)
- re.sub()
- re.split()
- re.findall()
- re.compile()


### import string 
字符串处理模块,已经被字符串类的方法征服了 ╮(╯▽╰)╭

- string.capitalize(string)    首字母大写
- string.lower(string)    全部小写化
- string.upper(string)    全部大写化
- string.replace(string,old,new[,maxsplit])     字符串中替换,max为最多替换个数
- string.join(string[,sep])  使用分界符(sep,默认空格)将字符串连接起来.
- string.split(string,sep=None,maxsplit=-1) 以sep为分界符将string分开成一个列表


### import shutil
深复制

- shutil.copyfileobj(fsrc, fdst[, length]) 
- shutil.copyfile(src, dst) #上面2个都是文件的复制 
- shutil.copymode(src, dst) #除了复制内容，还会复制其他的一些信息，主要是权限
- shutil.copystat(src, dst) #除了复制内容，还会复制存取时间的信息 
- shutil.copy(src, dst) #复制文件到dst，当dst为目录时，复制到子目录 
- shutil.copy2(src, dst) #相当于先copy再copystat =cp -p
- shutil.copytree(src, dst[, symlinks=False[, ingore=None]]) #复制文件夹树，注意,dst文件夹必须是不存在的 
- shutil.rmtree(path[, ignore_erros[, onerror]])  删除文件树
- shutil.move(src,dst) 移动到目标地点,可用于改名

### import linecache


### import fileinput


### import sys
系统通过命令行输入输出相关

- sys.argv 返回传递系统参数的一个列表,第一个一般是py文件，常配合index+1，[1:]等使用
- sys.path 返回系统参数的路径，若是执行py文件,[0]就是其地址,后面还有python有关地址.因为是list可以用insert,append方法,尤其当需要import某模组时需要.
- sys.exit() 退出系统程序 sys.exit(0)报错退出,返回0作为信号给dos或shell

### import time
时间模块

- Epoch 为时间戳,1970.1.1/8:00:00作为起点，记录过了多久秒
- time.sleep(seconds) 暂停指定秒数
- time.clock() 从程序启动(脚本运行)起持续了的时间(秒)
- time.time() 返回当前时间(秒float)（时间戳起,常用于两时间相减）
- time.localtime([seconds])返回元组结构time.struct\_time(tm\_year=2012, tm\_mon=3, tm\_mday=27, tm\_hour=1, tm\_min=31, tm\_sec=45, tm\_wday=1, tm\_yday=87, tm\_isdst=0)(wday是星期,0-星期一;yday为一年第几日,1~366,tmdst为日照时间变化)。不赋值表示当前时间转化。
- time.ctime([seconds]) 返回字符串'Sat Jun 06 16:26:11 1998',输入秒
- time.asctime([tuple])返回字符串，同上，输入为时间元组.两方法不输入值时默认为当前时间
- time.mktime([tuple]) 转化时间元组变为秒
- time.gmtime([seconds]) 返回时间元组,返回的是GMT格林威治标准时间
- time.strftime(format[, tuple]) 格式化时间元组,返回一字符串. 常用%y 99,%Y 1999,%m 01-12,%d 01-31,%H 0-23,%I 01-12(十二小时制),%M 00-59,%S 00-59,%p AM/PM,%%: %号本身,%a/A: 星期名,%b/B 月份名(小写为三字母简写) 其余参考别的..
- strptime(string[, format]) 常配合ctime类使用,格式化需要'%a %b %d %H:%M:%S %Y'形式(如使用strftime)

### import datetime  
比time要更为复杂和丰富. 注意.datetime和.date区别在于后者只截取日期部分

- datetime.datetime.now() 返回年月日时分秒微秒的7元元组
- datetime.day.today() 返回(年,月,日)元组
- datetime.timedelta(days=10,seconds=100,microseconds=500) 根据括号内实质参数作延时(或用元组),返回的值可用于datetime元组的加减法
- datetime.datetime(2012,3,26) 一个datetime对象
- datetime.datetime.strftime(format[,tuple])
- datetime.datetime.strptime(date-string[,format])
- datetime.tzinfo.*** 时区信息？

### import gc 
garbage collection 回收内存

- gc.collect() 回收无连接的内存
- gc.enable() 自动回收打开
- gc.disable() 自动回收关闭

### import calendar


### import timeit

- timeit.Timer(code)

### import platform
操作系统和当前平台相关

- platform.system()    返回操作系统类型windows,linux,java等
- platform.version() 返回版本号字符串
- platform.uname() 机器和系统的一系列信息
- platform.platform() 返回操作系统及版本信息'Windows-XP-5.1.2600-SP3'
- platform.machine() 返回机器类型,i386,x86等
- platform.architecture() 返回机器架构,('32bit','WindowsPE')
- platform.node() 返回机器在网络中节点名称,也就是机器名称.
- platform.python\_version\_tuple() 返回版本号的元组('2','7','2')主版本,小版本,补丁级数
- platform.python_version() 返回python版本号
- platform.python_compiler() 返回python编译器名
- platform.python_implementation() 返回python安装履行方式,如CPython,IronPython(.Net),Jython等
- platform.popen(cmd, mode='r', bufsize=None): 执行外部命令

### import math
数学函数

- math.fabs(x)
- pi,e 常量


### import glob
搜索文件

- glob.glob(r'filefullname') 搜索文件名，返回文件名的list
- glob.iglob(r'filefullname') 搜索文件名，返回生成器对象iglob

### import copy
复制

- copy.deepcopy(dict) 深复制，字典的复制实在太弱，这个复制是不会改变原字典的


### import textwrap

class TextWrapper(详细见help,不会用)

- textwrap.dedent(text)     去掉行开头的空格和tab,对于多行的,去掉得空格数量取决于最短那行
- textwrap.fill(text,width=70)    转换格式,每行的长度为70，然后换行，返回字符串
- textwrap.wrap(text,width=70)    转换格式,每行的长度为70，然后换行，返回每行为元素的列表

### import multiprocessing

- multiprocessing.cpu_count() 返回本机cpu数量

### import subprocess
子进程, 用来运行别的程序,控制子进程

- subprocess.call(["some_command", "some_argument","another_argument_or_path"])  运行shell命令

### import ctypes

ctypes.windll.user32.SetCursorPos(x,y) 移动鼠标到该位置

### import zipfile
zip压缩文件相关

- f = zipfile.ZipFile(fileName[, mode[, compression[, allowZip64]]]) 创建一对象,和open file差不多,'a''r''w'模式,compression设为zipfile.ZIP_DEFLATED即表示压缩。allowZip64为True表示支持64位压缩,压缩包可大于2G
- f.write('file1.txt');f.close() 添加到压缩文件，关闭压缩文件
- f.extractall([path[, member[, password]]]) 解压缩所有文件,指定path为解压缩目录，member可指明解压某些对象
- zipfile.is_zipfile(filename) 判断是否为压缩文件
- ZipFile.namelist() 返回文件列表
- ZipFile.open(name[, mode[, password]]) 打开压缩包内某个文件,和open一样 
- ZipFile.setpassword(password) 设置密码

### import codecs 字符集?

codecs.lookup(字符集名) 查看有否字符集？

### import win32gui

- win32gui.GetCursorPos() 获知当前鼠标位置

### import pyHook 消息勾(具体参见pyHook一文).

- pyHook.HookManager() # 监听所有键盘事件,用pyhook改变Tkinter会死循环?!
- pyHook.HookManager().KeyDown =onKeyboardEvent 这里,设置按下键时的事件
- pyHook.HookManager().HookKeyboard()	# 设置键盘“钩子”
- pyHook.HookManager().MouseAll =onMouseEvent # 监听所有鼠标事件	
- pyHook.HookManager().HookMouse() # 设置鼠标“钩子


### import ubllib2


### import pythoncom

- pythoncom.PumpMessages()	 # 进入循环，如不手动关闭，程序将一直处于监听状态

### import win32clipboard 剪贴板操作

- win32clipboard.OpenClipboard() 打开剪贴板
- win32clipboard.EmptyClipboard() 清空剪贴板内存
- win32clipboard.SetClipboardData(win32con.CF_TEXT, "Hello World!")  #复制文本内容到剪贴板，系统后台会返回内存地址
- wincb.GetClipboardData(win32con.CF_TEXT)  #'Hello World!'
- win32clipboard.CloseClipboard()

### import win32api 

- win32api.keybd_event(17,0,0,0) 模拟键按下事件,17是ctrl
- win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) 模拟键释放事件,86是V



### import win32con 
win32系统相关的常量.作为很多的辅助调用库

- win32con.KEYEVENTF_KEYUP 键释放,=2

### import httplib

### import ftplib

### import maillib

### import random 
用于生产伪随机数, 以当前时间作为随机数种子

- random.randrange([start], end[, step]) #格式与range()函数一样，随机返回一个在start 与end 之间的一个数。输入输出均是int型
- random.randint(start, end) #产生从start到end的随机整数，包括start与end
- random.uniform(start, end) #作用与randint()一样，但返回结果为float型，且不包括end
- random.random() #没有参数，返回0.0到1.0之间的一个float数，包括上下限
- random.choice(oneList) #从oneList中随机选择一个item返回。random.choice(range(start, end+1))等价于random.randint(start, end)
- random.shuffle(oneList) #对oneList中的项进行洗牌，即打乱顺序。并不返回一个新的list，而是将原list中的数据顺序打乱，所以如果需要以前的数据，记得备份。


## 常用外部库

### import pyperclip  
剪贴板工具.[参见](http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python/), 需下载放到Lib内

- pyperclip.getcb()  获取clipboard值
- pyperclip.setcb(text)  设置clipboard值
 



### import plistlib(>2.6)

## Reference

1. [The Python Standard Library(Official)](http://docs.python.org/library/index.html)




------
