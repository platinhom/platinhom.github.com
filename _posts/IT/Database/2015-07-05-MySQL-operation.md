---
layout: post_small
title: MySQL学习4-操作命令
date: 2015-07-05 10:37:58
categories: IT
tags: Database SQL
---

# 主句

## 数据

- `SELECT`: 选择和显示数据
	- `select 列名称 from 表名称 [查询条件];` 一般通式. 可以选择1或多列数据(多列名要`,`分隔)
	- `select 列名称 from 表名称 where 列 运算符 值;` where子句用于查询条件,请参看where子句
	- `SELECT DISTINCT 列 FROM 表 ` distinct关键词就是选取结果不重复
	- `select 列名称 from 表名称 order/desc by 列` 根据列来升序/降序排列结果
	- `select 列名 INTO 新表 [IN '外部数据库'] FROM 旧表` 将旧表数据复制到新表中.
	- `SELECT function(列) FROM 表` 使用选择后并函数处理
- `INSERT`: 插入一行数据
	- `INSERT INTO 表名称 VALUES (值1, 值2,....)` 输入所有值并插入,不需要列名
	- `insert [into] 表名 (列名1, 列名2, 列名3, ...) values (值1, 值2, 值3, ...);` 可以选择只填个别值.列和值要对上.
- `UPDATE`:更新修改数据
	- `UPDATE 表名称 SET 列名称 = 新值 WHERE 列名称 = 某值` 将满足条件该行某列值替换掉.前后列名无需相同. 多个同时替换时使用`,`分隔.
	- `UPDATE 表名称 SET 列名称 = 新值` 所有行对应列均进行如此修改
- `DELETE`:删除某行.删除一个值使用UPDATE办法
	- `DELETE FROM 表名称 WHERE 列名称 = 值` 删除满足条件的行
	- `DELETE FROM 表名称` 删除所有行数据
- `FILE`
- `TRUNCATE TABLE`删除表格数据

## 结构

- `CREATE`: 创建数据库,报表等
	- `create database 数据库名 选项;` 
	- `create table 表名称{列声明};` 
	- `create temporary table 表名(列声明);`建立临时表格
	- `create table table2 select * from table1;`复制并创建新表格. 后面还可以跟where来过滤.
- `ALTER`: 修改报表信息
	- `alter table 表名 add 列名 列数据类型 [after 插入位置];` 插入新列. after可以指明在哪列(列头名)之后插入,否则就追加.
	- `alter table 表名 change 列名 列新名称 新数据类型;` 更改数据类型同时改名
	- `alter table 表名 modify 列名 新类型;`修改该列的类型,不改列名.  
	- `alter table 表名 drop 列名;` 删除一列
	- `alter table 表名 rename 新表名;` 重命名数据库表
	- `ALTER table 表名 AUTO_INCREMENT=1;` 使得自增从1开始(还是受最高值控制)
- `INDEX`
- `DROP`: 删除数据库或报表
	- `drop database [if exist] 数据库名 `
	- `drop table 表名;`
- `CREATE TEMPORARY TABLES`
- `SHOW` 显示对象,对象一般复数
	- `show databases`
	- `show tables`
	- `show columns from tablename;`
	- `SHOW INDEX FROM table_name`
- `SHOW VIEW`
- `DESC`或`DESCRIBE`: 显示表的结构
	- `desc tablename` 显示表的结构:列名,类型,null,key,缺省,额外属性
- `CREATE ROUTINE`
- `ALTER ROUTINE`
- `EXECUTE`
- `CREATE VIEW`: 创建给用户看的表格,视图在每次用户需要时打开,读取数据库的结果展示.和excel差不多.
	- `CREATE VIEW view_name AS select句`: 将选择结果作为视图,并有命名.viewname一般用中括号?所谓视图其实和excel表格很像.视图也可以像table一样被select被操作.
	- `DROP VIEW view_name`:删除视图
- `EVENT`
- `TRIGGER`

## 管理

- `GRANT` 授权:
	- `grant 操作 on 数据库 to 用户 identified by '密码'`,常见`all privileges on *.*`.可改密码,可创建用户
- `REVOKE` 取消授权:
	- `revoke 操作 on 数据库 to 用户` 
- `SUPER`
- `PROCESS`
- `RELOAD`
- `SHUTDOWN`
- `LOCK TABLES`
- `REFERENCES`
- `REPLICATION CLIENT`
- `REPLICATION SLAVE`
- `CREATE USER`
- `flush privileges` 刷新权限

# 子句/辅助修饰

