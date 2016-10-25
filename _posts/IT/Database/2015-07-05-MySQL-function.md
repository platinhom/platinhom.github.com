---
layout: post
title: MySQL学习5-函数部分
date: 2015-07-05 11:48:41
categories: IT
tags: Database SQL
---

SQL 拥有很多可用于计数和计算的内建函数。  
内建 SQL 函数的语法是：`SELECT function(列) FROM 表`  
在 SQL 中，基本的函数类型和种类有若干种。函数的基本类型是：   

- Aggregate 函数  
合计函数（Aggregate functions）:操作面向一系列的值，并返回一个单一的值。 要是对分组的进行操作,则返回各个组的对应值.  
注释：如果在 SELECT 语句的项目列表中的众多其它表达式中使用 SELECT 语句，则这个 SELECT 必须使用 GROUP BY 语句！
- Scalar 函数  
Scalar 函数的操作面向某个单一的值，并返回基于输入值的一个单一的值。可以把无输入的也归这类.

## Aggregate 函数

- `AVG(字段名)` 得出一个表格栏平均值(数值型,日期)   
- `COUNT(*|字段名)` 对数据行数的统计(*)或对某一栏有值(非null)的数据行数统计(尤其搭where)   
- `MAX(字段名)` 取得一个表格栏最大的值(数值型,日期)   
- `MIN(字段名)` 取得一个表格栏最小的值(数值型,日期)   
- `SUM(字段名)` 把数据栏的值相加(数值型,日期)   
- `First(字段名)` 返回字段第一个值,常结合order用(其实就是不常用,用max/min够了)
- `LAST(字段名)` 返回字段最后一个值,常结合order用

## Scalar 函数  

- `NOW()`	返回当前的日期和时间
- `CURDATE()`	返回当前的日期
- `CURTIME()`	返回当前的时间
- `DATE()`	提取日期或日期/时间表达式的日期部分
- `EXTRACT()`	返回日期/时间按的单独部分
- `DATE_ADD()`	给日期添加指定的时间间隔
- `DATE_SUB()`	从日期减去指定的时间间隔
- `DATEDIFF()`	返回两个日期之间的天数
- `DATE_FORMAT()`	用不同的格式显示日期/时间

- `IFNULL(列名,0)` 或 `COALESCE(列名,0)`: 要是该列是null则按0处理.尤其将两列求和时重要.
- `LEN(col)` 字符串长度.
- `UCASE(col)`和`LCASE(col)` 字符串大写化和小写化.
- `MID(column_name,start[,length])` 其实是字符子串,从start(1开始)长度length的子串.
- `concat(colA,':',colB,'=')` 将两列的字符串拼接起来.
- `FORMAT(col,format)` 将列按指定格式进行格式化

## Having子句:
和where类似,用在order后,可以对结果进行函数处理后再进行表达式运算.

~~~sql
SELECT column_name[, aggregate_function(column_name)]
FROM table_name
[WHERE column_name operator value]
GROUP BY column_name
HAVING aggregate_function(column_name) operator value;

SELECT Customer,SUM(OrderPrice) FROM Orders
WHERE Customer='Bush' OR Customer='Adams'
GROUP BY Customer
HAVING SUM(OrderPrice)>1500;
~~~

## 自建函数例子

~~~sql
delimiter $$
CREATE FUNCTION myFunction
   (in_string      VARCHAR(255),
    in_find_str    VARCHAR(20),
    in_repl_str    VARCHAR(20))
  RETURNS VARCHAR(255)
BEGIN
  DECLARE l_new_string VARCHAR(255);
  DECLARE l_find_pos   INT;
  SET l_find_pos=INSTR(in_string,in_find_str);
  IF (l_find_pos>0) THEN
    SET l_new_string=INSERT(in_string,l_find_pos,LENGTH(in_find_str),in_repl_str);
  ELSE
    SET l_new_string=in_string;
  END IF;
  RETURN(l_new_string);
END$$
~~~

## Reference

1. [百度百科-mysql函数](http://baike.baidu.com/view/2140086.htm)
2. [MysQL常用函数](http://bxbx258.blog.51cto.com/339450/106008)

---
