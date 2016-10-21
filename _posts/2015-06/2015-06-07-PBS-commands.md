---
layout: post
title: PBS集群相关命令
date: 2015-06-06 21:11:11
categories: IT
tags: Shell Cluster
---


每个集群的情况不同, 限制有区别: 主要是walktime(程序跑的时间,相应要等那么久...)  最大处理器数量, 最大Job, memory.   
MSU: 最多1周walktime(168h) 520核 2TB   
[PSU的PBS教程](http://rcc.its.psu.edu/user_guides/system_utilities/pbs/  ).  [MSU的基础教程(PBS详细参数)](https://wiki.hpcc.msu.edu/display/hpccdocs/Scheduling+Jobs ); [MSU 已安装软件 (/opt/software)](https://wiki.hpcc.msu.edu/display/hpccdocs/Installed+Software?src=search  )   
使用X11 图形化登陆服务器: [ICER介绍](https://wiki.hpcc.msu.edu/display/TEAC/iCER+Workshops%3A+Set+Up+Instructions), 简言之, mac安装[Xquartz](http://xquartz.macosforge.org/landing/  )(一般mac可预装); win装 [Moba Xterm](http://mobaxterm.mobatek.net/download-home-edition.html  ); 随后用`ssh -XY id@server`登陆, 打`xeyes`测试是否装有X11 

一篇不错的博文: [PBS,QSUB常用命令](http://xpku.blog.163.com/blog/static/23965002012102954846726/)

##### PBS 脚本示例

~~~ bash
#PBS -l walltime=00:01:00        ##跑的时间
#PBS -l nodes=5:ppn=1            ##使用多少节点以及每个节点多少核
#PBS -l mem=2gb                        ##分配多少内存
#PBS -N name_of_job                ##可以给任务一个名字,方便辨识而已
#PBS -q queuename                ##queuename  可以指定但是需要权限.可以设为main. 建议不设定.
#PBS -j oe                                   ##使得输出和错误都输出到同一个文件.

module load HDF5                ###加载必要的模组
module unload GNU        ###卸载模块
module swap GNU Intel/12.0.0.084        ###切换模块
mpirun -np 8 <exectuable>
~~~

-----------

## qsub

~~~
qsub  [-a  date_time]  [-A account_string] [-b secs] [-c checkpoint_options] [-C directive_prefix] [-d path] [-D path] [-e path] [-f] [-h] [-I] [-j join] [-k
       keep] [-l resource_list] [-m mail_options] [-M user_list] [-n node exclusive] [-N name] [-o path] [-p priority] [-P proxy_username[:group]]  [-q destination]
       [-r  c] [-S path_list] [-t array_request] [-T prologue/epilogue script_name] [-u user_list] [-v variable_list] [-V] [-w] path [-W additional_attributes] [-x]
       [-X] [-z] [script]
~~~

- script : 就是提交作业的脚本了, 如果忽略就从标准输入获取
- `-e`和`-o`: 就是指定记录标准错误和标准输出的文件名.
- `-j`: 合并错误和标准输出. `-j oe`输出到标准输入文件, `eo`是到标准输出.

######### TODO

## module指令: 模块操作
- `module load Name`: 加载模块,一般是Name/Version的形式. 用如OpenMPI可以不区分版本加载默认版本. Name大小写敏感.
- `module unload Name`: 卸载模块
- `module swap mod1 mod2` 将模块mod1换为mod2. 如GNU(GCC系列)和Intel系列
- `module spider name` : 查询模块.
- `module avail name`: 查询模块name的已装有的版本
- `module list`: 显示所有已加载的模块
- `module show name`: 显示某模块的路径编译器信息等内容(相应模块的脚本文件内容).

## 提交和监控任务
- `qsub myjob.qsub`            #提交任务
- `qsub myjob.qsub -v var1,var2=2,var3=3`	#提交任务, 变指定脚本执行时的环境变量.
- `showq -u uid`        #简要显示任务的信息
- `qstat -u uid`    #查用户状况和申请的时间
- `qdel  jobid`  #删除指定任务. `qdel $(qselect -u username)`    可以删除所有某用户的任务. 也可以用`qstat -u username | grep username | cut -d "." -f1 | xargs qdel`
- `qstat -f jobid`  #查询任务详细信息(路径,提交人,位置,申请信息,变量等.
- `showstart jobid`    ##查询任务的可能开始时间/结束时间
- `checkjob jobid`    ##查询任务的信息 (-v 更详尽)


## 常用PBS脚本变量
- `PBS_O_WORKDIR`: 跑任务的路径位置.
- `PBS_O_JOBID`: 任务的ID
- `PBS_O_QUEUE`,`PBS_O_SERVER`,`PBS_O_HOST`: 跑任务的列队(如main), 服务器(如mgr-04), 主机(如intel14.i)
- `PBS_O_LOGNAME`, `PBS_O_HOME`: 跑任务的用户名及其HOME位置.
- `PBS_O_PATH`, `PBS_O_SHELL`:跑任务时的环境变量以及使用的shell.
- `PBS_NUM_PPN`: 使用核数

---