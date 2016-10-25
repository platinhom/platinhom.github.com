---
layout: post
title: Greedy String Tiling(GST)算法
date: 2016-02-16 12:07:56
categories: Coding
tags: Python Algorithm
---

在回答这个问题[Greedy String Tiling in Python](http://stackoverflow.com/questions/35419576/greedy-string-tiling-in-python/35421930#35421930) 时接触了GST算法. 这个算法是一种贪婪串匹配算法，对两个字符串进行贪婪式搜索以找出所有最大公有子串，它需要对要计算的两个字符串进行多次搜索，每次找出当前字符串中未“标注”部分的最长公共子串，并把找出的最长公共子串“标注”为已使用，避免最大匹配重复使用 (源自[字符串相似度计算](http://www.jmatrix.org/algorithm/166.html))。 根据这个定义, 我就改写了原帖的算法, 发来学习记录一下.

LCS算法[Longest Common Subsequences](https://zh.wikipedia.org/wiki/%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%AD%90%E5%BA%8F%E5%88%97) 是用于找出最长匹配子串的.  这里其实并没有真正实现维基所述的LCS, 那个要造2维数组来扫, 在Python我就简单化处理了.

这里实现LCS精妙的是利用`max(lcs(b+),lcs(a+),key=len)`来迭代. 将位置定出来后再将序列相加, 获得最长的序列解. 后面`while`循环实际就是解决GST算法定出所有不少于最少长度的子串位置了. 其实在`maxsub`中两个字符串的长度应该也是对计算时间有影响的, 可以进一步优化. 

TODO: 这个[Rabin–Karp algorithm](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm)算法看起来也很有趣, 下次实现一下.

~~~python
#! /usr/bin/env python

a=['a','b','c','d','e','f']
b=['d','e','a','b','c','f']

c = ['1','2','3','4','5','6','7','8','9','1','3']
d = ['3','4','5','2','1','7','8','9','1']

def gst(a,b,minlength=2):
	if len(a) == 0 or len(b) == 0:
		return []
	# if py>3.0, nonlocal is better
	class markit:
		a=[0]
		minlen=2
	markit.a=[0]*len(a)
	markit.minlen=minlength

	#output index
	out=[]

	# To find the max length substr (index)
	# apos is the position of a[0] in origin string
	def maxsub(a,b,apos=0,lennow=0):
		if (len(a) == 0 or len(b) == 0):
			return []
		if (a[0]==b[0] and markit.a[apos]!=1 ):
			return [apos]+maxsub(a[1:],b[1:],apos+1,lennow=lennow+1)
		elif (a[0]!=b[0] and lennow>0):
			return []
		return max(maxsub(a, b[1:],apos), maxsub(a[1:], b,apos+1), key=len)

	# Loop to find all longest substr until the length < minlength
	while True:
		findmax=maxsub(a,b,0,0)
		if (len(findmax)<markit.minlen):
			break
		else:
			for i in findmax:
				markit.a[i]=1
			out+=findmax
	return [ a[i] for i in out]

print gst(a,b,2)
~~~

------
