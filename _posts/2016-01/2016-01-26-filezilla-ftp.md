---
layout: post
title: FileZilla搭建ftp服务器
date: 2016-01-26 07:48:05
categories: IT
tags: Internet Software
---

XAMPP原来就配有了FileZilla的Server程序. 如果没有装XAMPP可以自行去[官网下载](https://filezilla-project.org/download.php?type=server)FileZilla的Server端程序.

### 1.安装和打开配置窗口

安装很easy啦...下一步步步就OK了. 安装后有2个执行文件, 按理在安装文件夹下的:`FileZilla Server.exe` 和`FileZilla Server Interface.exe`, 前者才是真正后台服务主程序, 后者不过是个设置的图形界面罢了.

如果是在XAMPP, 先配置(点击`Admin`进入FileZilla Server Interface),然后直接点开启FileZilla服务即可.

注意: 如果另外开了`FileZilla Server`非XAMPP版的话,可能会出现Interface和server交互出问题, 因为版本的问题, 解决办法是去FileZilla Server的安装目录下点击`FileZilla Server.exe`然后关闭服务.最好避免冲突还Unistall掉服务. 如果没有关好,尝试使用管理员权限.

### 2.防火墙设置

随后要解决防火墙问题. 控制面板->防火墙-> "Allow an app through Windows Firewall" -> "Change Settings" -> "Allow another app..." 来配置没有列出来的程序(一般不会列出来). 这里**特别**要注意, 我们放权允许通过防火墙的是`FileZilla Server.exe`, 而 **不是** `FileZilla Server Interface.exe` (因为前者才是真正的FTP服务器, 后者只是个本地看看的界面罢了..).

PS: [官网:配置网络](https://wiki.filezilla-project.org/Network_Configuration)

### 3.允许用户设置

配置好防火墙后, 配置用户. 打开Interface, `Edit`菜单找到 `Users`, 进去后(默认General页面), 右边的方框点 `"Add"` 产生新用户. 中间部分用户名和密码填好. 组可以忽略.如果没有配置FTPS就**不要**点选 "Force SSL for user login". 

### 4.用户允许目录(以及根目录)设置

1. 在刚才Users面板中, 打开最左的Page中的`Shared Folders`, 先选中一个用户, 然后中间的分享文件夹中点击`Add`增加一个共享的目录.
2. 添加文件夹后, 选中它. 中间右边可以选择**操作权限**, 就是对文件和文件夹分别的权限, 读写删除和添加. 自己玩的话全选就是了.. 给人家share就要注意了.
3. 中间还有个`Set As Home dir`, 就是这个用户登录我这个FTP时进去后的第一个显示的`根目录`.根目录只能设置一个. 根目录以下的东东都会被share出去.
4. 可以另外添加一些不在根目录下的文件夹, 例如上一层的另外一个文件夹.添加后, 设置别名`Aliases`, 设置为绝对路径在根目录下的文件夹. 例如根目录是 `C:\Share\`, 想添加的文件夹是`C:\Other`, 可以设置这个Other的别名为`C:\Share\Other\` (绝对路径哦), 这样他就会出现在根目录下啦! 要主要避免循环结构(就是不能设置`C:\`作为Share的子目录,否则结构就会不停死循环下去), 避免别名和真实路径的冲突.

最后就是点击OK啦! 看看Interface有没有报错, 没报错就可以测试客户端了. 可以本地浏览器测试`ftp://你的IP`试试.

### 5.客户端

在客户端, 配置好FTP的IP和用户名密码, 链接即可. 也可以在浏览器上输入`ftp://server_IP`来打开. 注意用户名不同, 可能对应的目录是不同的. 例如UserC对应C盘, UserD对应D盘. 这个取决于服务器端的配置. 自己玩吧..


### 6.配置FTPS (非必须)

FileZilla Server **不支持**SFTP, 支持`FTPS` (FPT over SSL/TLS). 这是另外一种FileZilla搞的服务, 一般使用990端口.   

安装设置就是在Edit 菜单 **Settings** 中开启 **SSL/TLS setting** 的 `Enable FTP over SSL/TLS support(FTPS)`. 首先需要点击`Generate certificate` 然后填一堆东西(瞎填可以)来产生个证书(保存某个地方), 开启上面的FTPS时会自动选择该证书. 之后就开启了FTPS了. 

开启FTPS后, 可以设置强制用户使用这种FTPS协议, 就是在配置用户的General的地方勾选`Generate certificate`.其实也就那样..图形介绍可以参考[这里](http://www.ahlinux.com/server/ftp/8443.html)



------
