---
layout: post
title: Python模块和包
date: 2015-08-29 13:33:01
categories: Coding
tags: Python
archive: true
---

python没有什么头文件cpp文件之分, 每个py文件都可以作为独立的模块module. 我们应该熟知使用 *import os* 一类语句加载标准模块.这里总结下模块,包等更多东东. 和一般的教材不同, 大家熟悉模块, 这里先介绍包, 概念比较简单, 但对后面模块进一步认识有很大意义.

## 包 package

和C++不同,模块加载是不支持路径形式的, 但我们经常要将很多个模块放在一个文件夹内便于管理.此时python就有了包package的概念. 包其实就是放了很多文件的文件夹特殊模块, 其最大作用是便于加载文件夹内的模块: `import package.module`

包的实质也是个模块.当在加载包内的模块时, 包也会被加载到模块列表中, 此时作为模块加载的内容在文件夹内`__init__.py`内. 

`__init__.py` : 当加载包模块时, 初始化包模块. 用途在于说明该文件夹是个package, 不需特殊加载的话可以留空,但作为包的话必须存在该文件.

## 模块 module

先谈模块搜索路径, 再谈看似很简单的模块加载. 重点是模块与包的加载机制, 有助于了解import的实质.

### 模块的搜素路径: 

1. 当前目录
2. 环境变量`PYTHONPATH`中指定列表依次搜索
3. python安装目录,子目录(如lib/site-packages,plat-win,lib-tk等),相关目录等

可以使用`sys.path`来查看当前的搜索路径. 如常使用建议使用`PYTHONPATH`环境变量来定义.

在机制中,python会搜索Python Home, 由PYTHONHOME给定或者python.exe所在去找, 找到后将导入lib/site.py, 将site-packages目录及其下的包加入.

### 加载模块

加载模块最常用方法有:

~~~python
import module1,module2
import module as mod
from module import sth
from module import *
~~~

模块就是一个py(pyc,pyd)文件, import时不需要文件后缀. 第一种方法加载整个模块(内容且带命名空间); 第二种方法便于缩写(缩写作为命名空间,但实质还是加载相应模块对象,详细看下面一个例子); 第三者选定性加载内容且不需再带命名空间; 第四种方法加载所有东西且没有命名空间 (四种情况的加载机制都请参考下面import 的机制).

每个模块对象都有`__name__`属性(就是文件名不带后缀或者`__main__`),所以常用`if (__name__ == "__main__")`判断是否作为main主程序.

#### 一个比较健壮的加载代码: 

~~~python
import sys;
if not "/home/a/" in sys.path:
    sys.path.append("/home/a/")
if not 'b' in sys.modules:
    b = __import__('b')
else:
    eval('import b')
    b = eval('reload(b)')
~~~

#### 注意点

- 模块不能带路径,例如在a文件夹内的模块b, 不可以 *import a/b*,这时要用包(见下面).  
- 模块加载的路径储存在`sys.path`中.可以将某个文件夹路径加载到该列表中, 从而实现对文件夹内py文件的加载.
- 已加载的模块储存在`sys.modules`一个字典当中,可以对其进行检查模块是否已加载. 字典项是模块名,字典值是其路径(文件名)或内建模块.
- **一个模块不会重复被载入**.模块若已被加载, 再次加载将无效(除非退出主程序或者退出解析器PVM), 这样可以避免重复加载的发生(其实就是检测字典是否有重值). 此时如模块被修改需重新加载, 要用`reload(modname)`重新加载(注意,会优先加载编译过的pyc文件!). 
- 模块加载时,先检查是否加载了,否的话加载并把名称导入到Local命名空间,而已加载的话则将模块名字加入到正在使用的模块的Local命名空间(可用`locals()`查得,全局是`globals()`). **每个模块的Local命名空间是独立的**. import A 时即使内部进行了import B, B模块也只存在A的命名空间,而不在当前命名空间, 这会导致需要B被加载了,但B的内容不能被调用,要使用还是需要明确import B.见下面实例解释.
- 详细的模块和包的加载机制, 请看完下面的例子.

#### import中再import的Local命名空间问题:

~~~python

# 当前目录:
# now.py 
import pkg.mod1
now = 0
print "In now"

# pkg目录下:(包含空白__init__.py)

# __init__.py
p=-1

# mod1.py
import pkg.mod2
m1=1
print "In mod1"

# mod2.py
m2=2
print "In mod2"

# 以下是交互模式下输入, 输出用->表示

import sys
import now
# -> In mod2 ; In mod1 ; In now
# 可见加载顺序是递归的.

print now.now; 
# -> 0; 
# 需要用命名空间now

print pkg.p; print pkg.mod1.m1; print pkg.mod2.m2
# -> Traceback (most recent call last):
# ->  File "<stdin>", line 1, in <module>
# -> NameError: name 'pkg' is not defined
# pkg的名字存在于now模块中,但不存在当前模块! 更别说子模块了.

