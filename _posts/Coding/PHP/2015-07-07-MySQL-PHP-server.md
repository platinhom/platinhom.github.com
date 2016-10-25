---
layout: post
title: MySQL-PHP服务器构建用户系统
date: 2015-07-06 16:40:13
categories: Coding
tags: PHP Database SQL Website
---

由于服务器需要,我们需要一个用户注册系统储存使用用户信息.这里记录一下需要的步骤.

## 安装服务器端PHP和MySQL

一般PHP服务器都自带了(否则还做服务器啊..),注意一下版本号(phpinfo()).  
mysql不一定会装有及运行,那么请自行安装上mysql.并且设置好root密码. 要是不知道root密码要重设,请参看我之前写的[Ref1](http://platinhom.github.io/2015/07/04/MySQL-Study-install/).  
root密码一定要设置好,开启mysql服务(linux服务器一般是service mysql start). mysql这个名字和注册的服务有关,一般都是mysql这样子,正常启动服务后,会在后台运行mysqld. `ps -ef|grep mysqld`查看程序是否运行.运行`mysql -u root -p`并输入密码,成功的话就OK了(退出exit).mysql指令不能直接运行的话,请自行找到相应的mysql主程序并放到PATH搜索目录下,请自行google基础知识..

## phpMyAdmin 在线图形化管理系统
phpMyAdimin是在网上管理MySQL数据库系统的在线工具,十分方便易用,一般服务器套装如XAMPP一类的都会自带该工具.这里简介一下安装和使用.注意下载的版本和你服务器端php及mysql版本要合适.

### 安装
看看你的系统有没有安装(例如XAMPP里面就自带有该文件夹和工具), 没有的话按下述方法操作.

- 去[官网下载](https://www.phpmyadmin.net/downloads/) 因为基于PHP,所以你的系统需要能够使用PHP就可以了,随便哪个压缩包都可以.因为不用安装,不区分系统.
- 下载获得的是一个压缩包,解压.解压后的文件夹重命名为phpMyAdmin这样子,放到主页目录下或某个位置(保证网页结构能够访问该位置,或者将该位置加入网络结构)
- 将里面的config.sample.inc.php 文件复制一个命名为config.inc.php. 命令: `cp config.sample.inc.php config.inc.php`
- 更改配置文件config.inc.php: 
	- `$cfg['servers'][$i]['host'] = 'localhost';` 这里一般就是localhost就可以了如果要管理别的服务器的mysql,可以改为相应IP.
	- `$cfg['servers'][$i]['port'] = '';` mysqld端口, 一般默认是3306,留空就是使用默认的.要是更改过mysqld配置就改相应的端口
	- `$cfg['servers'][$i]['auth_type'] = 'http';` 可以用cookie,http,HTTP,config.config是无需用户名密码,不安全.常用cookie和http.php安装模式为apache，可以使用http和cookie;php安装模式为cgi，可以使用cookie. 我这里用http.
	- `$cfg['servers'][$i]['user'] = 'root';` 登陆访问mysql的用户名,一般是root.也可以是别的
	- `$cfg['servers'][$i]['password'] = '';` 使用的登陆密码.这个要和mysql登陆相应用户时密码一致. 可能在配置文件没有该行,自己加上去.
	- `$cfg['blowfish_secret'] = '';`如果认证方法设置为cookie，就需要设置短语密码,不能留空，否则会在登录phpmyadmin时提示错误.我使用http,所以不用设置╮(╯▽╰)╭
- 在文件夹下有index.php, 所以根据文件夹名字(区分大小写)就可以直接访问了,例如localhost/phpMyAdmin .这里区分大小写,我后来把文件夹重命名为小写,但是导入一些库时配置还是用部分大写..不知道是不是第一次运行时配置的还是里面有选项可以设定...总之用上面的名字就好了.
- 输入网址后,输入刚才填入的root的账号和密码,就可以登进去访问mysql了.主框右上角的数据库就是现有数据库,点进去就可以见到相应的table什么的了~~十分直观

## 构建MySQL数据库

- 登陆mysql的root账号, `mysql -u root -p` 
- 在服务器端新建一个数据库,例如test_db等,名字随便.`create database test_db character set utf8;`.这里使用utf8编码.
- 使用该数据库.`use test_db;`
- 新建相应table.并新建表头,设置主键, 以及其他信息. 如`create table users(id int unsigned not null auto_increment primary key, firstname char(40) not null);`
- 登陆phpMyAdmin, 数据库->test_db数据库->users表,进去后看看是否有相应表格及头信息.是的话就成功了.

~~~sql
create database test_db character set utf8;
use test_db;
create table users(id int unsigned not null auto_increment primary key, firstname char(40) not null, lastname char(40) not null, institute char(80) not null, email char(40) not null, department char(80) null default '-', title char(40) null default '-');
insert into users values(null,"Hello", "World", "Michigan State University", "helloworld@msu.edu", "Math", "Postdoc");
exit
~~~

## 注册系统页面及PHP处理

- 注册页面就是做一个table-form的形式,以POST形式提交数据并处理就可以了.下面的只是示例, HTML部分代码不全.
- 使用POST形式抓取数据,将数据预处理
- 使用`$con = mysql_connect("localhost","user","password");`获取一个MySQL对话对象
- 使用`mysql_select_db("test_db", $con); `来进行数据库选择
- 将SQL命令写到字符串$sql内,然后`$result=mysql_query($sql);`来进行处理和返回.SQL输入数据库的数据部分用相应变量代替即可.
- 分析结果,提取关联数组,然后就可以分析了,例如本例中利用Email地址来获取信息分析,要是相同信息用户就不输入数据库: `$row=mysql_fetch_array($result);`
- 关闭MYSQL对话`mysql_close($con);`

~~~php
<body>
<?php
  if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $firstname=$_POST["firstname"];
    $lastname=$_POST["lastname"];
    $email=$_POST["email"];
    $institute=$_POST["institute"];
    $department=$_POST["department"];
    $title=$_POST["title"];
    if ($department==""){$department="-";}
    if ($title==""){$title="-";}
    
    //save user information into database
    $con = mysql_connect("localhost","root","password");
    if (!$con){
       die('Could not connect: ' . mysql_error());
    } 
    mysql_select_db("test_db", $con); 
    $result=mysql_query("SELECT * FROM users where email='$email';");
    $row=mysql_fetch_array($result);
    if ($row['firstname']==$firstname && $row['lastname']==$lastname && $row['institute']==$institute){
    ;}//have registered before
    else{
         $sql="insert into users values(null,'$firstname','$lastname','$institute','$email','$department','$title');";
    }
    mysql_query($sql);
    mysql_close($con);
    
    echo "<p>Linux 64bit version: <a href='./program_linux64'><img src='download.gif'></a></p>";
    echo "<p>Window 64bit version: <a href='./program_win64.exe'><img src='download.gif'></a></p>";
    echo "<p>Mac OS version: <a href='./program_mac64'><img src='download.gif'></a></p>";
    exit(0);
  }
?>

<div id="regbox">
<table border="0" id="maintable" style="font-size:14pt;" cellspacing="6px">
<form name="form1" method="post" enctype="multipart/form-data" action="test.php" onsubmit="return validator(this)">

  <tr>
    <td><label for="firstname">First Name:</label></td>
    <td><input name="firstname" id="firstname" size="40" type="text" onMouseOver="this.style.borderColor='#9ecc00'" onMouseOut="this.style.borderColor='#D2D9D8'" valid="required" errmsg="First name is required!"/>*<span id="errMsg_firstname" style="color:#FF0000"></span></td>
  </tr>
  <tr>
    <td><label for="lastname">Last Name:</label></td>
    <td><input name="lastname" id="lastname" size="40" type="text" onMouseOver="this.style.borderColor='#9ecc00'" onMouseOut="this.style.borderColor='#D2D9D8'" valid="required" errmsg="Last name is required!"/>*<span id="errMsg_lastname" style="color:#FF0000"></span></td>
  </tr>
   <tr>
    <td><label for="email">Email:</label></td>
    <td><input name="email" id="email" size="40" type="text" onMouseOver="this.style.borderColor='#9ecc00'" onMouseOut="this.style.borderColor='#D2D9D8'" valid="required|isEmail" errmsg="Email is required!|Invalid email!"/>*<span id="errMsg_email" style="color:#FF0000"></span></td>
  </tr>

  <tr>
    <td><label for="institute">Institute:</label></td>
    <td><input name="institute" id="institute" size="40" type="text" onMouseOver="this.style.borderColor='#9ecc00'" onMouseOut="this.style.borderColor='#D2D9D8'" valid="required" errmsg="Name for your institute is required!"/>*<span id="errMsg_institute" style="color:#FF0000"></span></td>
  </tr>
  <tr>
    <td><label for="department">Department:</label></td>
    <td><input name="department" id="department" size="40" type="text" onMouseOver="this.style.borderColor='#9ecc00'" onMouseOut="this.style.borderColor='#D2D9D8'" /></td>
  </tr>
  <tr>
    <td><label for="title">Title:</label></td>
    <td><input name="title" id="title" size="40" type="text" onMouseOver="this.style.borderColor='#9ecc00'" onMouseOut="this.style.borderColor='#D2D9D8'" /></td>
  </tr>

  <tr><td colspan="2"><br> </td></tr>
  
  <tr>
	<td colspan="2" align="center"><input type="submit" name="submit" value="Register and Download MIBPB" style="font-size:18pt;" onMouseOver="this.style.borderColor='#9ecc00'" onMouseOut="this.style.borderColor='#D2D9D8'"/></td>
  </tr>

</form>
</table>
</div>
</body>
~~~

## Reference

1. [MySQL学习1-安装登录和用户管理](http://platinhom.github.io/2015/07/04/MySQL-Study-install/)
2. [phpMyAdmin](https://www.phpmyadmin.net/)
3. [W3S-PHP mysql](http://www.w3school.com.cn/php/php_mysql_intro.asp)

---
