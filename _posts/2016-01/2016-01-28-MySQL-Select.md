---
layout: post
title: MySQL:Select读取数据
date: 2016-01-28 06:51:18
categories: IT
tags: SQL
---

Select 是从数据库中获取数据, 返回值是获取得到的数据**条数**. 他是个动作. 而 `WHERE` 是筛选条件, where才是国语说话时的"选择"的过程. `SELECT ...WHERE...` 实际等于`获取 列名... 当条件...`. 从数据库取数据最基本的关键词, 也是一般数据库操作权限最低时(只读)也需要赋予的权限. 

`SELECT` 后跟的是 Field名, 所有列使用`*`. WHERE 后面是选取哪几行数据的限定条件. 不加WHERE就是所有数据. SELECT..WHERE是最基础的获取条件, 除此以外SELECT还有多个可用选项子句 (详细介绍参考手册[SELECT说明](http://dev.mysql.com/doc/refman/5.7/en/select.html)):

~~~sql
SELECT
    [ALL | DISTINCT | DISTINCTROW ]
      [HIGH_PRIORITY]
      [MAX_STATEMENT_TIME = N]
      [STRAIGHT_JOIN]
      [SQL_SMALL_RESULT] [SQL_BIG_RESULT] [SQL_BUFFER_RESULT]
      [SQL_CACHE | SQL_NO_CACHE] [SQL_CALC_FOUND_ROWS]
    select_expr [, select_expr ...]
    [FROM table_references
      [PARTITION partition_list]
    [WHERE where_condition]
    [GROUP BY {col_name | expr | position}
      [ASC | DESC], ... [WITH ROLLUP]]
    [HAVING where_condition]
    [ORDER BY {col_name | expr | position}
      [ASC | DESC], ...]
    [LIMIT {[offset,] row_count | row_count OFFSET offset}]
    [PROCEDURE procedure_name(argument_list)]
    [INTO OUTFILE 'file_name'
        [CHARACTER SET charset_name]
        export_options
      | INTO DUMPFILE 'file_name'
      | INTO var_name [, var_name]]
    [FOR UPDATE | LOCK IN SHARE MODE]]
~~~

## WHERE 选择条件

## LIMIT [OFFSET] 输出数量和采样位置

## ORDER 排序

## 关于NULL

要用 `IS NULL` 或者 `IS NOT NULL` 来判断而不是`=`

1. [MySQL学习4-操作命令](/2015/07/05/MySQL-operation/)
2. [MySQL学习3-数据和数据操作](/2015/07/05/MySQL-datatype-syntax/)

TODO: 随机选择数据

------
