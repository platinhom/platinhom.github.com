---
layout: post
title: Python:difflib字符串差别
date: 2016-01-05 19:26:25
categories: Coding
tags: Python
---

difflib是可以比较文件和字符串差异的库, 能实现类似linux命令diff的效果. 如果比较文件夹和文件, 可以使用[filecmp](http://platinhom.github.io/ManualHom/Coding/Python/python-2.7.11rc1-docs-html/library/filecmp.html#module-filecmp)模块.

## 快速上手

#### 计算两个字符串相似度

~~~python
difflib.SequenceMatcher(None, 'abcde', 'zbcde').ratio()
~~~



<iframe src="http://platinhom.github.io/ManualHom/Coding/Python/python-2.7.11rc1-docs-html/library/difflib.html" width="100%" height="600px"></iframe>


## Reference

1. [Python-difflib](http://platinhom.github.io/ManualHom/Coding/Python/python-2.7.11rc1-docs-html/library/difflib.html)
2. [用PYTHON计算文本的相似度](http://crazyof.me/blog/archives/1555.html)
3. [python-Levenshtein几个计算字串相似度的函数解析](http://www.cnblogs.com/kaituorensheng/archive/2013/05/18/3085653.html)

------
