---
layout: post
title: MySQL学习3-数据和数据操作
date: 2015-07-05 06:59:48
categories: IT
tags: Database SQL
---

SQL 对大小写不敏感！

## 三大数据类型

1. 数字类型
	- 整数: tinyint、smallint、mediumint、int、bigint
	- 浮点数: float、double、decimal
2. 日期和时间: date、time、datetime、timestamp、year
3. 字符串类型
	- 字符串: char、varchar
	- 文本: tinytext、text、mediumtext、longtext
	- 二进制(可用来存储图片、音乐等): tinyblob、blob、mediumblob、longblob

tinyint(m) |1字节 | 范围(-128~127)
smallint(m) | 2字节 | 范围(-32768~32767)
mediumint(m) | 3字节 | 范围(-8388608~8388607)
int(m) | 4字节 | 范围(-2147483648~2147483647)
bigint(m) | 8字节 | 范围(+-9.22*10的18次方)
float(m,d) | 4字节 | 单精度(8位精度)浮点型, m总个数，d小数位
double(m,d) | 8字节 | 双精度(16位精度)浮点型, m总个数，d小数位
decimal(m,d) | | 定点数, 参数m<65是总个数，d<30是小数位(d<m)。
char(n)	| |固定长度，最多255个字符
varchar(n)| |可变长度，最多65535个字符
tinytext | | 可变长度，最多255个字符
tinyblob | | 不超过255字符2进制串
text | | 可变长度，最多65535个字符
blob | | 不超过65535字符二进制数据
mediumtext | |可变长度，最多2的24次方-1个字符
mediumblob | |最多2的24次方-1个字符二进制数据
longtext | | 可变长度，最多2的32次方-1个字符
longblob | | 最多2的32次方-1个字符二进制数据
date | 3字节 |日期 '2008-12-2'(1000-01-01/9999-12-31)
year | 1字节 | 年份 2008(1901-2155)
time | 3字节 | 时间 '12:25:36'
datetime | 8字节 | 日期时间 '2008-12-2 22:06:44'
timestamp | 8字节 | 自动存储记录修改时间
ENUM(x,y,z..) | | 可能值的列表.最多列出65535个值,没匹配则为空.
SET	| | 与ENUM类似,SET最多只能含64个项,不过可存储一个以上值。
NULL| | 特殊类型,无,不等价于0或''.

- 数值型括号的m规定最大位数
- unsigned 跟在整型后,范围从0开始,可以使正整数范围翻倍.(表示非负数的意思)
- char(n) 固定长度,总将占用n个字节;varchar是存入的实际字符数+1个字节（n<=255）或+2个字节(n>255),所以varchar(4),存入3个字符将占用4个字节。varchar会根据长度调整大小.char比varchar要快.
- varchar超过255字节会转为text类似,留两个空字节作为结束符标记.所以varchar是tinytext+text的综合.
- 若定义一个字段为timestamp,这个字段里的时间数据会随其他字段修改的时候自动刷新,所以这个数据类型的字段可以存放这条记录最后被修改的时间。
- 如果ENUM列表中不存在插入的值，则插入空值。注释：这些值是按照你输入的顺序存储的。可以按照此格式输入可能的值：ENUM('X','Y','Z').
- NULL 值.如果表中的某个列是可选的，那么我们可以在不向该列添加值的情况下插入新记录或更新已有的记录。这意味着该字段将以 NULL 值保存。
NULL 值的处理方式与其他值不同。NULL 用作未知的或不适用的值的占位符。注释：无法比较 NULL 和 0；它们是不等价的。 is null/ is not null操作符用于判断空值


## 数据选择

### where子句 `where 列 运算符 值`
常用`SELECT 列名称 FROM 表名称 WHERE 列 运算符 值`,一般在select,update,delete中用.  
条件值使用单引号来表明是字符串,数值型不要使用单引号。

- `=`	等于
- `<>`	不等于(mysql还支持用!=)
- `>`	大于
- `<`	小于
- `>=`	大于等于
- `<=`	小于等于
- `BETWEEN .. AND`	在某个范围内,MYSQL是[]型(两头都包括)
- `LIKE`	搜索某种匹配模式
- `IN`  后面是(值1,值2..).多种可能指定值匹配
- `not` 不满足后面条件的.
- `and` 两个不同条件的同时匹配
- `or` 两个不同条件匹配其中之一. 复杂条件运算请多使用括号.
- `REGEXP` 后面跟正则表达式.参看Ref4
- `is null`和`is not null` 专门用来判断空值

### SQL 通配符和Like操作符
在对字符串数据匹配时使用.注意在权限啊列选择啊等时还是使用一般的"*".  
一般配合Like操作符使用`LIKE 'C%on'`这样,需要LIKE关键词

- `%`	替代一个或多个字符
- `_`	仅替代一个字符
- `[charlist]`	字符列中的任何单一字符
- `[^charlist]或者[!charlist]`	不在字符列中的任何单一字符

## Reference

1. [英文W3-Sql数据类型](http://www.w3schools.com/sql/sql_datatypes_general.asp)
2. [W3S-SQL 数据类型](http://www.w3school.com.cn/sql/sql_datatypes.asp)
3. [RUNOOB-MySQL教程](http://www.runoob.com/mysql/mysql-tutorial.html)
4. [MySQL-正则表达式](http://www.runoob.com/mysql/mysql-regexp.html)

---
