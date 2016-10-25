---
layout: post_small
title: MySQL总结-Xiang
date: 2015-07-07 07:22:22
categories: IT
tags: Database SQL
---


1. show character set;查看所支持的字符集啥的
2. show variables like 'character%'
3. set character\_set\_database=gbk;
4. source c:\mysql\init.sql执行脚步文件


## 数据库有关

1. create database choose;创建choose数据库
2. show database;查看数据库
3. show create database choose;显示数据库结构
4. use choose;后续使用的都是choose数据库的对象
5. drop database student;删除student数据库

## 表有关

1. show engines;查看存储引擎
2. MyISAM不支持外键，但不知道有啥影响
3. set default\_storage\_engine=MyISAM;设置默认存储引擎
4. alter table my_table engine=MyISAM;
5. des table_name查看表结构
6. show create table table_name；查看表详细信息
7. drop table table_name;删除表
8. mysql里，系统变量以@@开头，用户变量以@开头
9. show global variables;查全局变量
10. show session variab1s；查当前会话变量

### 类型：

1. 区分timestamp以及datetime
2. now（）获得当前系统时间


### 创建表：
1. 设置主键：student_no char(11) primary key
2. 复合主键：primary key (字段名1，字段名2)
3. 自增型字段：字段名 数据类型 auto_increment
4. 存储引擎类型设置：engine=innodb；
5. default charset=字符集类型
6. 复制表结构：create table 新表名 like 源表
7. 复制表：create table 新表名 select * from 源表


### 修改表：

1. 删除字段：alter table 表名 drop 字段名
2. 加字段：alter table 表名 add 新字段名 新数据类型  
      【新约束条件】【first|after 旧字段名】
3. 修改字段名：alter table 表名 change 旧字段名 新字段名 新数据类型  
                      rename table 旧表名 to 新表名
4. 修改字段类型：alter table 表名 modify 字段名 新数据类型
5. 约束条件：alter table 表名 add constraint 约束名 约束类型（字段名）
6. 删主键约束条件：alter table 表名 drop primary key
7. 删外键约束条件：alter table 表名 drop foreign key 约束名
8. alter table 表名 auto_increment=新的初始值

## 索引：

1. 原则:表的某个字段值离散度越高，该字段越适合选作索引的关键字
2. 原则:占用储存空间少的字段更适合选作索引的关键字
3. 原则:较频繁地作为where查询条件的字段应该创建索引，分组字段或者排序字段应该创建索引，两个表的连接字段应该创建索引
4. 原则:更新频繁的字段不适合创建索引，不会出现在where子句中的字段不应该创建索引。
5. 原则:最左前缀原则
6. 原则:尽量使用前缀索引

### 创建索引：

1. `create [unique|fulltext] index 索引名 on 表名(字段名[(长度)] [asc|desc])`
2. `alter table 表名 add [unique|fulltext] index 索引名`
删除索引：drop index xx on 表名



### 表记录操作：

1. 插入：insert into 表名 [(字段列表)] values (值列表)
2. 插入：insert into 表名[(字段列表)] select (字段列表2) from 源表 where 条件表达式
3. 插入：replace into 表名 xxxxxxxxx
4. 表记录修改：update 表名 set 字段名1=值1，字段名2=值2 where a=b
5. delect from 表名 where a=b
6. 清空表truncate table

### 查询：

1. select * from table limit 1,3；从第二行起的3条记录
2. select * from table where a between .. and ..;
3. liek:%代表一窜字符，_代表一个字符，涉及有下划线记住转义
4. escape作为转义字符：select * from x where a like ‘%！_%’escape ‘！’
5. select name,group_concat(distinct score order by score desc separator ',')将一个集合的值合起来
6. union会去掉重复值union all不会去掉重复值
7. 子查询里any例子：“表达式>any(子查询)”表示至少大于子查询结果集中的某一个值
8. 子查询里all例子：“表达式>all(子查询)”表示大于子查询结果集中的任一个值
9. 子查询exist，检验查询结果是否为空
10. 全文检索例子：检索书名或者简介中涉及到practise或者cookbook单词的所有图书信息。  
select * from book where match (name,brief_introduction) against ('practices cookbook')\G


### 编程方面：

1. set @variable1='ni mei chixiang';
2. select 中赋值。select @var1:=expression1
3. select 中赋值。select expression1 into @var1.....
4. declare的变量，要放在begin...end之间使用
5. 查看指定数据库所有函数   
select name from mysql.proc where db='xiang' and type='function';  
或者使用show function status查看当前自定义函数
6. 删除函数drop function xxx;
7. 函数创建

~~~sql
create function 函数名(var1,var2,...)
return 返回值的数据类型
begin
    函数体;
    return 语句；
end；
~~~


## 条件语句：  

1. if.  
if xx then xx;  
elseif xx then xx;  
end if;  
2. case.  
case 表达式  
when value1 then 语句块1；  
when value2 then 语句块2；  
else 语句块；  
end case；  

## 循环：  

1. while  
while 条件表达式 do  
循环体；  
end while；  
2. leave语句  
跳出循环用  
leave 循环标签；  
3. iterate语句  
跳出这次循环，执行下次循环  
iterate 循环标签；  
4. repeat：条件为假时反复执行，直至为真结束  
repeat  
循环体；  
until 条件表达式  
end repeat [循环标签];  
5. loop  
loop  
循环体；  
if 条件表达式 then  
leave [循环标签]；  
end if；  
end loop；  


## 未知但感觉有用的函数

~~~sql
charset(x)，返回x的字符集
char_length(x),获取字符串x的长度
length(x)获取字符串x字节数
md5（）用于加密
encode decode也能进行加密解密
concat(x1,x2,...)将x1,x2等连接成新字符串
concat_ws(x,x1,x2,...)用x将x1,x2...连在一起
ltrim rtrim去左或右边的空格trim去两边空格
trim ([leading|both|trailing] x1 from x2)从x2去掉x1
left(x,n) right(x,n)截取左或右边前n个字符
upper(x)大写 lower(x)小写
lpad(x1,len,x2)将字符串x2填充到x1的开始处，使字符串x1的长度达到len
rpad(x1,len,x2)将字符串x2填充到x1的结尾处，使字符串x1的长度达到len
substring(x,start,length),mid(x,start,length)  从x的第n个位开始获取长度length的字符串
instr(x2,x1)x2里面获取x1 的位置
insert(x1,start,length,x2)  x1里从start起的length位替换为x2
replace(x1,x2,x3)用x3，替换x1里面的x2
repeat(x,n)将x复制n次
strcmp(x1,x2),x1>x2返回1，等于返回0，x1<x2返回-1
reverse（x）逆序
数据类型转换 convert(x,type) cast(x as type)
if(condition,v1,v2)  ifnull(v1,v2):如果v1为null,返回v2否则返回v1
database()获取当前操作数据库
curdate(),current_date(0获取当前日期
curtime(),current_time()获取当前时间
now(),current_timestamp(),localtime(),sysdate()获取当前日期时间
year() month() dayofmonth() hour() minute() second()
~~~

### 视图：

create view 视图名 as select 。。。  
show tables；列出所有基表，也会列出视图    

### 建立临时表：

create temporary table   
drop temporary table  




---
