---
layout: post
title: 检查端口状态:netstat和lsof
date: 2015-07-04 01:44:04
categories: Coding
tags: System Internet
---

因为最近经常碰网络, 应用经常会占用网络端口, 有时就导致程序启动不了.这里介绍怎么检查端口,知道端口占用,被何占用.

## Window版

目标：在Windows环境下，用`netstat`命令查看某个端口号是否占用，为哪个进程所占用.
操作：操作分为两步

1. 查看该端口被那个PID所占用;方法一：有针对性的查看端口，使用命令 `netstat –ano|findstr “<端口号>”`,如图，最后一列为PID。图中的端口号为1068，所对应的PID为3840。  
![](http://dl.iteye.com/upload/attachment/164587/18a81821-7c08-36b1-a23a-026ff1d5c027.jpg)  
2. 查看该PID对应的进程名称。
  - 用命令查找，`tasklist|findstr “<PID号>”`
  - 任务管理器,调出PID显示进程
3. 可以用命令`ntsd -c q -p "PID"`或者任务管理器终止进程.

在命令行中输入netstat /? 可以查看netstat的相关信息。
netstat 显示协议统计信息和当前 TCP/IP 网络连接。

`NETSTAT [-a] [-b] [-e] [-n] [-o] [-p proto] [-r] [-s] [-t] [-v] [interval]`

-  -a            显示所有连接和监听端口。
-  -b            显示包含于创建每个连接或监听端口的可执行组件。在某些情况下已知可执行组件拥有多个独立组件，并且在这些情况下包含于创建连接或监听端口的组件序列被显示。这种情况下，可执行组件名在底部的 [] 中，顶部是其调用的组件，等等，直到 TCP/IP 部分。注意此选项可能需要很长时间，如果没有足够权限可能失败。
-  -e            显示以太网统计信息。此选项可以与 -s选项组合使用。
-  -n            以数字形式显示地址和端口号。
-  -o            显示与每个连接相关的所属进程 ID。
-  -p proto      显示 proto 指定的协议的连接；proto 可以是下列协议之一: TCP、UDP、TCPv6 或 UDPv6。如果与 -s 选项一起使用以显示按协议统计信息，proto 可以是下列协议之一:IP、IPv6、ICMP、ICMPv6、TCP、TCPv6、UDP 或 UDPv6。
-  -r            显示路由表。
-  -s            显示按协议统计信息。默认地，显示 IP、IPv6、ICMP、ICMPv6、TCP、TCPv6、UDP 和 UDPv6 的统计信息；-p 选项用于指定默认情况的子集。
-  -t            显示当前连接卸载状态。
-  -v            与 -b 选项一起使用时将显示包含于为所有可执行组件创建连接或监听端口的组件。
-  interval      重新显示选定统计信息，每次显示之间暂停时间间隔(以秒计)。按 CTRL+C 停止重新显示统计信息。如果省略，netstat 显示当前配置信息(只显示一次)

## Linux和Mac

- 利用lsof命令,通用. `lsof -i :PIDnum` 
- Linux使用 	`netstat -anp | grep PIDnum`
- MacOSs使用 `netstat -anp tcp | grep PIDNum` 虽然可以列出端口占用情况,但是不显示那个程序占用.

---
