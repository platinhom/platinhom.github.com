---
layout: post
title: Python:重定向输出
date: 2015-11-07 01:28:46
categories: Coding
tags: Python
---

今天用openbabel时想将其标准输出弄走(因为我要自己print的结果..).查询后python也可以重定向输入输出. 虽然尝试了, 但还是失败..但是重定向还是很有用滴.

## python的标准输入/输出/错误

在python中, 标准输入/输出/错误以文件句柄的形式保存, 换句话说, 标准输出和标准错误相当于往文件句柄写入, 而标准输入则从文件句柄中读取.

python中标准输入/输出/错误储存在sys模块三个属性中:

- sys.stdout: 标准输出, 名字为`<stdout>`的文件句柄.关闭会出错. `<open file '<stdout>', mode 'w' at 0x107448150>`
- sys.stdin: 标准输入, 名字为`<stdin>`的文件句柄. `<open file '<stdin>', mode 'r' at 0x1074480c0>`
- sys.stderr: 标准错误, 名字为`<stderr>`的文件句柄. `<open file '<stderr>', mode 'w' at 0x1074481e0>`

#### 对于print语句, 实际等于:

~~~python
sys.stdout.write('hello'+'\n')
print 'hello'
~~~

即写入到标准输出sys.stdout 加上 换行符`\n`.

#### 对于raw_input函数, 实际等于

~~~python
hi=raw_input('hello? ')

print 'hello? ', #comma to stay in the same line
hi=sys.stdin.readline()[:-1] # -1 to discard the '\n' in input stream
~~~

即从标准输入sys.stdin 读取下一行 (忽略`\n`). 因为函数有提示符所以实际还有输出的效果.

## 重定向

和shell重定向单纯用`< , >`不同, python的重定向其实就是将标准输入/输出/错误作为文件句柄来操作, 所以要实现重定向, 首先需要将相应标准输出存于一变量, 更改sys.stdout到指定文件, 操作完后将原来的标准输出设回sys.stdout即可. 

### 从标准输出重定向到文件

将相应文件先打开, 使用**写入**模式. 并将文件句柄赋给sys.stdout即可. 用完记得设回原来的stdout.

~~~python
stdo=sys.stdout
# need a file handle with write mode
fhandle=open("out.txt",'w');
sys.stdout=fhandle

print "I'm the output~"
......
# reset the standard output
sys.stdout=stdo
~~~

### 同时重定向到文件和屏幕

要实现该功能,其实关键需要使用一个类对象具备write方法. 例如如下:

~~~python
class stdoutfile(object):
	# temp stdout
	console=None;
	fhandle=None;

	# save the stdout when initial
	__init__(self,fhandle):
		self.console=sys.stdout
		self.fhandle=fhandle

	# define write method to output to file and screen
	write(self, string):
		self.console.write(string)
		self.fhandle.write(string)

	# reset the stdout
	reset(self):
		sys.stdout=self.console

f=open("output.log",'w');
sout=stdoutfile(f);
sys.stdout=sout;

# indeed use: sys.stdout.write("Hello world!\n")
print "Hello world!"
sout.reset()
f.close()
~~~

------
