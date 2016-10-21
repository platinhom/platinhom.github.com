---
layout: post
title: Python:获取文献PDF文献doi
date: 2015-12-20 16:51:07
categories: Coding
tags: Python
keywords: "doi, pdf, python, pdfminer, regex" 
---

# Get DOI number from PDF file based on python 

-----

只能针对第一页具有doi号并且pdf不是扫描版..

需要安装python模块: [pdfminer](https://euske.github.io/pdfminer/)  
测试在python 2.7.10 上实现.

### 原理

- pdfminer读取pdf首页 (以后可以加入选项读取指定页码). [参考](/2015/12/18/pdfminer/)
- 正则表达式从输出内容中抓取doi号 (只支持`10.*/*`形式, 要是`10.*.*`暂不支持). [参考](http://stackoverflow.com/questions/27910/finding-a-doi-in-a-document-or-page)

这里的有点问题..

`'\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'<>])\S)+)\b'`

- 这条式子对于ACS有些doi以`+`结尾会误判, 忽略掉+号.  
改进: `'\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?!["&\'<>])\S)+)(?:\+?|\b)'`
- 在抓首页doi时有时会遇上恶心的`|`会出问题.  
改进: `'\b(10[.][0-9]{4,}(?:[.][0-9]+)*/(?:(?![\|"&\'<>])\S)+)(?:\+?|\b)'`


> 仍有的问题

- 对于校正类paper, 或者个别paper引用别的doi, 此时抓出来的是引用的doi, 而并非本paper的doi (或者可以根据抓取得到的doi数量来判断??)
- 对于SI..有时SI也会抓出SI..这就不对了..
- 对于老文献: 老文献没有doi..
- 对于扫描版: 扫描版抓不出数据 

### 使用

~~~bash
# 获取一个/多个pdf文件doi
# 输出屏幕: 文件名 Found: doi号
python getfiledoi.py a.pdf b.pdf c.pdf Done/*.pdf

# 根据doi号重命名文件, -r 选项
# 文件名为: 出版商号@文献号 , 如10.1021@jp123456f
python getfiledoi -r a.pdf

# 只输出doi号, 没有就空输出
python getfiledoi -d a.pdf
~~~

<script src="https://gist.github.com/platinhom/07475ec4efc514dd90d8.js?file=getfiledoi.py"></script>

------
