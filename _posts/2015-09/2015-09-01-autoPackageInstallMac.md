---
layout: post
title: Mac中自动安装软件的程序
date: 2015-09-01 07:05:12
categories: IT
tags: System
---

## Homebrew

Homebrew是基于ruby的Mac下自动程序安装管理的软件,安装和使用均十分简便,现在基本大部分Mac下安装程序均使用Homebrew完成,首选推荐.更多介绍请参看: Homebrew[主页](http://brew.sh/index_zh-cn.html).

### 安装:

复制敲一句命令即可(不行请自行参看homebrew主页):

~~~bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
~~~

相关程序内容安装在`/usr/local`内,安装后会有一堆相关说明文件.还有一些文件夹

- `/usr/local/Library` : 是homebrew主要相关主程序,brew.rb是其主程序(brew可执行文件其实是个bash脚本).里面的东东不用理=.=
- `/usr/local/Cellar` : 安装的软件包的具体详细安装的文件.
- `/usr/local/bin` : 可执行文件目录,所有安装后直接执行的文件都在这.`/usr/bin`内有原生的程序如clang版g++那些.因此一般版gcc那些可以使用brew来安装(名字可能带gcc-4.9)到/usr/local/bin.
还有其余文件夹,如库文件lib,帮助man,opt,等等.

删除Homebrew:

~~~bash
cd `brew –prefix`
rm -rf Cellar
brew prune
rm -rf Library .git .gitignore bin/brew README.md share/man/man1/brew
rm -rf ~/Library/Caches/Homebrew
~~~

### Homebrew常用命令

- brew search * 		:搜索程序，例：brew search python
- brew install * 		:安装程序，例：brew install python
- brew uninstall * 		:卸载程序，例：brew uninstall python
- brew list 		:列举通过Homebrew安装的程序
- brew update 		:更新Homebrew
- brew upgrade [*] 		:更新某个具体程序，或者更新所有程序
- brew cleanup [*] 		:删除某个具体程序，或者删除所有老版程序
- brew outdated 		:查看哪些程序需要更新
- brew doctor		:检测是否有冲突，同时它会提示一些已失效的库链接.

其他命令

- brew home * 		:用浏览器打开
- brew info * 		:显示软件内容信息
- brew deps * 		:显示包依赖
- brew server * 		:启动web服务器，可以通过浏览器访问http://localhost:4567/ 来同网页来管理包
- brew -h 		:查看帮助

PS:

- 当使用search时可能出现 *Github API Rate limit exceeded* ,就是使用接口太频繁所以限制你使用.解决办法参见[ref](https://gist.github.com/christopheranderton/8644743), 就是在个人设置那里*Personal access token* (推荐把所有flag取消掉再新建), 新设置一个token(generate new token)并将token的值export到环境变量*HOMEBREW_GITHUB_API_TOKEN*, 可以写到*~/.bashrc*中: `export HOMEBREW_GITHUB_API_TOKEN=YOURAPITOKENWITHFUNKYNUMBERSHERE`. (update:15.10.11) 

## MacPorts

MacPorts是一款老款的Mac软件包管理软件,具有更多的库,安装也较独立,缺点是不依赖于系统,很多依赖库需要重装.介绍可以参考[wiki](https://en.wikipedia.org/wiki/MacPorts)

### 安装

安装请参见[官网install](https://www.macports.org/install.php),推荐使用pkg方式下载包后双击直接安装.安装前需要装有XCODE和X11.最好使用`xcode-select --install`, 再装个xcode-select.

安装后,执行文件在`/opt/local/bin`.将其加入到PATH后即可直接运行port命令.安装的程序包执行程序也会放在这里.

删除ports[参考](https://trac.macports.org/wiki/Migration),卸载.


MacPorts常用命令：

- sudo port -v selfupdate : 更新ports tree和MacPorts版本，强烈推荐第一次运行的时候使用-v参数，显示详细的更新过程.
- port search name 		: 搜索索引中的软件.
- sudo port install name 		: 安装新软件.
- sudo port uninstall name 		: 卸载软件.
- port outdated 		: 查看有更新的软件以及版本.
- sudo port upgrade outdated 		: 升级可以更新的软件.
- port -qv installed 		: 查询已安装的软件.

## Fink

类似地,fink也能进行软件包安装和管理,更多参考[主页](http://www.finkproject.org/).

## pip

PIP

安装[参见](https://pip.pypa.io/en/stable/installing/),如果python带有easy_install可以`easy_install pip`.

PIP升级可以: `python -m pip install --upgrade pip`

------