sys.modules["now"];
# -> <module 'now' from 'now.py'>
sys.modules["pkg"];
# -> <module 'pkg' from 'pkg/__init__.py'>
sys.modules["pkg.mod1"];
# -> <module 'pkg.mod1' from 'pkg\mod1.py'>
sys.modules["pkg.mod2"];
# -> <module 'pkg.mod2' from 'pkg\mod2.py'>
# 可见四个模块都被加载了,

locals()
# -> {'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'sys': <module 'sys' (built-in)>, 'now': <module 'now' from 'now.pyc'>, '__name__': '__main__', '__doc__': None}
# 因为只是加载now,所以里面的子内容都没有加载.

import pkg;locals()
# ->{'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'sys': <module 'sys' (built-in)>, 'now': <module 'now' from 'now.pyc'>, 'pkg': <module 'pkg' from 'pkg\__init__.py'>, '__name__': '__main__', '__doc__': None}
# 新加入了pkg, 但没有子模块.

print pkg.p;print pkg.mod1.m1;print pkg.mod2.m2
# -> -1 ; 1 ; 2
# 第一个很容易理解,因为pkg被加载到locals了. 但mod1和mod2没有啊..? 再做个测试就明白了.

# 退出python, 重头再来
import pkg.mod1
# -> In mod2 ; In mod1

print pkg.p;print pkg.mod1.m1;print pkg.mod2.m2
# -> -1 ; 1 ; 2

locals()
# -> {'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'sys': <module 'sys' (built-in)>, 'pkg': <module 'pkg' from 'pkg\__init__.pyc'>, '__name__': '__main__', '__doc__': None}

# 由此可见,命名空间中即使我import pkg.mod1, 但命名空间中只有pkg! 也就是说,一旦命名空间加入包名,就可以调用包内已加载的模组内容! 

# 退出python, 重头再来
import sys,pkg.mod2
# -> In mod2

print pkg.p;print pkg.mod2.m2
# -> -1 ; 2
print pkg.mod1.m1;
# -> Traceback (most recent call last):
# ->  File "<stdin>", line 1, in <module>
# -> AttributeError: 'module' object has no attribute 'mod1'
# 虽然pkg被加载到Local,但pkg对象没有mod1属性(模组属性)

sys.modules["pkg.mod2"];
# -> <module 'pkg.mod2' from 'pkg\mod2.pyc'> 变pyc了~
sys.modules["pkg.mod1"]
# -> Traceback (most recent call last):
# ->   File "<stdin>", line 1, in <module>
# -> KeyError: 'pkg.mod1'
# 原因还是因为该模组mod1没有载入,不存在于pkg模组的__dict__当中.
~~~

#### 以下是import module as mod的测试,用numpy测试

~~~python
import sys
import numpy as np
sys.modules["numpy"]
# -> <module 'numpy' from 'c:\Python27\lib\site-packages\numpy\__init__.pyc'>
sys.modules["np"]
# -> Traceback (most recent call last):
# ->   File "<stdin>", line 1, in <module>
# -> KeyError: 'np'
# 由此可见, 模组是按原名载入

type(np)
# -> <type 'module'>
type(numpy)
# -> Traceback (most recent call last):
# ->   File "<stdin>", line 1, in <module>
# -> NameError: name 'numpy' is not defined
# 可见, 命名空间只有np而没有numpy
locals()
# -> {'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'sys': <module 'sys' (built-in)>, 'np': <module 'numpy' from 'c:\Python27\lib\site-packages\numpy\__init__.pyc'>, '__name__': '__main__', '__doc__': None}
# 结论也是np命名空间存在代替numpy模块

import numpy
locals()
# -> {'__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'sys': <module 'sys' (built-in)>, 'np': <module 'numpy' from 'c:\Python27\lib\site-packages\numpy\__init__.pyc'>, '__name__': '__main__', 'numpy': <module 'numpy' from 'c:\Python27\lib\site-packages\numpy\__init__.pyc'>, '__doc__': None}
# 再次加载numpy后,numpy并没有实际再次加载创建对象, 但命名空间加入了numpy
~~~

### import的机制

先看个测试例子, 明白这个例子和import的机制,就能明白上面的例子了.

#### 测试交叉引用:

~~~python
# A.py
from B import D
class C:pass

# B.py
from A import C
class D: pass

# Test 1
# 运行:
import A
# -> Traceback (most recent call last):
# ->   File "<stdin>", line 1, in <module>
# ->   File "A.py", line 1, in <module>
# ->     from B import D
# ->   File "B.py", line 1, in <module>
# ->     from A import C
# -> ImportError: cannot import name C

# Test 2
# 外部执行:
python A.py
# -> Traceback (most recent call last):
# ->   File "A.py", line 1, in <module>
# ->     from B import D
# ->   File "c:\Users\Hom\Desktop\B.py", line 1, in <module>
# ->     from A import C
# ->   File "c:\Users\Hom\Desktop\A.py", line 1, in <module>
# ->     from B import D
# -> ImportError: cannot import name D

# Test 3
# 若A.py 中改为import B:
import A
# -> Traceback (most recent call last):
# ->   File "<stdin>", line 1, in <module>
# ->   File "A.py", line 1, in <module>
# ->     import B
# ->   File "B.py", line 1, in <module>
# ->     from A import C
# -> ImportError: cannot import name C

