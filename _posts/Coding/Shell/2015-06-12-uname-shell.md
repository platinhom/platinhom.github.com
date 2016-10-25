---
layout: post
title: 操作系统判断的指令:uname
date: 2015-06-12 04:58:18
categories: Coding
tags: Shell Bash System
---
## uname for system OS judgement

- 用来检查系统信息,包括系统,版本,内核,硬件架构,节点名等. 在做系统判断时常用.
- 各选项在不同系统的结果可以参看[wiki:uname](http://en.wikipedia.org/wiki/Uname)


一般系统选项: (默认是`-s`)

~~~~
  -a, --all    以如下次序输出所有信息。其中若 -p 和 -i 的探测结果不可知则被省略：
  -s, --kernel-name    输出内核名称(Linux)
  -n, --nodename    输出网络节点上的主机名
  -r, --kernel-release    输出内核版本
  -v, --kernel-version    输出内核发行时间
  -m, --machine    输出主机的硬件架构名称(和64位,32位有关)
  -p, --processor    输出处理器类型或“unknown”
  -i, --hardware-platform    输出硬件平台或“unknown”
  -o, --operating-system    输出操作系统名称(GNU/Linux)
      --help     显示此帮助信息并离开
      --version  显示版本信息并离开
~~~~
注意:在Mac中,`-s`输出是操作系统,和linux基本一致. 没有了`-i,-o`选项

Mac版本(默认是`-s`):

~~~~
     uname -- Print operating system name
SYNOPSIS
     uname [-amnprsv]
DESCRIPTION
     The uname utility writes symbols representing one or more system characteristics to the standard output.
     The following options are available:
     -a      Behave as though all of the options -mnrsv were specified.
     -m      print the machine hardware name.
     -n      print the nodename (the nodename may be a name that the system is known by to a
             communications network).
     -p      print the machine processor architecture name.
     -r      print the operating system release.
	 -s      print the operating system name.
	 -v      print the operating system version.
~~~~

## `arch`: print machine hardware name (same as `uname -m`)
特殊的uname指令专用于硬件架构(32位 or 64位).一般是`x86_64`,`i386`这样. Mac中有更多选项.

###  以下小脚本内容用于系统判断的示例

~~~~ bash
sysOS=`uname -s`
if [ $sysOS == "Darwin" ];then
	echo "I'm MacOS"
elif [ $sysOS == "Linux" ];then
	echo "I'm Linux"
else
	echo "Other OS: $sysOS"
fi
~~~~

---
