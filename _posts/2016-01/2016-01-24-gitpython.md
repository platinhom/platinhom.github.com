---
layout: post
title: GitPython
date: 2016-01-24 12:15:14
categories: IT
tags: Python Git
---

[GitPython](https://pypi.python.org/pypi/GitPython/1.0.1) ([Github](https://github.com/gitpython-developers/GitPython))是Python中可以实现Git功能的模块, 比较成熟, 用起来比较方便. [官方说明文档](http://gitpython.readthedocs.org/en/stable/)也比较全面.

类似的还有[pygit2](https://github.com/libgit2/pygit2), pygit2是基于[libgit2](https://github.com/libgit2/libgit2)的可动态链接库的. [libgit2项目](https://github.com/libgit2)是比较早的基于C++的Git库, 也算比较成熟了. 但是, 我在本机(Win7 64位)下安装时失败, 先是说缺了VS C++ 9.0, 安装后又说缺了个头文件. 哎, 不弄了. 估计要先装Cmake, 然后编译libgit2, 然后再弄pygit2... 麻烦就不弄了. 不过一些libgit2的教程倒是可以参考参考示例, 可以相应用到GitPython中去(理念差不多). Pro Git也有对libgit2的[介绍](http://git-scm.com/book/zh/v2/%E5%B0%86-Git-%E5%B5%8C%E5%85%A5%E4%BD%A0%E7%9A%84%E5%BA%94%E7%94%A8-Libgit2)

另外还有个叫[Dulwich](https://github.com/jelmer/dulwich)的, 是通过纯Python实现Git功能(GitPython有很多是通过Git命令然后通过解析输出来实现的, 例如`git diff`). 比较底层, 文档说明示例很少, 接口太底层用起来不怎么方便. 

## 安装

安装就是`pip install gitpython`咯, 喜欢还可以下载源码然后`python setup.py install`. 

安装依赖: `async`, `smmap`, `gitdb`. 

克隆库可以: `git clone https://github.com/gitpython-developers/GitPython`

在python中引入模块一般使用 `import git` 或者 `from git import *`. 功能和类都在里面了.

## 简要使用

GitPython的主要对象体是Repo这个类, 对应一个Repo仓库. 初始化可以指明该仓库的文件夹路径(主要是文件夹名就可以了, 例如当前文件夹就是`repo=Repo('.')`).

在Repo仓库类里有各种对象和方法. 例如常见的index类(对应一个索引区), remote对象等.

一般实现一次提交, 可以如下操作:

1. 创建Repo实例
2. 使用repo对象的index索引区对象, 进行add/rm操作, 将文件添加到缓存区.
3. 使用index的`commit([comment]`)方法将修改加到本地
4. 获取远程主机对象(`repo.remotes.远程机名`, 如origin) 
5. 使用远程主机对象的push/pull功能                                                                                                                                                                              
要是更多细节和问题, 可以查阅[官方说明](http://gitpython.readthedocs.org/en/stable/tutorial.html#the-index-object)                       

~~~python
#! /usr/bin/env python

import os,sys,glob
from git import *

repo=Repo('.')
index=repo.index
index.add(repo.untracked_files)
newcommit=index.commit('Regular')
origin=repo.remotes.origin
origin.push()
~~~

先创建Repo对象, 随后对其index区进行add操作(这里使用只添加文件的方法, 对修改的文件无能为力.)

## 常用功能

- Repo(仓库路径): (注意大小写)
- repo.heads 查询头和当前头 
- repo.commit 当前的commit的对象, 返回对象时有对应有其SHA-1值. hexsha对应是sha值, parents是祖先的commit对象, author是Actor类的对象(用户名和邮箱), message就是提交commit时对应的message罗.
- repo.remotes.origin 对应是远程仓库origin, 如果有多个远程仓库可以明确指出(这里remotes是个list, 方法对应是list方法, 但是可以通过`.仓库名`获取的远程仓库.
). 远程仓库可以使用例如`fetch()`,`push()`, `pull()`方法.
- repo.index 索引区, 可以使用`add([文件列表])`来模拟git add功能

更多的参考[GitPython git python 的开发库](http://my.oschina.net/hopeMan/blog/141221?fromerr=7BkYbssm) 这个帖子里介绍吧, 挺详细的. 需要再慢慢学和补充...

## Reference

1. [使用 pygit2 创建提交](http://lilydjwg.is-programmer.com/2012/6/20/use-pygit2-to-make-a-commit.34261.html)
2. [Pro Git 2 : Libgit2介绍](http://wiki.jikexueyuan.com/project/pro-git-two/libgit2.html)
3. [GitPython的簡單說明](http://www.xlgps.com/article/354053.html)
4. [GitPython git python 的开发库](http://my.oschina.net/hopeMan/blog/141221?fromerr=7BkYbssm)

------
