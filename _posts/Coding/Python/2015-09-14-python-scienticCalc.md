---
layout: post
title: python科学计算软件安装
date: 2015-09-14 07:01:29
categories: Coding
tags: Python
---

Mac安装:
先安装homebrew

然后

~~~bash
brew install python --framework --universal #fw是告诉是一个框架用于安装别的东东.universal是32/64都装
easy_install pip  ##可能已经会安装上了

## 以下是科学计算一般需要的库
pip install numpy
pip install scipy
pip install ipython
pip install matplotlib
pip install pandas
pip install sympy
pip install nose
~~~

## ipython

这是个替代传统默认python终端的终端,优点相比传统idle优点多多: 

1. 支持tab补全属性/函数/变量.
2. 支持函数/方法参数直接提示.
3. 非python标准的输入和控制,例如`%`神奇命令以及`!`外部命令

### 安装

有很多安装方式.最常用方便是pip安装方法.也可以利用软件包安装管理工具来安装.可以[参考](http://ipython.org/install.html).  

- 使用pip安装:

一般现在的python安装包都会安装上pip, unix基础的更加常装上了. [Window安装setuptool和pip参考](http://docs.python-guide.org/en/latest/starting/install/win/)

在window下运行pip需要在dos下运行`python -m pip install package` (python -m pip <command>)
如果把 *python/Scripts* 加入到环境变量可以直接运行`pip install package`， 这里安装ipython所以pip install ipython

~~~bash
pip install ipython
pip install "ipython[notebook]"
pip install pyreadline
~~~

要是装有但有问题,可以用`pip install ipython --upgrade` 来升级

PS: 要是提示以下就要安装后面的`pyreadline`,否则可以不装. 这个pyreadline可以使得ipython支持tab补全等. 比较重要.

~~~bash
WARNING: Readline services not available or not loaded.
WARNING: Proper color support under MS Windows requires the pyreadline library.
You can find it at:
http://ipython.org/pyreadline.html
~~~

- 使用setup.py
	- 


另外一些Python发布版本包含部分python包的也装有ipython,例如Continuum的[ANACONDA](http://continuum.io/downloads)以及Enthought的[Canopy](https://store.enthought.com/downloads/#default)等.

### 启动

支持三种启动模式: shell, qtconsole和notebook. notebook需要额外安装,qtconsole需要额外安装qt,pyqt依赖. 如果不需要图形界面或者网络界面, 只是使用命令行, 可以忽略后面的这部分.

#### Shell模式

就是启动时直接`ipython`.功能已经很强大了.但是缺点是终端不能出图显示图像结果.已经支持各种补全.

#### qtconsole模式

基于QT写图形界面,类似于普通IDLE. 快捷键等支持, 支持出图了~  
要使用qtconsole,就需要装上jupyter, qt, sip, pyqt几个东西.否则报错说No module或者Qt library找不到.

~~~bash
pip install jupyter
brew install qt
brew install sip
brew install pyqt
~~~
运行[qtconsole](http://ipython.org/ipython-doc/stable/interactive/qtconsole.html?highlight=qtconsole)使用命令行命令: `ipython qtconsole`

qtconsole一共有3种启动方式，详见[interactive qtconsole](http://ipython.org/ipython-doc/dev/interactive/qtconsole.html)。

- 不加参数。用matplotlib画的图会调用后台的其他图形化程序打开。
- –pylab。默认同1，但是用`display`函数能让图在qt界面里画上。
- –pylab=inline。画的图直接就在qt界面上显示了。

在window当中,可以使用以下vbs脚本来启动ipython qtconsole,并带上配置!双击运行vbs脚本即可~   
其实使用快捷方式加入命令参数也行,避免黑色dos的方法: 创建pythonw.exe的快捷方式,修改属性为:起始位置:`C:\Python27\Scripts`，目标改成`C:\Python27\pythonw.exe ipython.exe qtconsole --pylab=inline --ConsoleWidget.font_size=12`即可.会有dos闪过,所以还是推荐vbs脚本.

~~~
DIM objShell
set objShell=wscript.createObject("wscript.shell")
iReturn=objShell.Run("C:\Python27\Scripts\ipython.exe qtconsole --pylab=inline --ConsoleWidget.font_size=12", 0, TRUE)
~~~

##### 修改配置

`ipython profile create` 命令的输出会告诉你创建的profile的位置。得到的文件夹后缀是DEFAULT，即启动时会载入的默认配置。在这里找到qtconsole相关的配置文件改就行了。

更多细节参看[configuration](http://ipython.org/ipython-doc/3/config/index.html)

#### notebook模式

支持浏览器多tab,每个tab是一个终端.比较潮.还支持远程.

运行[notebook](http://ipython.org/notebook.html)使用命令行命令: `ipython notebook`.

~~~bash
pip install jupyter
pip install "ipython[notebook]"
~~~

要是`No module named notebook.notebookapp`就要`pip install jupyter`安装一个附加工具[jupyter](http://jupyter.org/).

### 使用

- 可以使用**ctrl+enter**达到多行代码的输入，再一起执行。
- 快速帮助: `obj?`, `obj??`, `?obj`, `??obj`.还支持?foo.\*abc\*这样列出匹配方法/属性.
- 调用系统指令: `!command`  
可以直接调用系统指令(指令取决于运行环境,例如msys启动就使用ls), 并且支持 **将指令返回值赋值给变量!**,如:

~~~python
a=!ls
a
['hi.txt','hehe.txt']
~~~

神奇命令(部分按esc退出)

- `%magic` 查看所有的神奇指令
- `%edit` 编辑并执行文件。编辑器取决于EDITOR环境变量.
- `%pwd` 显示当前目录。
- `%pdoc modulename` 显示模组/方法的文件. 等价于 `modulename ?`
- `%psource modulename` 或 `%pfile modulename`. 显示程序源码.
- `%time statement` 计算运行時間。

更多神奇命令以及ipython使用请参考[Ipython-quick-ref-sheets](http://damontallen.github.io/IPython-quick-ref-sheets/) (也可以使用`%quickref`来查看).

-----

scipy官网推荐使用懒人用macports安装办法.需要先安装macports,使用port命令:

`sudo port install py27-numpy py27-scipy py27-matplotlib py27-ipython +notebook py27-pandas py27-sympy py27-nose`
这样就会一次性自动安装好多好多相关程序.


## Reference

1. [iPython](http://ipython.org/index.html)
2. [SciPy](http://www.scipy.org/index.html)
3. [Installing Python, virtualenv, NumPy, SciPy, matplotlib and IPython on Lion or Mountain Lion](http://www.thisisthegreenroom.com/2011/installing-python-numpy-scipy-matplotlib-and-ipython-on-lion/)

------
