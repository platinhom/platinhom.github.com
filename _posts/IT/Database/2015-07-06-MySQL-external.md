---
layout: post
title: MySQL学习6-外部数据交流
date: 2015-07-06 4:24:32
categories: IT
tags: Database SQL
---

## 导出数据

导入外部数据文本:   
1.执行外部的sql脚本   
当前数据库上执行:mysql < input.sql  
指定数据库上执行:mysql [表名] < input.sql  
2.数据传入命令 load data local infile "[文件名]" into table [表名];   
备份数据库：(dos下)   
mysqldump --opt school>school.bbb   
mysqldump -u 用户名  -p  需要备份的数据库名 >备份的文件的保存路径和文件名

备份数据库：(将数据库test备份)   
mysqldump -u root -p test>c:/test.txt   
备份表格：(备份test数据库下的mytable表格)   
mysqldump -u root -p test mytable>c:/test.txt   
将备份数据导入到数据库：(导回test数据库)   
mysql -u root -p test   

 
## 导入数据

source d:\datafilename.sql 
 

导入数据库备份文件：   
(1).在mysql命令窗口   
(2).新建一个要导入的数据库(因为备份中没有备份建数据库操作)   
(3).use 当前库名   
(4).source 备份的文件的保存路径和文件名(此命令不能加分号结尾)  

分页查询：select *from 表名 limit 每页数量 offset 偏移量;
 

查询时间：select now();   
查询当前用户：select user();   
查询数据库版本：select version();   
查询当前使用的数据库：select database();

## PHP控制简介

`mysql_connect(servername,username,password);`,servername一般是localhost:3306, 也可以忽略端口.

~~~php
$con = mysql_connect("localhost","peter","abc123");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

// some code

if (mysql_query("CREATE DATABASE my_db",$con))
  {
  echo "Database created";
  }
else
  {
  echo "Error creating database: " . mysql_error();
  }

mysql_close($con);
~~~

~~~sql
create table users(id int unsigned not null auto_increment primary key, firstname char(40) not null, lastname char(40) not null, institute char(80) not null, email char(40) not null, department char(80) null default '-', title char(40) null default '-');
insert into users values(null,"Firstname", "Lastname", "Michigan State University", "hello@msu.edu", "Math", "Postdoc");

~~~

TODO: 这篇迟点再补全了..

## Reference

1. [w3s-php-mysql](http://www.w3school.com.cn/php/php_ref_mysql.asp)
2. [w3s-php-mysqli](http://www.w3school.com.cn/php/php_ref_mysqli.asp)

---