# Test 4
# 外部执行:
python A.py
# -> 
~~~

上面的例子要了解**import的机制**, 以from B import D为例:

1. 在sys.modules中查找符号"B".
2. 如果符号B存在，则获得符号B对应的module对象<module B>。从<module B>的`__dict__`中获得符号"D"对应的对象，如果"D"不存在，则抛出异常.
3. 如果符号B不存在，则创建一个新的module对象<module B>，注意，这时，module对象的`__dict__`为空。执行B.py中的表达式，填充<module B>的`__dict__` 。从<module B>的`__dict__`中获得"D"对应的对象，如果"D"不存在，则抛出异常。

而当import B时:

1. 在sys.modules中查找符号"B"
2. 如果符号B存在，则不再重复加载, 并把B (或者as name)加到命名空间(要是不存在于命名空间).要是as name方式加载,创建新名字映射到B模块对象(所以例子中numpy和np都是指向同一个numpy模块对象)
3. 如果符号B不存在，则创建一个新的module对象<module B>, 并执行B.py表达式, 将产生的子对象/变量等填充<module B>的`__dict__` . 并且和上面情况一样, 创建相应的命名空间并映射到模块对象. 完成后退出.

- 所以执行 *python A.py* 时: 
	1. A.py的from B import D, 创建B模块,并执行B.py来填`__dict__`(此时为空)
	2. B.py的from A import C. 此时从命令行执行,A.py是主程序, 并没有A模块.所以创建A模块,并执行A.py来填`__dict__`(此时为空)
	3. A.py的from B import D, 此时B模块已存在,所以根据上述机制2中所述,不创建B模块了而是从B中`__dict__`中调用D.此时字典为空,不存在D.所以抛错.如Test 2中错误无D的存在.
- 要是执行 *import A* 时:
	1. 创建模组A,执行A.py填空的`__dict__`
	2. B.py的from A import C. 此时已经存在模组A, 所以直接从`__dict__`中加载, 因为为空, 所以报错没有C.如Test 1所示.
- 要是A.py修改为 *import B* , 执行 *import A*, 效果和上面一样,A缺C, Test 3的情况
- 当执行 *python A.py* : 
	1. A.py的import B, 创建B模块,并执行B.py来填`__dict__`(此时为空)
	2. B.py的from A import C, 创建A模块,并执行A.py来填`__dict__`(此时为空)
	3. A.py的import B, B模块已存在, 完成.因为没有再加载D, 所以不报错.此时A和B模块实际仍是空的.

以上示例很好地说明了import的机制.一定要清楚!!!

当测试1 import再import的命名空间时,可以知道**包的import机制**: 

- 不管 *import pkg* 还是 *import pkg.mod1*, 第一步,先import pkg, 执行`__init__.py`内容, 创建命名空间及对应的包模块的对象, 在modules中加载模块.
- 如果*import pkg* 且`__init__.py` 不加载子模块,实际pkg这个包模块对象的`__dict__`是空的, 没有子对象.
- 要是执行*import pkg.mod1*,检测存在pkg模块后则继续执行import子模块pkg.mod1,此时, 不创建命名空间, 但创建对象, **对象绑定到pkg的`__dict__`中**. 在modules中也会加载模块pkg.mod1 来确认已加载避免重复加载

所以, 实际上包模块的加载方式是创建一个整体的pkg模块对象, 再加载子模块到pkg模块对象的`__dict__`中.只要子模块被加载并且母包存在于命名空间,则可被调用.

### 一个实际例子: Pymol 1.7.2.1

当我尝试help('modules')时,报错:

~~~
In [1]: help('modules')

Please wait a moment while I gather a list of all available modules...

/usr/local/lib/python2.7/site-packages/IPython/kernel/__init__.py:13: ShimWarning: The `IPython.kernel` package has been deprecated. You should import from ipykernel or jupyter_client instead.
  "You should import from ipykernel or jupyter_client instead.", ShimWarning)
Error: unable to initalize the pymol.cmd module
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/site-packages/pymol/cmd.py", line 117, in <module>
    from chempy import io
ImportError: cannot import name io
An exception has occurred, use %tb to see the full traceback.

SystemExit: 0
~~~

进一步追踪%tb.

~~~
site-packages/chempy/fragments/__init__.py:
      2 import chempy
----> 3 from chempy import io

chempy/io.py:
---> 21 from chempy.mol import MOL

chempy/mol.py:
---> 19     from pymol import CmdException

pymol/__init__.pyc:
--> 454     from pymol import cmd

pymol/cmd.pyc:
--> 328         sys.exit(0)
~~~

单独import pymol/chempy 均没有问题,但单独运行from chempy import io就报错. 因此局部模块很可能是交叉引用的问题, 

首先在fragments里先import chempy,再chempy.io,此时加载该模块,但里面dict为空,而后面pymol.cmd 又再次加载chempy.io 所以不存在就报错了. 解决办法在cmd.py前面from chempy import io, 前加入import pymol,chempy


> 本博文已合并到[Python语法汇总](/1234/01/01/Python-Language/#more-module-package)中, 不再更新.

------
