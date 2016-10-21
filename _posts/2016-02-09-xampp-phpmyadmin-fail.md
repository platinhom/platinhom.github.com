---
layout: post
title: xampp:自装phpMyAdmin失败(或连不上)
date: 2016-02-09 13:03:17
categories: IT
tags: Internet PHP SQL
---

# phpMyAdmin Fail in XAMPP

今天想本地装个phpMyAdmin管理数据库(架构在XAMPP上), 然而改掉mysql密码后一直连不上去..

> phpMyAdmin 尝试连接到 MySQL 服务器，但服务器拒绝连接。您应该检查配置文件中的主机、用户名和密码，并确认这些信息与 MySQL 服务器管理员所给出的信息一致。

奇怪了, 改了配置文件 `phpMyAdmin/config.inc.php` 的MySQL用户和密码, 改了http验证, 一样上不去....

~~~
/*
 * Servers configuration
 */
$i = 0;

/**
 * First server
 */
$i++;
/* Authentication type */
$cfg['Servers'][$i]['auth_type'] = 'http';
/* Server parameters */
$cfg['Servers'][$i]['host'] = 'localhost';
$cfg['Servers'][$i]['connect_type'] = 'tcp';
$cfg['Servers'][$i]['compress'] = false;
$cfg['Servers'][$i]['AllowNoPassword'] = false;
$cfg['Servers'][$i]['user'] = 'root';
$cfg['Servers'][$i]['password'] = 'imnotpassword';
~~~

PS: 原来是没有user和password项的, auth_type默认是`cookies` (其实清空cookies后用cookies登录是不是更好?).

搜了网上一些方法, 也就只是说这么做.. 我清空了localhost的和127.0.0.1的cookies依然不成...

最后我把网址`localhost/phpmyadmin` 改为了`localhost/phpMyAdmin` 就成了..

## 故障原因

xampp 也是预装有phpMyAdmin的, 所以我root无密码登上去时显示的phpMyAdmin版本是旧版而不是新版就是这个原因..因为我登的是旧版的..

在`xampp/apache/conf/extra/httpd-xampp.conf`的配置文件里, 定义了以下内容:

~~~
Alias /phpmyadmin "C:/xampp/phpMyAdmin/"
<Directory "C:/xampp/phpMyAdmin">
    AllowOverride AuthConfig
    Require all granted
</Directory>
~~~

所以使用小写`localhost/phpmyadmin`时登上去的是xampp版本的, `localhost/phpMyAdmin`登上去才是自己安装的版本的, 修改自己安装版本的root和密码当然对xampp版本不起效啦!~~

这种大小写区分不太好,可以修改apache中xampp配置文件重新指向或者将新装的文件夹改个名字,例如phpadmin 就好了.

------
