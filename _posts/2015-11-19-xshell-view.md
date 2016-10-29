---
layout: post
title: Mac上X11图形界面化远程程序
date: 2015-11-18 21:57:41
categories: IT
tags: Software
---

1. 启动XQuartz (可以命令行,也可以从app里启动X11)
2. 打开偏好设置，勾选输入下的“模拟三按键鼠标”
3. 输出可以选择“全屏模式”，按Command-Option-A切换.
4. 如果修改了配置需要退出重新启动生效
5. 选择“应用程序－终端”
6. 终端窗口打开后输入：`xhost +` 然后回车. access control disabled, clients can connect from any host. 出现这句话就OK了.
7. 登陆远程主机： `ssh -X username@host` 输入密码登陆即可. -X不行就-Y.
8. 登陆后输入setenv回车，查看DISPLAY变量，对DISPLAY变量设置：`setenv DISPLAY localhost:10.0`
9. 可输入xclock，如果弹出窗口，说明可以使用远程主机的图形界面了。
10. 退出时，先关闭图形窗口，然后命令行上输入exit退出

注意DISPLAY变量可以通过控制`localhost`的ip来将X图形界面显示到相应终端, 例如可以图形化到另一台机子上.


------