- `where 列 运算符 值`: 常用查询条件,一般在select,update,delete中用.
	- `where 列1 = 值1 and/or 列2 <> 值2` 比较运算符和逻辑运算符匹配
	- `where 列 like 匹配串;` Like操作符使用字符串匹配来查询
	- `where 列 in (value1,value2);` 满足其中一个值
	- `where 列 between val1 and val2` 在两个值之间,MySQL是包括两头(不同SQL语言定义不同)
	- `where 列 not 上面条件` 不符合条件的
- `order by colA [asc], colB [desc]`: 按升序/降序排列结果, 先按colA来排,相同的根据colB来排.asc升序默认,desc降序
- `group by colA`: 根据colA来分组,将相同的作为一组,一般都作为下一个函数或处理时使用.如"SELECT Customer,SUM(OrderPrice) FROM Orders GROUP BY Customer"根据用户名先分组然后将用户名和对应用户分组的总和显示出来
- `Limit n`头几行;`limit n,m` 就是n+1到n+m行(即默认n=0).
	- `limit m offset n`等价于`limit n,m`offset偏移量就是第一个值,从0开始.为了另一种数据库兼容引入的.
	- `where condition group by remark order by regdate limit 6` 先过滤,分组 再排序,显示前6行.LIMIT放最后 这是语法不能颠倒。
- `having function(col) 操作符 值` 和where类似,进行条件筛选,区别在于having用函数,where直接用列值. 位置跟在group by后.
- `join 表2 on 表1.colA=表2.colB` 根据两列中匹配情况获得新表(一般是两表某些列的合并),有几种变体.
	- `join`或`inner join`:当表1的列中在表2列中有最少一个匹配时,就展示.展示顺序根据表1该列来. 如"select 展示列 from 表1 join 表2 on 表1.colA=表2.colB"(表1中该列有,表2没有就不会显示.)
	- `left join`:不管有无匹配,均把表1的列出来合并上表2对应的列.表2中没有匹配的为空.
	- `right join`:不管有无匹配,均把表2的列出来合并上表1对应的列.表1中没有匹配的为空.展示顺序依旧按表1来,表2有表1无的列在最低.
	- `full join`: 不管有无匹配,两个表两列的对应都列出来.顺序按表1来,不匹配的放最后.
- `union`和`union all`: 合并两单列显示.
	- `SELECT column_name(s) FROM table_name1 UNION SELECT column_name(s) FROM table_name2` 合并两列显示,重复的会去掉.
	- union all会把合并重复的也显示出来.
- `As alias` 别名,
	- 表别名尤其在多表格时常用,如"select p1.A,p2.A from peopleA as p1,peopleB as p2"
	- 别名也可以对列名进行别名化,此时输出结果将按别名来.可以暂命名结果. "SELECT LastName AS Family, FirstName AS Name FROM Persons"
- `if exists`和`if not exists` 一般用于是否存在数据库/表格时的判断,如"create table if not exists 表名{}".
- `default value` 一般是在声明表头时用来指明其缺失值,算属性吧.去default属性:"ALTER TABLE 表名 ALTER 列名 DROP DEFAULT"
- `auto_increment` 自增属性,可以'AUTO\_INCREMENT=10'来设定起始值.一个表只有一个该字段,一般是主键. 'ALTER TABLE 表名 AUTO\_INCREMENT=100'可以改变自增起始值(但受限于该列最大值)
- `primary key (column_list)`:建立主键.更常用是在create表头时追加属性.'alter table table_name add primary key ([column-list]);'
- `FOREIGN KEY (Id_P) REFERENCES 表1(Id_P)`:建立指向表1的外键,例如'ALTER TABLE 表2 ADD [constraint FK名] FOREIGN KEY (IdP) REFERENCES 表1(IdP)'
- `check(列 操作符 值)`: 限定条件,例如不小于0. 
	- 一般在定义完列以后加入,例如"CREATE TABLE 表名(colA int NOT NULL, colB varchar(255) NOT NULL,CONSTRAINT chk\_name CHECK (colA>0 AND colb=value)" check在mysql单独列出来,在其他数据库可能紧跟列声明. constraint是给限制起名.
	- Alter方法: "ALTER TABLE 表名 ADD CONSTRAINT 限制名 CHECK (colA>0)",限制名部分可不要
	- 撤销限制: "ALTER TABLE 表名 DROP CHECK 限制名"
- `Null`和`Not Null`专门声明是否能为空.如果不能为空,就限制了不能不赋值!

TODO: 补全

---
