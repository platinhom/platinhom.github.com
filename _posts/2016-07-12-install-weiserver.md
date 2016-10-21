---
layout: post
title: 在新的ubuntu虚拟服务器建立服务器
date: 2016-07-12 14:46:56
categories: IT
tags: System
---

Ubuntu 16.04 LTS

如有问题,查找错误: `vi /var/log/apache2/error.log`.

~~~bash
# change user password and add ssh key
sudo passwd username
vi ~/.ssh/authorized_keys

# need for amber:
sudo apt-get install csh
sudo apt-get install gfortran
## X11 need
sudo apt-get install xorg-dev
## need for NAB and antechamber
sudo apt-get install flex
## flexible to install
sudo apt-get install zlib1g-dev libbz2-dev
## openmpi for amber
sudo apt-get install openmpi-bin

# install php
sudo apt-get install php
sudo apt-get install libapache2-mod-php7.0
### 加密扩展库和curl用于异步
sudo apt-get install php7.0-mcrypt
sudo apt-get install php7.0-curl

# install mysql
sudo apt-get install mysql-server
#sudo apt-get install mysql-server-core-5.7
#sudo apt-get install mysql-client-core-5.7
sudo apt-get install php-mysql
# the following needed by phpMyAdmin, maybe fail for php-mysqli when Ubuntu-16
sudo apt-get install php-mbstring
sudo apt-get install php-mysqli

# restart service
sudo service apache2 restart
sudo /etc/init.d/mysql restart
~~~

## 关于权限的进一步调试:

Default user and group for apache2: www-data

~~~bash
sudo chown -R yourname:www-data foldername
sudo chmod -R g+x foldername
~~~

## 额外安装AmberTools16

~~~bash
tar -xjf AmberTools16.tar.bz2
# Configure AMBERHOME for once
export AMBERHOME=`pwd`
# it will install many softwares!
./configure gnu
# It should be load!
source /home/user/Software/Amber16/amber.sh
make install
# To install openmp version, do following one more time
./configure -openmp gnu
source /home/user/Software/Amber16/amber.sh
make install
~~~

## Bug

###### 异步问题

异步asynchronous call, 打断时间那里可以用`CURLOPT_TIMEOUT_MS`毫秒(默认秒, 只在新版本支持)

~~~php
$curl = curl_init();
 
curl_setopt($curl, CURLOPT_URL, 'http://www.mysite.com/myscript.php');
curl_setopt($curl, CURLOPT_FRESH_CONNECT, true);
curl_setopt($curl, CURLOPT_TIMEOUT, 1);
 
curl_exec($curl);
curl_close($curl);
~~~

因为我在另一个脚本进行异步调用的原因, 新服务器解析网址有点慢..TIMEOUT设置1会导致这步响应没完成就结束从而导致脚本没有继续执行. 解决办法是增大时间, 更好是整合为一个脚本或者把下载一步放到主脚本内. 先随便改个6秒吧..

后来在上传文件时依然有问题. 原因是PHP7里面已经移除了一些旧式用法, 更新为新用法即可, 参考[PHP利用curl来Post表单和上传文件](/2015/07/03/PHP-curl-postwithfile/)可解决. 

###### phpMyAdmin问题

安装下载: [官方地址](https://www.phpmyadmin.net/downloads/),下载解压后放置到某个目录即可运行.

不能登录问题, 设置登录方式http/cookie 或者用户密码都不能解决.

查找apache2/error.log 找到以下错误

> PHP Fatal error: Uncaught Error: Call to undefined function mb\_detect\_encoding() phpmyadmin

参考[PHP Fatal error when trying to access phpmyadmin mb_detect_encoding](http://stackoverflow.com/questions/13351635/php-fatal-error-when-trying-to-access-phpmyadmin-mb-detect-encoding)和[Fatal error: Call to undefined function mb_detect_encoding()](http://stackoverflow.com/questions/17204437/fatal-error-call-to-undefined-function-mb-detect-encoding), 查看phpinfo后发现缺了两个重要php库:mbstring和mysqli, 安装即可.

> PHP Fatal error:  Uncaught Error: Call to undefined function mysql_connect()

网上说没有安装php_mysql.装好后依然不行,有说修改` /etc/php/7.0/apache2/php.ini`移除mysql相应extension的注释,但在7.0只有mysqli没有mysql...依旧不行.  
原因是PHP7.0 ([>5.5被废弃,7移除了](http://php.net/manual/en/function.mysql-connect.php))已经废弃了`mysql_*`函数取而代之使用`mysqli_*`代替. 一些说明参考[MySQL Improved Extension](http://php.net/manual/en/book.mysqli.php)

~~~php 
$con=mysqli_connect(hostname, user, passwd) //the same
if (!$con){
       die('Could not connect: ' . mysqli_error());
}
//// Notice: the argument with different order!!!
//mysql_select_db(dbname,$con);
mysqli_select_db($con, dbname);
//mysql_query(query)
$result=mysqli_query($con, query_string);
//mysql_fetch_array($result)
$row=mysqli_fetch_array($result);
//mysql_close($con)
mysqli_close($con);
~~~

------
