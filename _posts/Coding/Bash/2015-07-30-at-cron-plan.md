---
layout: post
title: At和Crontab用于计划任务
date: 2015-07-30 03:34:57
categories: Coding
tags: Bash System
---

linux有两个命令用于计划时间执行任务,一个是at,一个是crontab, 用好了就可以人不在都按时提交作业 :)

## at 一次性定时执行

`at(选项)(参数)`

选项:

- 不输入 直接敲命令,ctrl+D完成.
- `-f`：指定包含具体指令的任务文件； 
- -q：指定新任务的队列名称； 
- -l：显示待执行任务的列表； 
- -d：删除指定的待执行任务； 
- -m：任务执行完成后向用户发送E-mail。

参数:  
未来最近符合的时间.例如指定9PM, 那就是即将到来的9PM. 一般格式为`time + count time-units`, 支持的时间包括:  

- 13:00 
- 1:00PM+1 days
- 5:30AM Monday
- now+10 minutes/hours/days/weeks/months/years
- 4:00 tomorrow/today
- midnight/noon/teatime(4pm) DD.MM.YYYY / DD.MM.YY / MM/DD/YYYY /  MM/DD/YY  /  MMDDYYYY or MMDDY

### atq
查询现在还在排队的任务. 第一个是任务编号, 后面是执行时间

### atrm Num
删除排队任务编号Num的.

### at -c Num
查询排队任务(编号Num)的详细,将有以下信息,最下的是任务的命令:  

~~~
#!/bin/sh
# atrun uid=501 gid=20
# mail Hom 0
umask 22
....环境变量,此处省略
cd /Users/Hom/MyGit/platinhom\.github\.com/\_posts || {
	 echo 'Execution directory inaccessible' >&2
	 exit 1
}
OLDPWD=/Users/Hom/MyGit/platinhom.github.com; export OLDPWD
echo hello
~~~

## crontab 计划任务
cron是计划任务,是依靠底层驻留程序**crond**的.at一般进行简单的一次性执行,cron则可以定期进行指定的行为.    
cron把命令行保存在/etc/crontab文件里，每个系统用户如果设置了自己的cron，那都会在/var/spool/cron下面有对应用户名的crontab。  
无论编写/var/spool/cron目录内的文件还是/etc/crontab文件，都能让cron准确无误地执行安排的任务，区别是/var/spool/cron下各系统用户的crontab文件是对应用户级别的的任务配置，而/var/crontab文件则是对应系统级别的任务配置。  
cron服务器每分钟读取一次/var/crontab/cron目录内的所有文件和/etc/crontab文件。

`crontab [-u user] 计划任务列表`

- -u 指定用户, 只有root权限才可以, 否则不需该项就是编辑自己的.
- -e 编辑crontab文件, 格式每行一个任务, 遵循分钟/小时/日/月/星期 命令,其中是空格,支持-,*的通配
- -l 列出crontab文件内容
- -r 删除crontab文件
- 文件名 使用文件名来代替crontab文件
- 不输入 直接敲命令,ctrl+D完成.

`*　　*　　*　　*　　*　　command`  
分　时　日　月　周　命令

- 第1列表示分钟1～59 每分钟用*或者 */1表示  
- 第2列表示小时1～23（0表示0点）  
- 第3列表示日期1～31
- 第4列表示月份1～12
- 第5列标识号星期0～6（0表示星期天）
- 第6列要运行的命令

`*`通配表示每一分钟/小时/日月周等.`*/n`每n时刻. `23-7`23点到7点(范围). `1,3,5` 表示多个指定时间  
当程序在你所指定的时间执行后，系统会寄一封信给你，显示该程序执行的内容，若是你不希望收到这样的信，请在每一行空一格之后加上` > /dev/null 2>&1` 即可

例如:

- `30 21 * * * /usr/local/etc/rc.d/httpd restart`  表示每晚的21:30重启httpd。
- `45 4 1,10,22 * * /usr/local/etc/rc.d/httpd restart` 表示每月1、10、22日的4 : 45重启httpd
- `10 1 * * 6,0 /usr/local/etc/rc.d/httpd restart` 表示每周六、周日的1 : 10重启httpd。
- `0,30 18-23 * * * /usr/local/bin/dosth.sh`  表示在每天18 : 00至23 : 00之间每隔30分钟执行一次dosth脚本。
- `* */2 * * * clean` 每二小时执行一次清屏, 如小时处换为`23-7/1` 表示23到7点间每小时执行一次
- `0 11 * jan mon-wed echo hello` 一月的每周一到周三的11点执行某某某


### crond服务 

- `/sbin/service crond start` 启动服务 
- `/sbin/service crond stop` 关闭服务 
- `/sbin/service crond restart` 重启服务 
- `/sbin/service crond reload` 重新载入配置 
- `service crond status` 查看crontab服务状态
- `ntsysv` 查看crontab服务是否已设置为开机启动  
- `chkconfig –level 35 crond on` 加入开机自动启动 

------
