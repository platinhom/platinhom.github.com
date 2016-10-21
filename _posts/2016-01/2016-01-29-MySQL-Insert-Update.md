---
layout: post
title: MySQL:Insert/Update/Delete数据
date: 2016-01-29 06:17:26
categories: IT
tags: SQL
---

数据库数据操作最基本莫过于Select和Insert/Update/Delete这几个了. 第一个是怎么选取数据, 可以单独讨论了. 后三个是添加修改和删除数据. 这里将近几日用到的小结一下吧.

## 添加数据: [Insert](http://dev.mysql.com/doc/refman/5.7/en/insert.html)

### 添加一条数据 Insert Into .. Values (a,b,c)...

- 将所有列的数据列出来插入, 适用于初始化时且项不多, 表结构较简单  
`INSERT INTO 表名 VALUES (值1, 值2,....);`

- 指定某些列名, 并按顺序对这些列赋值. 最常用. 注意, 没有赋值的项, 需要有**自增** 或者 **预设值**(default或者null)属性.  
`INSERT INTO 表名 (列名1, 列名2, 列名3, ...) VALUES (值1, 值2, 值3, ...);`

> 别忘了`INTO 表名`和`VALUES`非value.

### 添加多条数据 Insert Into .. Values (),()..

多条数据主要使用`(,..),(,..)`去提交, 和单条数据类似:

`INSERT INTO 表名 (列名1, 列名2, 列名3, ...) VALUES (值11, 值12, 值13, ...),(值21, 值22, 值23, ...),(值31, 值32, 值33, ...);`

括号内多个值(`,`分隔)对应前面的列, 而`()`作为整体则是对应一条数据, 多条就是用`,`分隔.

例如: 

`INSERT INTO table1(i) VALUES(1),(2),(3),(4),(5);` 是插入5条数据, 每条1列.

### 添加数据要是存在就修改: Insert ... ON DUPLICATE KEY UPDATE ...

这句[ON DUPLICATE KEY UPDATE](http://dev.mysql.com/doc/refman/5.7/en/insert-on-duplicate.html)是十分常用的. 当表中有唯一性(**UNIQUE**)的列时, 会出现数据冲突, 尤其是有主键 **PRIMARY**时(如果主键是自增的可以避免). 

> 注意: 避免有多个唯一列进行`ON DUPLICATE KEY UPDATE`!   

- 调用旧数据的值: 直接用列名: `c=c+1`
- 调用新数据的值: 用VALUES(列名): `c=VALUES(c)`

~~~sql
INSERT INTO table (a,b,c) VALUES (1,2,3)
  ON DUPLICATE KEY UPDATE b=b+1,c=VALUES(c);

UPDATE table SET b=b+1,c=3 WHERE a=1;
~~~

### 添加数据要是存在就忽略,不替换 Insert IGNORE ....

如果没有`IGNORE`, 插入时如果有唯一键重复会报错, IGNORE可以忽略报错.

`INSERT IGNORE INTO table (a,b,c) VALUES (1,2,3)`

另外对重复键的处理还可以利用`Insert..Select..`, `Replace`进行.

## 修改数据: [UPDATE](http://dev.mysql.com/doc/refman/5.7/en/update.html)

### 修改单条数据单列/多列

`UPDATE table SET field = 'value' WHERE other_field = 'other_value';`

一条一条数据根据 `WHERE` 条件进行选择然后修改field为值value

### 修改多条数据, 同一修改

`UPDATE table SET field = 'value' WHERE other_field = ('value1','value2'..);`

多条数据的选择条件使用`WHERE IN`, 再统一使用`SET field = value` 来实现多条设置同一个value.

### 修改多条数据, 但修改值不同

使用 `CASE var WHEN condition THEN value ... END WHERE var IN (condition1,condition2...)`格式, 简单说就是用`CASE..WHERE IN`语句来构造多选条件. 例如: 

~~~sql
UPDATE mytable
    SET myfield = CASE id
        WHEN 1 THEN 'value1'
        WHEN 2 THEN 'value2'
        WHEN 3 THEN 'value3'
    END
WHERE id IN (1,2,3)
~~~

###### 一个PHP实例 [来源](http://www.ghugo.com/update-multiple-rows-with-different-values-and-a-single-sql-query/):

~~~php
$display_order = array(
    1 => 4,
    2 => 1,
    3 => 2,
    4 => 3,
    5 => 9,
    6 => 5,
    7 => 8,
    8 => 9
);
 
$ids = implode(',', array_keys($display_order));
$sql = "UPDATE categories SET display_order = CASE id ";
foreach ($display_order as $id => $ordinal) {
    $sql .= sprintf("WHEN %d THEN %d ", $id, $ordinal);
}
$sql .= "END WHERE id IN ($ids)";
echo $sql;
~~~

## 删除数据: [DELETE](http://dev.mysql.com/doc/refman/5.7/en/delete.html)

删除数据很简单, 结合where来选择就好了, 删除多条用`WHERE IN` 好了

`DELETE FROM 表名 WHERE field = value` 删除满足条件的单行  
`DELETE FROM 表名 WHERE field IN (value1,value2...)` 删除满足条件的多行  
`DELETE FROM 表名` 删除所有行数据

## Reference

1. [MySQL学习4-操作命令](/2015/07/05/MySQL-operation/)
2. [MySQL学习3-数据和数据操作](/2015/07/05/MySQL-datatype-syntax/)
3. [MySQL:Select读取数据](/2016/01/28/MySQL-Select/)

------
