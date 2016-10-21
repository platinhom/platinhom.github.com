---
layout: post
title: Python:MySQLdb模块操作数据库
date: 2016-02-01 05:56:02
categories: Coding
tags: Python SQL
---

**MySQLdb模块**也就是常见的**MySQL-Python** (或**MySQL for Python**). 可以说是MySQL在Python最基础的模块.

在Mac上貌似不需要安装. 而在window里需要[下载安装](https://sourceforge.net/projects/mysql-python/). `import MySQLdb`测试一下就好了.

基本上, 就是连接服务器, 打开数据库, 创建执行指针, 执行sql命令, 处理返回几个基本步骤, 并无什么特别的. 关键还是SQL语句嘛.

例如简单的一个打开数据库查询所有结果的示例:

~~~python
import MySQLdb
 
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='test',port=3306)
    cur=conn.cursor()
    cur.execute('select * from user')
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
~~~

port一般可以不指名. db是打开的数据库, 不指明的话, 可以用服务器连接对象的`conn.select_db(database_name)`来实现, 当然也可以用SQL命令`USE databae`来实现啦.

当不是进行查询而是进行修改, 需要用`conn.commit()`来提交修改并更新数据库.

`cur.executemany('insert into test values(%s,%s)',values)` 可以将列表等的值逐一赋给sql式并执行(这里的values是[(a,b),(c,d)...])的格式.


## Reference

1. [MySQLdv模块官网](https://sourceforge.net/projects/mysql-python/)和[项目主页](http://mysql-python.sourceforge.net/)
1. [MySQLdb User's Guide](http://mysql-python.sourceforge.net/MySQLdb.html)
3. [python操作mysql数据库](http://www.runoob.com/python/python-mysql.html)

------
