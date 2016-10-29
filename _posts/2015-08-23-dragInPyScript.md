---
layout: post
title: 使Python脚本支持拖动文件执行处理
date: 2015-08-23 12:37:47
categories: Coding
tags: Python
---

我记得我以前使用Python时可以很方便把文件拖过去直接执行的.但貌似在win7现在不行,十分奇怪;但正常命令行输入是可以的.  

网上找半天没找到办法.经过check发现, 其实原因是因为IOError:

`IOError: [Errno 2] No such file or directory: '...'`

执行时,若是处理拖动的文件, 会瞬间弹出以上报错.经过分析发现, 拖动时, python脚本会在c:/windows/system32内. 而不是在脚本所在目录或者文件所在目录...

~~~python
import os,sys
print os.getcwd()
for i in sys.argv:
	print i
raw_input()

# 拖动文件后结果
# -> C:\Windows\system32
# -> C:\Users\Hom\Desktop\test.py
# -> C:\Users\Hom\Desktop\data.txt
~~~

所以执行例如open,mkdir语句时进行读写, 没有绝对路径那是会死的.

例如以下例子:

~~~python
datasheet=["BZ2A","MZ2A","GZ2A","SZ2A"]
fname=sys.argv[1]
fnamelist=os.path.splitext(fname)
fr=open(fname)
nowdoing="";
fw=open(fname);
for line in fr:
	tmp=line.strip().split()
	if (len(tmp)==0):continue
	if(tmp[0] in datasheet):
		nowdoing=tmp[0];
		if (fw):
			fw.close()
		if (not os.path.exists(nowdoing)):
			os.mkdir(nowdoing);
		fw=open(nowdoing+"/data.txt",'w');
		continue;
	fw.write(line)
fw.close();
fr.close();
# Whether to do for test case
needtest=False;
totalpar=open("totalpar.txt",'w');
#......
~~~

这个脚本内的问题很多,在命令行时是没有问题, 拖动肯定就出事了.

`os.mkdir(nowdoing)` 在哪个目录新建? 当前目录!  
`totalpar=open("totalpar.txt",'w');` 想在system32内写文件?!!呵呵  

注意`fr=open(fname)`是没有问题的.

所以啊, 如果python脚本想用于拖动处理, 应该用以下办法进行:

## 更改当前目录

~~~python
import os,sys
print os.getcwd()
for i in sys.argv:
	print i

startdir=os.getcwd()
if (len(sys.argv)>1 and os.path.exists(sys.argv[1])):
	os.chdir(os.path.dirname(sys.argv[1]))
else:
	os.chdir(os.path.dirname(sys.argv[0]))
print os.getcwd()
#....
os.chdir(startdir)

raw_input()
~~~

这个处理中, 若是有参数并且是文件, 则使用该文件的目录进行更改, 否则按脚本名进行更改路径.因为脚本名总是存在的,所以不用担心else后会报错.  
`len() and os.path.exists()` 因为前面错了就会短路不执行后面一句, 所以不必担心.  
`startdir=os.getcwd() ...os.chdir(startdir)` 是用来返回原文件夹的.  

这样处理是OK, 但是也会有点问题...例如我数据在 hi\data.txt, 我想在另一文件夹hehe内处理数据: ./test.py ../hi/data.txt 这样的话处理数据会永远在hi里面而不是hehe里面...所以除非脚本是专门设计来处理

## 利用绝对路径

其实和上面的处理大同小异. 不过不用在文件夹内跳来跳去.先具体获得某个文件夹,然后操作的文件/文件夹使用绝对路径即可.

这里可以使用os.sep获得分隔符,也可以使用os.path.join(path,name)来获得绝对路径

~~~python
jobdir='.'
if (len(sys.argv)>1 and os.path.exists(sys.argv[1])):
	jobdir=os.path.dirname(sys.argv[1])
else:
	jobdir=os.path.dirname(sys.argv[0])
os.mkdir(jobdir+os.sep+nowdoing)
totalpar=open(os.path.join(jobdir,"totalpar.txt"),'w')
~~~

不过在拖放时依然难以避免system32写操作权限的问题.

## 改注册表

根据这个[帖子](https://mindlesstechnology.wordpress.com/2008/03/29/make-python-scripts-droppable-in-windows/), 还有可能是注册表问题, 需要写入以下内容到注册表:

~~~
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Python.File\shellex\DropHandler]
@=”{60254CA5-953B-11CF-8C96-00AA00B8708C}”

[HKEY_CLASSES_ROOT\Python.NoConFile\shellex\DropHandler]
@=”{60254CA5-953B-11CF-8C96-00AA00B8708C}”

[HKEY_CLASSES_ROOT\Python.CompiledFile\shellex\DropHandler]
@=”{60254CA5-953B-11CF-8C96-00AA00B8708C}”
~~~

第一个是py结尾的, 第二个是pyw结尾的, 第三个是pyc.



------
