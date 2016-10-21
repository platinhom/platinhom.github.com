---
layout: post
title: 检索PDF内容进行文件检索
date: 2015-12-17 11:40:08
categories: IT
tags: Software
---

经常有大量的PDF然后想搜出PDF内容中有指定内容的文件. 有几种办法.

### Adobe内置高级搜索

这个就是使用"高级搜索"功能, 定义好查找的位置进行搜索即可. 很简单. 更多细节参考[帮助](http://help.adobe.com/zh_CN/acrobat/pro/using/WS047F7D61-E05E-4e82-98BA-F84B2E7A5974.w.html). 

能搜出相关文件以及包含搜索词的位置, 点击即可打开文件并跳到相应检索到的位置. 挺方便的. 适合用于快速搜索一些内容, 定位某几个文件.

> 缺点: 不能对搜索出来的文件批量进行操作, 例如移动压缩等.

### PDF建立索引

这里需要使用[Foxit PDF IFilter](https://www.foxitsoftware.com/products/pdf-ifilter/)插件进行, 极快的文件搜索功能, 但是非免费(30天试用,或者自己找找D版吧).. 

支持在Explorer中进行PDF内容搜索. 简单说就是安装这个软件后, 去控制面板(大图标显示方式, 不能是小图标) 找到索引选项(Indexing Option), 进去后高级选项->文件类型, 找到pdf格式, 使用 Foxit PDF IFilter 进行索引, 并勾选 **为属性和文件内容添加索引**(第二项). 之后确定后就会发现缓慢的建立索引了..实在太慢了..

![索引选项](http://www.weste.net/uploadfile/2012/0104/20120104092901663.jpg)![设定pdf文件索引方法](http://www.weste.net/uploadfile/2012/0104/20120104092902311.jpg)

### 借助第三方文件内容搜索软件

一些是通过索引的方法, 一些是直接硬搜文件.

#### FileLocator Pro 

不建立索引马上搜索文档内容. 适用于PDF, 各种文本文档, 甚至音频图片. 安装[Microsoft Office 2010 Filter Pack](http://www.microsoft.com/zh-cn/download/details.aspx?id=17062) (或类似功能)后可以通过索引搜索office文件.更多可以参考[介绍文](http://www.portablesoft.org/filelocator-pro-portable/)及[外链下载](http://180.97.83.161:443/down/0267ccce56d0a863b819257dbe07b7c0-16059835/FileLocatorPro%207.2.2038%20x86%20PortableSoft.7z?cts=dx-f-F742aeD35A8A151A207&ctp=35A8A151A207&ctt=1450351579&limit=3&spd=2200000&ctk=90d359c9c111bbe96ea58b1e5936615f&chk=0267ccce56d0a863b819257dbe07b7c0-16059835). 功能实在十分十分强大, 支持多种格式文件, 甚至压缩包..可以进行VBscript或JSscript辅助. 支持正则表达式, 支持文件属性限定..总之就是很强大..

#### DocFetcher

一个可以指定搜索位置和文件类型进行索引的**开源免费**软件, 有mac/linux/window版本. 因为不用全盘索引, 所以速度要快些. 支持pdf, chm, rtf, office系列等. [介绍文](http://www.iplaysoft.com/docfetcher.html), 下载可到[官网](http://docfetcher.sourceforge.net/en/index.html). 如果只是搜索文件名不搜索内容, [Everything](http://www.voidtools.com/)是最佳选择(超快, 参考[介绍](http://www.iplaysoft.com/everything.html)).

ACS的草稿/接收pdf含有: "ACS Paragon Plus Environment" 关键词~.

------
