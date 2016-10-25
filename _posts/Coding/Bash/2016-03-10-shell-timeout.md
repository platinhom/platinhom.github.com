---
layout: post
title: Shell:timeout
date: 2016-03-10 11:50:46
categories: Coding
tags: Bash
---

今天交任务, 想避免某些死任务卡死(会一直耗下去, 还没有结果),想设置一个时间限制, 使得超时后自动kill任务. 部分系统Shell提供`timeout`命令来实现该功能, 没有的话就要自己写函数咯.

-----

## timeout命令

`timeout [OPTION] NUMBER[SUFFIX] COMMAND [ARG] ...`

- `NUMBER` 就是超时限定的时间, 例如30就是30秒
- `SUFFIX` 就是时间单位, 默认是`s`秒, 也可以是`m`分钟, `h`小时, `d`天. 例如30m就是30分钟
- `COMMAND [ARG]` 就是要执行的命令咯 
- OPTION部分主要是 `-s`, `--signal`, 使用该选项可以指定`kill`时使用的信号, 默认是TERM.
- 正常终结command就返回命令的返回码, 否则被中断返回124. 

-----

自定义timeout函数:

~~~bash
#! /bin/bash
function timeout() {
waitsec=5
# submit command in background and save pid
( $* ) & pid=$!
# timeout 
( sleep $waitsec && kill -HUP $pid ) 2>/dev/null & watchdog=$!
# wait command, if normal, kill the watch timeout
if wait $pid 2>/dev/null; then
    pkill -HUP -P $watchdog
    wait $watchdog
fi
# else: command interrupted
}
timeout sleep 10
~~~

------
