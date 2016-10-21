---
layout: post
title: 传输文件到集群
date: 2015-09-05 20:50:39
categories: IT
tags: Cluster
---

感觉xmanager的ftp工具对于HPCC不太好用,打算换一个ftp工具. 本来传输时是一卡一卡的,要刷新才能起效,而且速度很慢..后来换了Filzilla以后30多M/s...吓尿了...

顺便归纳以下传输文件到集群的方法.


## 图形界面FTP工具(Windows/OS X/Linux)

下载安装免费开源FTP工具, 如[Filezilla client](http://filezillaproject.org/download.php).
下载安装后,打开后,输入IP地址,用户名,密码即可..十分方便.端口22是sftp,21是ftp.一般22就挺好.例如下图.第一次使用会让你是否记住服务器端主机信息,accept/yes/OK就好了.

![](https://wiki.hpcc.msu.edu/download/attachments/13864442/filezilla_screen1.png?version=1&modificationDate=1314306681000&api=v2)

支持拖拽,右键来指定传输向上/向下传输.左边是本地,右边是服务器端文件系统.不用介绍了..

## 映射网络地址到本地

该方法一般只适合于局域网或者校园内.可以参考[HPCC映射到本地](https://wiki.hpcc.msu.edu/display/hpccdocs/Mapping+HPC+drives+to+a+campus+computer). 好处是可以直接在电脑上复制黏贴.缺点是弄起来复杂一些.


## Dropbox (Windows/OS X/Linux)

使用dropbox你就可以十分简单利用同步盘同步文件了..弄起来复杂点.下载安装请[参见](https://www.dropbox.com/install?os=lnx).在集群上安装需要一些库,先登入节点,再解压, 按说明安装即可.

### scp 远程复制

命令格式就是`scp -r fromFile ToFile`, -r是针对文件夹. 远程端格式是`用户名@主机名或ip:指定位置或文件名`.例如: 

~~~bash
# Upload From local to remote server
scp "My File Name" username@hpcc.msu.edu:"My\ File\ Name"
# Download from remote server to local
scp username@hpcc.msu.edu:example.txt ./example_copy.txt
~~~

### rsync 文件夹同步

和scp相比,没有更新的相同文件不会同步到本地/远端. 基本用法是`rsync -ave 来源文件夹 接收文件夹`.文件夹格式也是 `用户名@主机名或ip:指定位置`. 第一次同步时可加入-n的选项.如: 

~~~bash
# Upload From local to remote server
rsync -ave ssh <local_dir> username@hpcc.msu.edu:<hpcc_dir>
# Download from remote server to local
rsync -ave ssh username@hpcc.msu.edu:<hpcc_dir> <local_dir>
~~~

### sftp 登录后交互传输

和scp相比, 就是先登入远程端, 然后再对指定远程端文件进行子命令操作, 适用于要操作多个文件或复杂目录结构下的文件. 

`sftp username@hpcc.msu.edu` 将登入远程服务器端,然后可以使用部分linux指令,如ls,pwd,cd等进行操作.找到相应文件后再赋值. 同时也可以操作本地端,在指令前加l..如`lcd`本地端改变目录,`lpwd`是查看本地端当前位置,`lls`查看本地端文件.另外,改变权限,重命名,操作文件夹等指令也可以使用. `quit`退出sftp模式.

最关键两个指令: `get filename` 是下载远程文件到本地, `put filename`是上传文件到服务器端. 

### wget 下载远程文件

十分简单, `wget 网上文件url` 即可下载远程文件到本地. `-O filename` 可以指定下载后的文件名, 尤其是一些网名很长的文件..例如:

`wget http://www.examplesite.com/examplefile.txt -O example.txt`

1. [Transferring Files to the HPCC](https://wiki.hpcc.msu.edu/display/hpccdocs/Transferring+Files+to+the+HPCC)

------
