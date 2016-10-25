---
layout: post
title: MySQL:选出field中unique不重复数据以及统计其数量
date: 2016-02-15 00:07:29
categories: IT
tags: SQL
---

选择出一列中不重复使用`DISTINCT` 关键词. 例如:

~~~sql
SELECT DISTINCT prefix
FROM table1
~~~

`DISTINCT`关键词用在SELECT后, 可以用于只选择出唯一的项.

另外, 我们也可以通过`GROUP BY`分组修饰词来实现选出不重复的项:

~~~sql
SELECT prefix 
FROM table1
GROUP BY prefix
~~~

如果要统计其中每一个项所拥有的条数, 那么用DISTINCT就不合适了(因为这个只选出一项), 这时可以通过`GROUP BY`和`COUNT`结合实现:

~~~sql
SELECT prefix,COUNT(doi) 
FROM table1
GROUP BY prefix
~~~

------
