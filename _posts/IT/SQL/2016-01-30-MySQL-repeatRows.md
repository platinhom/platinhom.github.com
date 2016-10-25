---
layout: post
title: MySQL唯一键重复的处理
date: 2016-01-30 08:25:13
categories: IT
tags: SQL
---

顾明思议, 唯一键就是一列数据中不可以产生重复的数据. 索引中设置**UNIQUE**或者 **PRIMARY**(带有INDEX, UNIQUE且只能有一个的特性) 后该列数据就是唯一的. 一个表可以设置多列有唯一键, 但不建议. 如果有此情况, 有些处理就要特别考虑了.

但插入数据INSERT时, 可能会存在多rows的唯一键的重复情况, **默认**情况时就会**报错**. 处理嘛, 无非就是忽略掉不替换, 以及替换原有数据进行更新. 后者有好几种做法.

## 忽略掉重复的数据

很简单, 在INSERT 后面加入**IGNORE** 关键词忽略报错. 

`INSERT IGNORE INTO table (a,b,c) VALUES (1,2,3)`

IGNORE是忽略掉INSERT时产生的错误, 不仅仅是重复的问题, 例如分隔表数据不够, 类型不匹配这些错也会忽略掉. 所以使用时还是要小心.  

更多信息关于[IGNORE参考](http://dev.mysql.com/doc/refman/5.7/en/sql-mode.html#ignore-strict-comparison).

## 使用INSERT IF 逻辑语句来控制

这种做法比较直观, 但比较笨, 还要用`COUNT`来先统计. 

~~~sql
SELECT COUNT(*) FROM xxx WHERE ID=xxx;  
  
if (x == 0)  
    INSERT INTO xxx ... VALUES ...;  
else  
    UPDATE xxx SET ...; 
~~~

## INSERT ... SELECT .. WHERE EXIST (SELECT .. WHERE ...) .... 利用INSERT..SELECT...的复合语句

这个语法句也比较直观, 适合于从一个表复制数据到另一个表时处理. 有两个`SELECT WHERE`结构, 第一个从源数据表中取数据用于替换新表, 第二个从被替换表中选取已存在的数据用于 `EXISTS/NOT EXISTS`处理.  

看起来很复杂, 其实不难, 看例子:

~~~sql
INSERT INTO clients   
(client_id, client_name, client_type)   
SELECT supplier_id, supplier_name, 'advertising'   
FROM suppliers   
WHERE not exists (select * from clients   
where clients.client_id = suppliers.supplier_id);  
~~~

这里唯一键是`client_id`(和 supplier_id 是一个东东). 第二个SELECT子句选出所有clients表中唯一键重复的数据, 将数据递给`not exists`, 表示唯一键非重复的数据. 这时第一个SELECT子句就会从suppliers 表中取出唯一键非重复的数据.


## INSERT ... ON DUPLICATE KEY UPDATE ... 重复时就修改更新

这句[ON DUPLICATE KEY UPDATE](http://dev.mysql.com/doc/refman/5.7/en/insert-on-duplicate.html)是十分常用的. 当表中有唯一性(**UNIQUE**)的列时, 会出现数据冲突, 尤其是有主键 **PRIMARY**时(如果主键是自增的可以避免). 和`REPLACE`语句类似, 写起来复杂点. 返回值是受影响的行数(包括插入这行), 例如插入一行且有一个重复, 返回2, 没有重复就返回1.

> 注意: 避免有多个唯一列进行`ON DUPLICATE KEY UPDATE`!     

在UPDATE部分, 数据值的调用除了一些常量变量, 还有例如: 

- 调用旧数据的值: 直接用列名: `c=c+1`, 例如原有(1,2,3), 在unique后就会(1,2,4)
- 调用新数据的值: 用VALUES(列名): `c=VALUES(c)`. 这样会取决于INSERT时的给定value值, 例如INSERT(4,5,6)那么就会把原来的 (1,2,3) 替换为 (1,2,6)

~~~sql
INSERT INTO table (a,b,c) VALUES (1,2,3)
  ON DUPLICATE KEY UPDATE b=b+1,c=VALUES(c);

UPDATE table SET b=b+1,c=3 WHERE a=1;
~~~

## [REPLACE](http://dev.mysql.com/doc/refman/5.7/en/replace.html) 语句

REPLACE语句实际是先DELETE再INSERT, 其实和`INSERT ON DUPLICATE KEY UPDATE` 没啥区别. 看起来还更简易, 就是相当于多记住一个主要行为关键词REPLACE罢了. 返回值也是受影响的行数 (没有重复返回1, 有重复>=2, 一般单唯一键时是2) . 

REPLACE语法可以和INSERT一样, `REPLACE INTO 表名 (fields,..) VALUES(value,..)` , 也可以使用UPDATE的`SET` 来实现(实际就是UPDATE SET嘛) `REPLACE INTO 表名 SET field1=value1, field2=value2...;`. 例如以下三句是等价的: 

~~~sql
REPLACE INTO users (id,name,age) VALUES(22, '老赵', 30);
REPLACE INTO users SET id = 22, name = '老赵', age = 30;

INSERT INTO users (id,name,age) VALUES(22, '老赵', 30) 
ON DUPLICATE KEY UPDATE SET name = VALUES(name),age = VALUES(age)
~~~

有多个唯一键的列时, 受影响的就会增多, 例如三个数据分别(1,1,1) ; (2,2,2); (3,3,3) 输入数据时(1,2,3), 三个都是唯一键, 此时会返回4, 原来三个数据变成一个: (1,2,3)

------
