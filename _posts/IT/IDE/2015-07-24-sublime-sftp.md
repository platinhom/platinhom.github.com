---
layout: post
title: Sublime SFTP远程编辑文件
date: 2015-07-23 19:25:31
categories: IT
tags: IDE Internet
---

- **FTP** 是文件传输协议。在网络上,如果你想把文件和其他人共享。最方便的办法莫过于将文件放FTP服务器上，然后其他人通过FTP客户端程序来下载所需要的文件。FTP进行文件传输需要通过端口进行。FTP为了适应不同的网络环境，支持主动连接和被动连接两种模式。这两种模式都主要针对数据链路进行的，跟控制链路无关。一般所需端口为：
	1. 控制链路—TCP端口21。控制器端。用于发送指令给服务器以及等待服务器响应。
	2. 数据链路---TCP端口20。数据传输端口。用来建立数据传输通道的。主要用来从客户向服务器发送一个文件、从服务器向客户发送一个文件、从服务器向客户发送文件或目录列表。
- **SFTP** 是Secure File Transfer Protocol的缩写，安全文件传送协议。可以为传输文件提供一种安全的加密方法。sftp 与 ftp 有着几乎一样的语法和功能。sFTP 为 SSH的一部份，是一种传输档案至 Blogger 伺服器的安全方式。但是，由于这种传输方式使用了加密/解密技术，所以传输效率比普通的FTP要低得多，如果对网络安全性要求更高时，可以使用SFTP代替FTP。

## 安装
- Package Control(*shift+cmd+p*,然后输入 *PCI* 安装)搜索SFTP,搜索后安装.
- 安装后,在**File->SFTP/FTP** 中可以编辑和打开服务器.
- 新建一个文件(可能有bug会在当前文件插入内容), 在*File->SFTP/FTP->Setup server* 中配置sftp,例如使用sftp服务,host,user name, password(免密码登陆,需要取消注释//),port(sftp:22,ftp:21). remote_path是远程登陆的目录,配置位置不对的话会登陆失败.
- 将配置文件保存到 *Packages/User/sftp_servers* 内(*Preference-Browse Packages*).名字根据自己需要,默认后缀json.
- 菜单*File->SFTP/FTP->Browse server* (快捷键cmd+ctrl+R,B)可以列出现在的服务器列表(注意上一步配置文件保存位置对不对).出现了文件列表(转图)  
![](http://wpjam.qiniudn.com/qiniu/3736/image/310422cb212eca74ed9a844573801461.png?watermark/1/image/aHR0cDovL3dwamFtLnFpbml1ZG4uY29tL3dwamFtL3dhdGVybWFyay5wbmc=/dissolve/100/gravity/SouthEast/dx/10/dy/10|imageView2/2/w/442/h/420)
- 点击文件,出现菜单,点edit就可以编辑了!   
![](http://wpjam.qiniudn.com/qiniu/3736/image/a2059b28f29ad7b8298f5ad3eeb0f3f2.png?watermark/1/image/aHR0cDovL3dwamFtLnFpbml1ZG4uY29tL3dwamFtL3dhdGVybWFyay5wbmc=/dissolve/100/gravity/SouthEast/dx/10/dy/10|imageView2/2/w/465/h/218)

## 使用
[官方使用介绍](http://wbond.net/sublime_packages/sftp/usage).


## Reference
1. [官网](http://wbond.net/sublime_packages/sftp)
2. [SFTP/FTP图文介绍](http://nonfu.me/p/1257.html)

------
