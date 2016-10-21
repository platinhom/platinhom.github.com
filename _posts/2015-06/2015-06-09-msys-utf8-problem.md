---
layout: post
title: MSYS输出中文到文件后无法提交到Github:UTF-8 error
date: 2015-06-09 09:29:52
categories: IT
tags: Shell Bash Git
---

# UTF-8 encoding error when using MSYS for Github

今天写个脚本处理自动根据文件夹内PDF文件来编写页面的脚本.出现了以下问题:

> Page Build failure. The page build failed with the following error: The file `index.md` is not properly UTF-8 encoded. For more information, see ...

在开始, 以为是网页没有使用UTF8编码原因, 因为附带的链接告诉你添加在`_config.yml`中添加`encoding: UTF-8`. 我按照他做了. But it fails. 追踪下来, 虽然我的config里没有加入该项,但我在网页模板中加入了`<meta http-equiv="content-type" content="text/html; charset=utf-8" />` 所以理论上是等价的.

问题来了.折腾半天,仍然不行.我文件中有两处中文:一处是自己编写的Title项, 另一处是使用循环echo文件名到index.md中.

网上有说使用`iconv`命令转化文件, 但老出错.研究半天发现:

- 我手动输入的文字是UTF-8格式的.
- msys(原生态, 非msysgit)只支持GBK格式,虽然我们用`alias ls='ls --show-control-chars -F --color=tty'`可以更改shell显示中文,但输出编码仍然是GBK!
- 一个文件中存在两种编码,于是变成非标准格式,iconv转换失败.
- Github不支持GBK

所以问题解决了:1.脚本自动化后统一处理中文. 2.iconv将文件从GBK变为UTF-8.

使用命令 `iconv -f GBK -t UTF-8 index.md > index-2.md` 即可.

- `-f` 指明输入编码
- `-t` 指明输出编码
- `-l` 列出支持的编码
- `-o` 指明输出文件,但是msys的不能用该选项,请注意用管道代替.

判断文件类型可以使用`file filename` 来判断.msys显示echo出来中文输出格式为`ISO-8859 text`

好了,以下是脚本,仅供参考.

~~~~ bash
#! /bin/bash
# Author: Platinhom
# Last updated:2015.6.9

# To list all the pdf file into the index.md file.
# Notice the encoding problem. http://platinhom.github.io/2015/06/09/msys-utf8-problem/

echo "---">index.md
echo "title: PDF">>index.md
echo "layout: page">>index.md
echo "comments: yes">>index.md
echo "---">>index.md
echo "">>index.md

echo "- Manual:    ">>index.md
for files in manual/*.pdf
do
filename=${files##*/}
echo "[${filename%.*}](/pdf/${files})" >> index.md
done

echo "- Book:    ">>index.md
for files in book/*.pdf
do
filename=${files##*/}
echo "[${filename%.*}](/pdf/${files})" >> index.md
done

echo "- Paper:    ">>index.md
for files in reference/*.pdf
do
filename=${files##*/}
echo "[${filename%.*}](/pdf/${files})" >> index.md
done

echo "">>index.md

## replace the gbk encoding file.
if [ ! -z "`file index.md|grep ISO-8859`" ];then
iconv -f GBK -t UTF-8 index.md > index-2.md
rm index.md
mv index-2.md index.md
fi

~~~~

---
