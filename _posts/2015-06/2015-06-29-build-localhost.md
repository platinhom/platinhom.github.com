---
layout: post
title: 搭建本地服务器
date: 2015-06-29 07:26:39
categories: IT
tags: Website Internet
---

## 概念

- [OSI模型](https://zh.wikipedia.org/wiki/OSI%E6%A8%A1%E5%9E%8B): 开放式系统互联通信参考模型, 所谓的7层协议.
	1. 物理层: 局部局域网传输, 如电脑-集线器,网卡,主机适配器等.
	2. 数据链路层: 负责网络寻址、错误侦测和改错。将数据加头加尾标识处理, 如以太网,wifi,GPRS等.
	3. 网络层: 决定数据的路径选择和转寄,将网络表头加至数据报，以形成分组。如IP协议.
	4. 传输层: 把传输表头(TH)加至数据以形成数据报。传输表头包含了所使用的协议等发送信息。如TCP.
	5. 会话层: 负责在数据传输中设置和维护电脑网络中两台电脑之间的通信连接。(搭建连接)
	6. 表示层: 把数据转换为能与接收者的系统格式兼容并适合传输的格式。(转为本地可用数据)
	7. 应用层: 提供为应用软件而设的界面，以设置与另一应用软件之间的通信。如HTTP,FTP,SSH.POP3等.
- [TCP](https://zh.wikipedia.org/wiki/%E4%BC%A0%E8%BE%93%E6%8E%A7%E5%88%B6%E5%8D%8F%E8%AE%AE):传输控制协议,传输层,OSI第四层
- [TCP/IP](https://zh.wikipedia.org/wiki/TCP/IP%E5%8D%8F%E8%AE%AE%E6%97%8F): TCP/IP提供点对点的连结机制，将数据应该如何封装、定址、传输、路由以及在目的地如何接收，都加以标准化。它将软件通信过程抽象化为四个抽象层，采取协议堆叠的方式，分别实作出不同通信协议. TCP/IP发源于DoD四层模型,实际是将OSI的5-7层为应用层,1-2层为网络接口层. 其实也是如何封装,传递数据的协议.
- [HTTP](https://zh.wikipedia.org/wiki/%E8%B6%85%E6%96%87%E6%9C%AC%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE):超文本传输协议,是一个客户端终端（用户）和服务器端（网站）请求和应答的标准.服务器响应的[状态码](https://zh.wikipedia.org/wiki/HTTP%E7%8A%B6%E6%80%81%E7%A0%81)反应处理状态,例如常见的404错误.
- [HTTPD](https://en.wikipedia.org/wiki/Httpd) 负责HTTP应答的服务器端的后台驻留程序(Daemon).负责的有很多种,就是所谓的服务器,例如Apache,GWS(google web server),Ngnix,轻量级的lighttpd等.
- [LAMP](https://zh.wikipedia.org/wiki/LAMP) :LAMP是指一组通常一起使用来运行动态网站或者服务器的自由软件名称首字母缩写,包括linux,Apache,MySQL/MariaDB,3P(PHP,Python,Perl),分别是服务器平台,服务器响应程序,数据库,CGI处理语言.有很多变种,就是替换其中一些部分,例如LNMP是Ngnix代替Apache,WIMP是window+IIS代替LA,MAMP就是Mac咯.
- [Apache](https://zh.wikipedia.org/wiki/Apache_HTTP_Server): 开源服务器软件([Apache httpd-github](https://github.com/apache/httpd)),市场占有率最高.跨平台,linux很多都预装有.

## Mac上搭建本地服务器

- [xampp](https://www.apachefriends.org/index.html):([维基](https://en.wikipedia.org/wiki/XAMPP))X代表跨平台,PP代表perl跟php(不包括python). 下载后打开dmg文件双击安装,安装后在/Application/XAMPP文件夹内, 应用里有一个manager-osx.打开manager-osx可以调出很多东西,默认打开的网页可以以后再看.十分简要的介绍看[这个](http://www.arefly.com/xampp-mac/).   
打开manager-osx,选`Manage Servers`标签,选Apache web server, 点击Configure,open conf file,打开注册文件`httpd.conf`(实际为/Applications/XAMPP/etc/httpd.conf),找到`DocumentRoot`和他下面的`<Directory `,更改为你选做主页的目录(两个都要改,最好原位修改,我注释后在下面新加就出问题了╮(╯▽╰)╭ 在上面注释的空位备份一下旧位置),然后保存文件,OK退出小窗,点`restart`(必须),去`Application log`看红字有无报错,无的话就大功告成了.为了保障以前的主页能用,找到`<IfModule alias_module>` 按格式`Alias /xampp /Applications/XAMPP/xamppfiles/htdocs`,并且要更改htdocs文件夹内的index.php,因为其指向/xampp/所以会循环指向,sudo vi 改为`/xampp/xampp/`即可. 然后在指定的目录下写个index.php即可. 支持在local根下用软链接连接到别的目录,支持上述的alias方法指定到别的目录.

- [mamp](https://www.mamp.info/en/downloads/)和OSX server, 参见这篇文章[如何在Mac os X上搭建本地服务器环境](http://segmentfault.com/a/1190000000719292).

- 徒手搭建请参见[Mac OS X 系统配置 Apache+MySql+PHP 详细教程](http://tieba.baidu.com/p/2747109517)..有空再试试..

### 关于httpd.conf

- [Directory](http://httpd.apache.org/docs/2.2/mod/core.html#directory)文件夹权限<Directory dirname>...</Directory> 里面包含子文件夹及自身的权限,即使设了Alias,但可能还不能访问,此时就要在这里新建一个tag,模仿DocumentRoot文件夹的写法.

---
