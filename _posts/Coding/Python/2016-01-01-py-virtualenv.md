---
layout: post
title: Python:virtualenv
date: 2016-01-01 10:18:31
categories: Coding
tags: Python
---

考虑了很久元旦这篇补些啥呢? setup.py? 虚拟环境? 还是游记? 最后还是决定写个虚拟环境吧, 简单~~

-----

> 在集群或者别的公共服务器, 权限是个大问题. 因为权限的问题, 我们没法将Python的一些下载模块安装到默认的地方. 自行下载安装文件修改再安装又太麻烦不方便. 而我又想在HPCC里使用像requests这样的常用模块怎么破呢?

在网上最后找到了HPCC使用自行安装Python模块的方法: [Using Python virtualenv on the HPCC](https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2013/03/06/Using+Python+virtualenv+on+the+HPCC), 简单点说, 就是利用虚拟环境`virtualenv`.

`virtualenv`的介绍可以查看[PyPI](https://pypi.python.org/pypi/virtualenv)上的介绍. [Github](https://github.com/pypa/virtualenv)和主页说明戳[这里](https://virtualenv.pypa.io/en/latest/). virtualenv说白了就是建立一个独立的python运行环境, 将库独立开来.可以完成:

1. 权限不允许下安装新模块到虚拟环境
2. 不同版本的模块安装在不同的虚拟环境方便调换
3. 不同模块有冲突的模块依赖关系

-------

先简单介绍HPCC上virtualenv的使用. 

一般模块使用`module spider py` 查找python相关的模块(一般都带有py). 更多更详细可以用`module avail`查看(不仅python,包括基于OpenMPI等的可用模块也会列出来).但一般预装的模块不多.

可以在加载完已装模块后再设置虚拟环境!! 例如`module load NumPy`那么虚拟环境对应的就有numpy了(但下次还是需要加载一次NumPy再加载虚拟环境..).

安装使用虚拟环境很简单

~~~bash
# Install virtualenv at the first time
virtualenv ~/myPy
# Load the virtualenv
source ~/myPy/bin/activate
# Then you will see you are in myPy, just like that
Hom@HPCC $
(myPy)
# To install new module
pip install requests
(myPy)
# To close the virtualenv
deactivate
~~~

1. 使用`virtualenv`命令安装和设置一个虚拟环境. 后面是该环境所在的路径(会新建一个目录)
2. `source`加载该虚拟环境下的`bin/activate`进行加载.
3. 加载后, 提示行下面会出现虚拟环境名
4. 安装软件可以使用`easy_install` 或 `pip`
5. 退出虚拟环境使用`deactivate`

事实上,在该虚拟环境文件夹中含有以下内容:

- `bin`: 可以使用的可执行文件(包括easy_install, pip, python, 安装的可执行脚本) 和激活用的脚本`activate`. 
- `include`: 内有一python文件夹, 内含相关需要的头文件`.h`, 实际指向实际环境里的`include/python2.7`
- `lib`: 就是一个python的lib文件夹, 虚拟环境的`环境`所在, 包括`site-packages`和一堆基础的py库. 在默认系统内就有的就软链接指过去.
- `lib64`: 在64位系统实际指向lib.

卸载该虚拟环境就`rm -rf 该文件夹`就好了.

-------

## 安装virtualenv

安装virtualenv需要系统装有`pip`和`setuptools`系列模块, 如上所述, 其生产的bin文件夹需要这些玩意.

- 自行使用`pip`自动安装虚拟环境(需要权限)

`[sudo] pip install virtualenv`

- 如果不用pip可以用`curl`进行全局安装

~~~bash
curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-X.X.tar.gz
tar xvfz virtualenv-X.X.tar.gz
cd virtualenv-X.X
[sudo] python setup.py install
~~~

- 甚至可以不进行全局安装, 而是安装到本地再进行运行: 

~~~bash
curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-X.X.tar.gz
tar xvfz virtualenv-X.X.tar.gz
cd virtualenv-X.X
python virtualenv.py myPy
~~~

就这么简单了. 使用就参考上面HPCC的说明就好了. That's ALL~ Happy New Year and have a good year!

------
