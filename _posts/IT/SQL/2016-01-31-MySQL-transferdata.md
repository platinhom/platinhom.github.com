---
layout: post
title: MySQL转移数据(同一数据库表到表)
date: 2016-01-31 08:49:18
categories: IT
tags: SQL
---

其实就是Insert和Select的复合应用了. Select的结果作为Insert的数据源. 注意表中的field要对号(尤其**顺序**)

这里table1是源表, table2是接收的表

### 1.将所有数据导入

首先两个表必须格式一致(数据field一致, 主要是列数和顺序要一致,最好数据格式数据名也一致)

~~~sql
INSERT INTO table2 SELECT * FROM table1;
# if you make sure the process is ok
TRUNCATE table1;
~~~

- 如果同时想新建一个新表, 可以:

~~~sql
CREATE TABLE table3 
SELECT * FROM table1 ;
~~~

- 如果想先复制一份该表的结构(不包含内容)

~~~sql
CREATE TABLE table3
SELECT * FROM table1 
WHERE 1=2 ;
~~~

这是通用型的复制表结构的方法, `1=2`是永远不成立的, 所以没有数据被复制.

在MySQL5 以后, 可以用`LIKE`来只复制结构

~~~sql
CREATE TABLE table3
LIKE table1 ;
~~~

- 复制数据后想删掉一些指定数据可以用`DELETE`完成

~~~sql
DELETE FROM table2
WHERE field=value ;
~~~

### 2.选择某些数据进行复制转移

这里'某些' 有两个概念: 所有数据某些列; 某些行的数据; 甚至两者结合:

- 某些行所有field, 其实就是`WHERE`一下就好了:  

~~~sql
INSERT INTO table2 
SELECT * FROM table1 
WHERE primary=value;
~~~
2. 所有行某些列, 注意这些列的顺序一定要对好: 

~~~sql
INSERT INTO table2 (field1,filed2) 
SELECT field1,field2 FROM table1;
~~~

第三种情况就是前两者的结合了. 

~~~sql
INSERT INTO table2 (field1,filed2) 
SELECT field1,field2 FROM table1 
WHERE primary=value;
~~~

### 3.只转移table2不存在的数据

可以参考之前的[MySQL唯一键重复的处理](/2016/01/30/MySQL-repeatRows)类似的处理. 要么是`IGNORE`掉重复的 (如果是主键或者唯一键), 要么是用SELECT进行控制:

~~~sql
INSERT INTO table2 (field1,filed2)
SELECT field1,filed2 FROM table1
WHERE NOT EXISTS 
(SELECT * FROM table2 
WHERE table2.id=table1.id);
~~~

如果重复的是主键等唯一键:

~~~sql
INSERT IGNORE INTO table2 
SELECT * FROM table1;
~~~

------
