---
layout: post
title: Sublime删除空行
date: 2015-08-20 20:46:35
categories: IT
tags: IDE
---

## 正则表达式替换法

[正则表达式](http://platinhom.github.io/2015/06/10/regexp-re/)

### 删除空行

`ctrl+H` 进入替换模式, 然后`alt+R`或者点击左边第一行一个的正则表达式, 变得更灰表示使用正则模式.  

第一行查找部分输入`^\n` 替换部分为空,再replace all. 这样就可以把所有空行都删掉. 最简单的方法..

### 删除多余空格

同上, 进入正则表达式替换. 输入查找 `(?ms)\ {2,}`, 替换成空格. 前者表示2个或以上空格的选取. 同理可以进行很多方便的处理.


## DeleteBlankLines 插件

搜索这玩意就可以了, 介绍可以去[Package Control](https://packagecontrol.io/packages/DeleteBlankLines)看.用法就是选择部分后ctrl+alt+backspace键(Mac是delete键).


------
