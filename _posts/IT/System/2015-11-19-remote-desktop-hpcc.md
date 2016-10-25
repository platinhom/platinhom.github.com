---
layout: post
title: 图形界面连接到集群
date: 2015-11-18 23:17:15
categories: IT
tags: System Cluster
---

我们知道window下可以方便地配置远程桌面进行连接, 从另一台window系统电脑连接到开启了远程桌面的电脑上. 因为想要图形界面打开安装在集群上的Schrodinger, 而XQuartz则速度太慢; 客户端安装Schrodinger的话, 因为程序安装在服务器的局域网内, 而客户端只能连接到gateway门户端, 因此不能连接到装有Schrodinger的机器的端口...所以也不能通过客户端运行程序的方法执行..唯一方法就是连接到集群上进行远程桌面了.

## 服务器端(被远程端)

主要是要开启远程桌面协议[Remote_Desktop_Protocol(RDP)](https://en.wikipedia.org/wiki/Remote_Desktop_Protocol) 或者[VNC协议服务](https://en.wikipedia.org/wiki/Virtual_Network_Computing)实现远程桌面屏幕分享以及远程控制.

### Window客户端

右键我的电脑,属性, 远程设置, 在远程桌面选项, `允许运行任意版本远程桌面的计算机连接 (较不安全)`, 即可.

### Linux客户端

xrdp借用VNC实现远程桌面, 安装可参考[CentOS安装xrdp](http://technote.aven-network.com/550/centos-remote-desktop-via-rdp). 安装后启动服务即可.

## 客户端(远程连接端)

### Window端

直接 开始->所有程序->附件->远程桌面连接 即可.输入ip, 用户名, 密码就可登录.

### Mac端

需要先安装[Microsoft Remote Desktop](https://itunes.apple.com/us/app/microsoft-remote-desktop)程序一类的app才能实现远程桌面. 可以切换全屏, 记住快捷键(我的版本是command+1 自动适应窗口, command+2 全屏)


[MSU-HPCC-Connecting with a Remote Desktop Client](https://wiki.hpcc.msu.edu/display/hpccdocs/Connecting+with+a+Remote+Desktop+Client)

------
