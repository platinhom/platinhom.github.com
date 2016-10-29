---
layout: post
title: MySQL学习2-数据库和报表
date: 2015-07-04 3:30:52
categories: IT
tags: Database SQL
---

现代的 SQL 服务器构建在 RDBMS 之上。

1. DBMS - 数据库管理系统（Database Management System）  
数据库管理系统是一种可以访问数据库中数据的计算机程序。DBMS 使我们有能力在数据库中提取、修改或者存贮信息。不同的 DBMS 提供不同的函数供查询、提交以及修改数据。
2. RDBMS - 关系数据库管理系统（Relational Database Management System）
RDBMS也是一种数据库管理系统，其数据库是根据数据间的关系来组织和访问数据的。20世纪70年代初，IBM公司发明了 RDBMS。RDBMS 是 SQL 的基础，也是所有现代数据库系统诸如 Oracle、SQL Server、IBM DB2、Sybase、MySQL 以及 Microsoft Access 的基础。  
RDBMS 中的数据存储在被称为表（tables）的数据库对象中。表是相关的数据项的集合，它由列和行组成。

可以把SQL分为两个部分：数据操作语言 (DML) 和 数据定义语言 (DDL),前者操作和改变数据,如select,update等;后者操作和改变表格数据库,如create和alter等.

----------

## 数据库

### 创建数据库

- `create database test_db character set gbk;`  
创建数据库,并设定字符编码.数据库名为test_db.注意最后分号语句结束的存在!不加分号会在下一行输入. 成功后 Query OK, 1 row affected(0.02 sec). 失败的话,可能没有权限如`ERROR 1044 (42000): Access denied for user 'Hom'@'localhost' to database 'hom_db'`.
- 数据库保存位置参看配置文件(my.ini/my.cnf)中`data_home_dir`相关信息,window一般在安装目录下data文件夹或者programdata/mysql下的data文件夹,linux系统一般在某个文件夹下var/mysql下.例如在xamppfiles目录下. 数据库名对应的是文件夹,里面报表文件等.

### 选择操作的数据库

- 可以使用 `show databases`; 命令查看已经创建了哪些数据库。注意复数..
- 登录时, 使用-D选项指明 `mysql -D 所选择的数据库名 -h 主机名 -u 用户名 -p`.
- 登录后,使用use. `use 数据库名;`.
- 只能选择操作一个数据库.使用use后会改变操作的数据库对象.

### 删除数据库

- `drop database name` 删除指定数据库
- `drop database if exists name;` 如果存在则删除

