---
layout: post
title: 判断Bash指令存在与否
date: 2015-08-17 09:22:54
categories: Coding
tags: Bash
---

## 使用which

使用which两有个trick:
- 第一,找不到stderr会告诉你在环境变量中找不到. 所以要将错误重定向. 
- 第二, 这里which commd 不能加入`` ` ``号. 否则会变成运行后面的指令...`` `which gcc` ``和`$(which gcc)`都会运行gcc, 而`[ which gcc ]` 则会报语法错..

~~~bash
if which brew 2>/dev/null; then
  echo "brew exists!"
else
  echo "nope, no brew installed."
fi
~~~

或者通过返回值判断:

~~~bash
which brew >/dev/null 2>&1
if [ $? == 0 ]; then
  echo "brew exists!"
else
  echo "nope, no brew installed."
fi
~~~

## 使用-x

-x是判断一个命令是否存在于PATH并且是可执行的.

~~~bash
if ! [ -x "$(command -v git)" ]; then
  echo 'git is not installed.' >&2
fi
~~~


## 使用另外一些内建命令

有时候有些系统没有which, 有些which不会设置有效的退出状态, 此时可能出现兼容问题.

~~~bash
command -v foo >/dev/null 2>&1 || { echo >&2 "I require foo but it's not installed.  Aborting."; exit 1; }
type foo >/dev/null 2>&1 || { echo >&2 "I require foo but it's not installed.  Aborting."; exit 1; }
hash foo 2>/dev/null || { echo >&2 "I require foo but it's not installed.  Aborting."; exit 1; }
~~~

这个用法参考[stackoverflow的解答](http://stackoverflow.com/questions/592620/check-if-a-program-exists-from-a-bash-script). 推荐用法, 但这三个命令不常用啊...

如果不存在指令, 就可以结合下面来自定义一套: 

~~~bash
shopt -s  expand_aliases ; alias fn="command"
~~~

------
