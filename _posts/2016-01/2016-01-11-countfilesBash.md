---
layout: post
title: Linux下统计文件或文件夹数量
date: 2016-01-11 05:38:04
categories: IT
tags: Bash
---

一般性统计, 最简单就是

`ls | wc -l`

在这个基础上, 可以衍生出:

1. 统计文件或文件夹
	- 文件: `ls -l | grep "^-" | wc -l`
	- 文件夹: `ls -l | grep "^d" | wc -l`
2. 递归统计文件或文件夹:
	- 文件: `ls -lR | grep "^-" | wc -l`
	- 文件夹: `ls -lR | grep "^d" | wc -l`

另外一种是利用find

`find ./ -type f | wc -l` 

------

- `ls -l` 可以列出详细信息, 列出后第一大列是文件权限和文件/文件夹. 第一列文件是`-`, 文件夹是`d`
- `grep "^-"` 用正则匹配开头
- `wc -l` 统计行数

------
