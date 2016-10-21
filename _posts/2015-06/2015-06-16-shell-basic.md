---
layout: post
title: Shell基础与指令简介
date: 2015-06-16 00:02:31
categories: Coding
tags: Shell Bash
---
这是篇大篇幅的入门教程啊...分几篇来写吧.

## 绝对路径和相对路径
- 绝对路径就是从根目录`/`开始定位起的路径. 可以使用:  
`pwd` 查看和返回当前目录绝对路径.
- 相对路径是相对个别目录为起点的路径,可以认为是利用缩写来简化路径名,如:
  1. `~` 用户目录(一般是/home/username/)
  2. `.` 当前目录
  3. `..` 上一层目录
  4. `-` 上一次所在的目录

## 简单的通配符
常用在对批量文件进行选择,例如`*.txt`表示所有txt文件.

- `*`任意数量任意字符匹配
- `?`匹配一个任意字符
- `[123a],[1-9]`匹配指定几个字符,可用`-`表范围
- `[!123]`匹配除指定字符外任意字符.

## 管道与重定向

- 管道: `|` 在命令后使用管道,可以将管道前的指令的输出作为下一个指令的输入(可以认为以中介临时文件形式)
- 输出重定向:`>` 将前面指令的输出重定向到别的地方,例如本来显示在屏幕的输出到指定文件.
- 输入重定向:`<` 将后面的内容作为输入到前面的指令. 

## 文件/目录相关指令

~~~ bash
cd dirname  #移动到指定文件夹作工作目录
cd ~	#移动到用户目录,
cd ..	#移动到上级目录,../..是上上级目录
cd -	#移动到上次所在的目录

pwd    #查看当前目录绝对路径

ls file/dir #显示文件/目录内容
ls -l    #一般也用ll,显示详细,一般配合-h(文件大小以Mb等形式形式)
ls -a    #显示所有文件

mkdir dir #创建文件夹
rmdir dir #删除文件夹(必须为空)

cp f1 f2        #复制文件f1为f2
cp A B dir      #将A个B复制到目录
cp -r dirA dirB #递归复制目录所有内容

mv f1 f2 移动文件,可以用于改名

rm files   #删除文件,不可逆.
rm -rf dir #递归地删除整个目录,-f是强制进行,不提示

file f1 #判断文件类型
touch f1 #若没有则创建,否则可以更新修改日期.还可以更新更多信息
ln  
~~~

## 文件内容显示和操作相关指令

~~~ bash
echo 
read
tee
wc
cat
nl
head
tail
more
less
split
diff
comm
cmp
sort
cut
paste
join
tr
grep
sed
awk
~~~

## 运行状况相关指令

~~~ bash
top  #交互界面查看任务
ps  #查询进程, 更常用ps -ef查看所有进程
bg  #背景运行
fg  #将背景任务掉到前台
jobs #查看用户任务
kill #终止进程,使用进程id
nohup #在命令前使用,可以使进程在用户退出后依然运行
sleep #暂停几秒
wait #等待所有后台任务结束
time #统计命令任务耗时
crontab
at
~~~

## 用户和配置指令

~~~ bash
chmod
chown
chgrp
id
login
logout
su
whoami
adduser
passwd
chfm
chsh

source
alias
unset
unalias
export

~~~

## 系统管理指令

~~~ bash 
# shutdown: 关机/重启
# shutdown [options][time][message]
# options -r 重启,-h等系统服务停止后再进行,-f 快速关机
# time可以是hh:mm绝对时间,可以是+m多少分钟后,可以是now,message是管理员发给用户的提示.

reboot
chkconfig
service
date
mount
unmount
init
du
df
stat
uname
find
locate  #利用文件目录数据库快速定位,updatedb可以更新文件索引
locale 
where
whereis
which
tar
yum
rpm
apt
uptime
who
last
finger
updatedb
fdisk
~~~

## 网络相关

~~~ bash
ssh
ssh-keygen
scp
sftp
wget url -O output -o out.log #-O 指定下载文件,-o指明输出记录.
ping
ifconfig
curl
netconfig
route
~~~

## 杂项

~~~ bash
exec
expr
test
seq
args
cal
nautilus #RHEL下的文件夹浏览器
clear #清屏
history  #查看命令历史
~~~

Ref:
1. [Linux指令查询](http://man.linuxde.net/)
2. [Linux基础命令教程(豪华版)](http://www.ioesse.com/hqjs/upload/20102421923835325.pdf)



---
