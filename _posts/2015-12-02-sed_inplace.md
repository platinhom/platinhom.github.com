---
layout: post
title: sed原位修改-i选项
date: 2015-12-02 01:42:50
categories: Coding
tags: Bash Git
---

sed 可以进行源文件替换, 此时使用-i 选项

~~~bash
sed -i "s/text/replacment/g" testfile.txt
~~~

该命令在Linux正常运行. 然而该命令在Mac上就行不通了...

> command i expects \ followed by text sed

这个i可以是c可以是别的.

原因是, Mac是使用的BSD不同, 需要 [ -i extension ], 需要进行强制备份. 需要一个字符串后接用来进行文件备份(追加文件名后). 例如

~~~bash
sed -i ".bak" "s/text/replacment/g" testfile.txt
# backup file: testfile.txt.bak
sed -i "" "s/text/replacment/g" testfile.txt
# in place
~~~

将生成testfile.txt.bak 文件保存原有文件. 若实在不需要备份, 可使用 `-i ""`

但随后我用相关命令处理`*`所以文件时出现错误:

> RE error: illegal byte sequence

原因可能因为是对二进制文件处理的编码问题. 可以参见[Stackoverflow](http://stackoverflow.com/questions/19242275/re-error-illegal-byte-sequence-on-mac-os-x)的回答.

解决:

~~~bash
LC_ALL=C sed -i '' 's/_static\//static\//g' *
~~~

------
