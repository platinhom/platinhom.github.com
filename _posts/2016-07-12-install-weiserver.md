---
layout: post
title: 在新的ubuntu虚拟服务器建立服务器
date: 2016-07-12 14:46:56
categories: IT
tags: Ubuntu System
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
## openmp and MPI for amber
sudo apt-get install openmpi-bin
sudo apt-get install openmpi-bin libopenmpi-dev 

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
# Update many patch
./update_amber --update
# it will install many softwares!
./configure gnu
# It should be load!
source /home/user/Software/Amber16/amber.sh
make install
# To install MPI and openmp version, do following one more time
./configure -mpi -openmp gnu
source /home/user/Software/Amber16/amber.sh
make install
~~~

如要安装CUDA:

~~~bash
### If you don't install nvidia driver, use following two commands
#sudo apt-get purge nvidia*
#reboot

### If you don't want to install nvidia-toolkit in official way:
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get install nvidia-367 nvidia-367-dev  
sudo apt-get install libcuda1-367 nvidia-cuda-dev nvidia-cuda-toolkit
~~~

以上方法能帮你安装好cuda. 但是cuda的执行文件在`/usr/bin/`,库文件很零散,如果有程序需要`CUDA_HOME`变量实在不知道怎么指定比较合理,而且要想安装多个CUDA-toolkit就比较烦了. 