## 数据库表
数据库就如同一个excel文件, 而数据库表则相当于excel里面的每个sheet. 一个数据库可以包含多个数据库表.数据库表和sheet还是有区别的, 其有更严格的格式需求,虽然看上去差不多.  
![](http://images.cnitblog.com/blog/453818/201305/09030127-13657abaf11945d1916297e6d23f2ec9.png) 

- 表头(header): 每一列的名称;必须
- 列(row): 具有相同数据类型的数据的集合;
- 行(col): 每一行用来描述某个人/物的具体信息;
- 值(value): 行的具体信息, 每个值必须与该列的数据类型相同;
- 键(key): 表中用来识别某个特定的人\物的方法, 键的值在当前列中具有唯一性.主键同时是索引列.

### 创建数据库表

- 格式: `create table 表名称{列声明};` 列声明是表头.
- 列声明结构块: `{条目1,条目2...条目N}`,逗号分隔,一般为了好看分行.
- 条目的格式:`名字 类型 可否为空 其余限定`.前三者是必须的: 名字随便取.类型参看另一篇的说明,可否为空为`null/not null`,默认可为空. 全部用空格分隔. 
	- 这么多条目中需有一个主键. 这个主键是唯一的,用`primary key`声明. `id int unsigned not null auto_increment primary key,`就是一个主键例子.主键同时也是unique的,但表可以有多个unique键,只能有一个主键.
	- 主键一般伴随`auto_increment`(需在整数列中使用, 其作用是在插入数据时若该列为 NULL, MySQL将自动产生一个比现存值更大的唯一标识符值。在每张表中仅能有一个这样的值且所在列必须为索引列。)
	- `default '-'` 缺省值是'-'.
- 使用 `show tables;`命令可查看已创建了表的名称.注意复数..
- 使用 `describe 表名;` 命令可查看已创建的表的详细信息。

### 简单的输入和操作数据

- 插入一行数据: 插入一行数据:`insert [into] 表名 [(列名1, 列名2, 列名3, ...)] values (值1, 值2, 值3, ...);`.可以不值列名按顺序代入;也可以指明列名和对应的值,排好队就好了;有缺省值或自增的可以不指明.
	- `insert into students values(NULL, "王刚", "男", 20, "13811371377");`
	- `insert into students (name, sex, age) values("孙丽华", "女", 21);`
- 读取一列数据: `select 列名称 from 表名称 [查询条件];`
	- `select name, age from students;`
	- `select * from students where sex="女";`
- 修改数据: `update 表名称 set 列名称=新值 [where 更新条件];`
	- `update students set age=age+1;` 无条件全部操作
	- `update students set tel=default,age=19 where id=5;`通过某些条件定位到行.可以同时修改两项,逗号分隔.
- 删除一行数据: `delete from 表名称 where 删除条件;`
	- `delete from students where id=2;`删除一行
	- `delete from students;`删除所有

### 修改数据库表

- `alter table 表单 操作` 修改数据库表,包括:
	- `alter table 表名 add 列名 列数据类型 [after 插入位置];` 插入新列. after可以指明在哪列(列头名)之后插入,否则就追加.
	- `alter table 表名 change 列名称 列新名称 新数据类型;` 更改数据类型.就是把定一个列条目时的东东写一遍.
	- `alter table 表名 drop 列名称;` 删除一列
	- `alter table 表名 rename 新表名;` 重命名数据库表
- `drop table 表名;` 删除库表.

### 索引
在不读取整个表的情况下，索引使数据库应用程序可以更快地查找数据。您可以在表中创建索引，以便更加快速高效地查询数据。用户无法看到索引，它们只能被用来加速搜索/查询.可以认为,创建索引就是把所有可能的值预先提取出来并事先排序,有序化数据有利于更快速搜索,而且不用在一大块数据中进行移动(抽离出来了).  
**注释**：更新一个包含索引的表需要比更新一个没有索引的表更多的时间，这是由于索引本身也需要更新。因此，理想的做法是仅仅在常常被搜索的列（以及表）上面创建索引。
**unique唯一索引**: 唯一的索引意味着两个行不能拥有相同的索引值。主键也是唯一索引.  
索引的创建可以在CREATE TABLE语句中进行，也可以单独用CREATE INDEX或ALTER TABLE来给表增加索引。删除索引可以利用ALTER TABLE或DROP INDEX语句来实现。

1. 建立索引: (create和alter均可多列操作,中间用`,`.create不能造出主键).一般都需要把所有都指明.
	- 一般索引格式: `create index [index_name] on [table_name] ([column_name]);` 
	- 唯一索引格式: `create unique index [index_name] on [table_name] ([column_name]);`
		- create index ind_id on table1 (id);   
	- 一般索引: `alter table table_name add index [index_name] ([column_list]);`
	- 唯一索引: `alter table table_name add unique ([column_list]);`
	- 主键: `alter table table_name add primary key ([column_list]);`
2. 删除索引: 语法和建立索引类似,不用指明列而已.   
	- `drop index idx_id on table1;`   
	- `alter table table1 drop index idx_id;`
3. 更新自增索引起始值: `ALTER TABLE tablename AUTO_INCREMENT=1` 注意, 要是有比该值大的,会从最大值开始

**注释**: 索引名缺省是索引列第一列名称定出来的;

### Foreign Key 外键
一个表中的 FOREIGN KEY 指向另一个表中的 PRIMARY KEY。FOREIGN KEY 约束用于预防破坏表之间连接的动作。FOREIGN KEY 约束也能防止非法数据插入外键列，因为它必须是它指向的那个表中的值之一。

- `CREATE TABLE Orders(Id_O int NOT NULL,Id_P int,PRIMARY KEY (Id_O),FOREIGN KEY (Id_P) REFERENCES Persons(Id_P))`创表时声明
- `ALTER TABLE Orders ADD [constraint FK名] FOREIGN KEY (Id_P) REFERENCES Persons(Id_P)` 使用alter方法添加. foreign key..references table(indexname)...
- `ALTER TABLE Orders DROP FOREIGN KEY fk_PerOrders` 撤销外键

## Alter的修改数据库表和insert/select/Update/delete区别?

- 数据报表是以表头header为基础组织数据的,就像三维空间有XYZ三个坐标一样.而数据则是以每行每行每行的形式储存的,如每个原子的数据.  
- 修改原子的数据,就是操作数据, 选用insert/select/Update/delete, 而where定位条件是`列=条件`去操作,相当于操作某些指定原子.  
- 而Alter进行操作则是改变数据结构了, 例如新增原子半径, 原子电荷, 变为2维坐标. 均是整列整列操作, 没有行的筛选条件(因为对所有对象都起效). 要对行的某些数据进行操作, 又回到之前的insert/select/Update/delete+where去了.

## Reference

1. [w3school-sql](http://www.w3school.com.cn/sql/index.asp)  
2. [21分钟 MySQL 入门教程](http://www.cnblogs.com/mr-wid/archive/2013/05/09/3068229.html#d17) 
3. [漫谈数据库索引](http://kakajw.iteye.com/blog/1656532)

---
