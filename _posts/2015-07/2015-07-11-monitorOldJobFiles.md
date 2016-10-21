---
layout: post
title: 后台监控删除老结果
date: 2015-07-10 16:30:28
categories: Coding
tags: Bash
---

- 这个脚本是删除旧任务的.当任务已经完成超过7天, 就自动被删除. 每小时运行一次检测.  
- 关键原理是用`stat -c %Y` 来获取文件目录生成时间的绝对秒数,扣除`date +%s`当前时间的绝对秒数.  
- 因为要一直后台监测, 所以要用while循环一直循环, 命令用`nohup command &` 来运行.
	- 不使用nohup, 即使用`&`将任务放到后台,当任务执行者退出时任务也会被关闭, 并不能正常工作.
	- 当用户退出shell的时候，bash会发送hangup(hup)信号给该用户该shell的所有子进程。bash的后台任务也都被kill了。
	- nohup命令会使得子进程忽略hang-up信号。但仍然可以通过kill来杀掉某个进程，kill是发送SIGTERM而不是hangup信号。
	- Nohup的提示消息是告诉你把任务的输出重定向到了当前目录的nohup.out中. 也可以重定向到指定文件.
- 中间有个判断是否没有任何文件夹的,否则每一小时在nohup.out写一个错误信息.

~~~bash
#! /bin/bash
# file: deleteOldJob.sh
# Author: Zhixiong Zhao, 2015.7.10
# 
# Monitor the job number and generated old directories.
# Use as : nohup ./deleteOldJob.sh &
 
#work directory
cd /home/labsite/MIBPBweb/MIBPBRun
 
while true
do
 
nowtime=`date +%s`
# avoid nothing in directory
dirnum=`ls mibpb* | wc -l`
if [ $dirnum -gt 0 ];then

# job name mibpb*****, find them all
for dir in mibpb*
do
filetime=`stat -c %Y $dir`
delta=`expr $nowtime - $filetime`
# 7day=604800second, after 7 day, job will be deleted.
if [ $delta -gt 6048000 ];then
# delete it! Be careful! 
rm -rf $dir
# Save to nohup.out
echo "$dir :time $delta seconds." 
fi
done

fi
 
sleep 3600
done #while
 
cd -
~~~

------