最后推荐用官方更规范的方法安装, 在笔者尝试中在[官方下载](https://developer.nvidia.com/cuda-toolkit)只提供CUDA7.5 的14.04和15.04的deb包, 不过有提供run包(两个ubuntu版本是一样的!).这里就参考这篇文章[NVIDIA CUDA with Ubuntu 16.04 beta on a laptop (if you just cannot wait)](https://www.pugetsystems.com/labs/hpc/NVIDIA-CUDA-with-Ubuntu-16-04-beta-on-a-laptop-if-you-just-cannot-wait-775/)来安装:

~~~bash
wget http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local_installers/cuda_7.5.18_linux.run
# To install cuda. Notice that "DON'T" install the NVIDIA driver in the run file! Setup see the following block
sudo ./cuda_7.5.18_linux.run --override
~~~

可能出现下面的画面(这里我缺了个库,`ln -s /usr/lib/x86_64-linux-gnu/libGLU.so.1 /usr/lib/x86_64-linux-gnu/libGLU.so`搞掂):

~~~
Do you accept the previously read EULA? (accept/decline/quit): accept    
You are attempting to install on an unsupported configuration. Do you wish to continue? ((y)es/(n)o) [ default is no ]: y
Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 352.39? ((y)es/(n)o/(q)uit): n
Install the CUDA 7.5 Toolkit? ((y)es/(n)o/(q)uit): y
Enter Toolkit Location [ default is /usr/local/cuda-7.5 ]: 
Do you want to install a symbolic link at /usr/local/cuda? ((y)es/(n)o/(q)uit): y
Install the CUDA 7.5 Samples? ((y)es/(n)o/(q)uit): y
Enter CUDA Samples Location [ default is /home/hom ]: /usr/local/cuda-7.5
Error: unsupported compiler: 5.4.0. Use --override to override this check.
Missing recommended library: libGLU.so

Error: cannot find Toolkit in /usr/local/cuda-7.5
~~~

如果有对应Ubuntu版本的deb包, 安装则是:

~~~bash
# If exist deb package...
sudo dpkg -i cuda-repo-<distro>_<version>_<architecture>.deb
sudo apt-get update
sudo apt-get install cuda
~~~

如果安装成功, 就进行CUDA配置. 在.bashrc或者.profile里面加入:

~~~bash
export CUDA_HOME="/usr/local/cuda" 
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/lib:$LD_LIBRARY_PATH
~~~

测试是否安装好:

~~~bash
# Just to test whether CUDA is OK
nvcc -V
cd /usr/local/cuda/samples
sudo chown -R <username>:<usergroup> .
cd 1_Utilities/deviceQuery
make
./deviceQuery
~~~

------------------

`source .bashrc`加载一下后, 就可以安装CUDA版本了!

~~~bash
./configure -mpi -openmp -cuda gnu
source /home/user/Software/Amber16/amber.sh
make install
~~~

可能会遇到以下错误:

~~~
In file included from /usr/local/cuda/include/cuda_runtime.h:76:0,
                 from <command-line>:0:
/usr/local/cuda/include/host_config.h:115:2: error: #error -- unsupported GNU version! gcc versions later than 4.9 are not supported!
 #error -- unsupported GNU version! gcc versions later than 4.9 are not supported!
~~~

因为CUDA这里限定了编译器不能高于4.9. 我们实际ubuntu16就已经超过5.4了. 为此, 要修改一个文件:

~~~bash
sudo cd /usr/local/cuda/include/ #进入到头文件目录cuda；
sudo cp host_config.h host_config.h.bak #备份原头文件；
sudo gedit host_config.h #编辑头文件；
# ctrl+F查找4.9出现的地方，大约位于115行，在第113行处应该显示if _GNUC_>4 || (_GNUC_ == 4 && _GNUC_MINOR_ > 9)，因为我们的是5.4，因此，把上面的2个4都改成5就ok了，保存退出。
~~~

随后`make clear; make install`再来一遍

~~~
mpicc -Duse_SPFP -O3 -mtune=native -DMPICH_IGNORE_CXX_SEEK -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -DBINTRAJ -DMPI   -DCUDA -DMPI -DMPICH_IGNORE_CXX_SEEK -I/usr/local/cuda/include -IB40C -I/usr/lib/openmpi/include/openmpi/opal/mca/event/libevent2021/libevent -I/usr/lib/openmpi/include/openmpi/opal/mca/event/libevent2021/libevent/include -I/usr/lib/openmpi/include -I/usr/lib/openmpi/include/openmpi  -c gputypes.cpp
/usr/local/cuda/bin/nvcc -gencode arch=compute_20,code=sm_20 -gencode arch=compute_30,code=sm_30 -gencode arch=compute_50,code=sm_50 -gencode arch=compute_52,code=sm_52 -gencode arch=compute_53,code=sm_53 -use_fast_math -O3  -Duse_SPFP -DCUDA -DMPI -DMPICH_IGNORE_CXX_SEEK -I/usr/local/cuda/include -IB40C -I/usr/lib/openmpi/include/openmpi/opal/mca/event/libevent2021/libevent -I/usr/lib/openmpi/include/openmpi/opal/mca/event/libevent2021/libevent/include -I/usr/lib/openmpi/include -I/usr/lib/openmpi/include/openmpi   -c kForcesUpdate.cu
/usr/include/string.h: In function ‘void* __mempcpy_inline(void*, const void*, size_t)’:
/usr/include/string.h:652:42: error: ‘memcpy’ was not declared in this scope
   return (char *) memcpy (__dest, __src, __n) + __n;
                                          ^
Makefile:38: recipe for target 'kForcesUpdate.o' failed
~~~

遇到这个问题, 我修改了`config.h`里面`PMEMD_CU_DEFINES=-DCUDA -DMPI -DMPICH_IGNORE_CXX_SEEK -D_FORCE_INLINES`, 加入了后面的`-D_FORCE_INLINES`. 编译成功! (参考自[`memcpy' was not declared in this scope (Ubuntu 16.04) ](https://github.com/opencv/opencv/issues/6500)). 在安装GROMACS时在CMakelists.txt加入`set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -D_FORCE_INLINES")`.

Ref: 

1. [CUDA Toolkit Documentation](http://docs.nvidia.com/cuda/cuda-samples/index.html)
2. [Ubuntu 16.04下安装Tensorflow(GPU)](http://www.linuxdiyf.com/linux/22230.html)
3. [testing Ubuntu 16.04 for CUDA development. Awesome integration!](https://devtalk.nvidia.com/default/topic/926383/testing-ubuntu-16-04-for-cuda-development-awesome-integration-/)
4. [NVIDIA CUDA with Ubuntu 16.04 beta on a laptop (if you just cannot wait)](https://www.pugetsystems.com/labs/hpc/NVIDIA-CUDA-with-Ubuntu-16-04-beta-on-a-laptop-if-you-just-cannot-wait-775/)
5. [Ubuntu 14.04 安装配置CUDA](http://www.linuxidc.com/Linux/2014-10/107501.htm), [CUDA入门教程](http://www.linuxidc.com/Linux/2014-07/104328.htm)
6. [Amber11+AmberTools1.5+CUDA加速 安装总结](http://www.linuxidc.com/Linux/2015-07/120485.htm)
7. [Ubuntu15.10_64位安装Theano+cuda7.5详细笔记 ](http://blog.csdn.net/niuwei22007/article/details/50439478): 很好的一篇从头装theano的
8. [ubuntu 16.04 编译opencv3.1，opencv多版本切换 ](http://blog.csdn.net/Swearos/article/details/51307304)

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
