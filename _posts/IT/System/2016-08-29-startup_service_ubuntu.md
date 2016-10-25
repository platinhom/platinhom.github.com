---
layout: post
title: Ubuntu开机服务
date: 2016-08-29 14:51:04
categories: IT
tags: System Ubuntu
---

如果只是想开机时执行一些命令在背景运行, 而不是用到复杂的开机服务(例如可以暂停重启什么功能的), 可以这么做:

1. 编辑`/etc/rc.local`, 在 *exit 0* 前面加入你要执行的命令,脚本. 注意, 这个是很早的执行阶段, 可能`PATH`没有设置好, 所以最好用绝对路径!!!再说一次, 绝对路径! 包括脚本内!
2. `sudo crontab -e` 进入计划事务编辑模式, 编辑计划, 加入这么一句`@reboot /path/to/script`. 这个可以加载比较多的指令了, 如果没有正常运行, 请用绝对路径.
3. 如果要执行的命令没有背景运行模式, 可以用`nohup command > /dev/null 2>&1 &`

----------------

一般的开机服务是定义在`/etc/init.d`里的东东, 图形管理界面可以使用`sysv-rc-conf`, 命令行可以使用`service`命令.

~~~bash
sudo apt install sysv-rc-conf
sudo sysv-rc-conf
~~~

![](/blogpic/sysv-rc-conf.png)

- 这里面service是不同级别的runlevel处理方法, `[X]`就是开启, 否则是没有开启, 按空格键切换 
- 要马上操作服务: 按`+`开启,`-`停止服务
- `q`退出

其实, 这些服务的真实脚本放在`/etc/init.d`里, 其实是一些可执行的bash脚本. 相应脚本其实是`service` 运行的. 而开机运行的内容放在`/etc/rc*`内. 有些系统有`/etc/rc/`文件夹专门放置, 在ubuntu16里面都放在`/etc/`内. 在`/etc/rc*`的一般是放/etc/init.d内文件的链接文件.

在开机启动内容文件夹内一般有`rc*.d`和`rc.local`,一般定义一句话开机启动的就定义在rc.local好了, 这个是最后必定加载的文件.

而`rc*.d`则对应不同开机级数作相应运行, 文件名开头`S`的表示该服务会加载,`K`代表该服务不加载: 

- rc0.d: 关机级别 -> `shutdown` 命令
- rc1.d: 单用户, 不带网络, 不执行daemon背景程序, 不允许非root登陆
- rc2.d: 多用户, 不带网络, 不执行daemon背景程序的级别
- rc3.d: 多用户, 带网络的级别(正常级别)
- rc4.d: 用户自定义
- rc5.d: 多用户带图形界面(一般情况)
- rc6.d: 重启级别 -> `reboot` 命令
- rcS.d: 在`rc?.d`之前运行

> PS: `runlevel` 命令可以知道当前级别.
> PS: 总的加载顺序是: 开机init -> rcS.d -> rc0~6.d -> rc.local
> PS: 即使有个服务存在/etc/init.d 但要是没有rc的运行级别来运行, 依然是运行不起来的~
> PS: `sudo init N` 就是切换当前操作系统的Runlevel的命令 一般用init 3和init 5

所以sysv-rc-conf 是个十分强大方便管理这个加载情况的软件~


用命令行来设置运行级别的服务可以使用`update-rc.d`命令, 不同系统该指令有差异. 在ubuntu16有以下参数(有些版本可以使用start/stop:

~~~bash
# Set service at 2,3,4,5 Level
update-rc.d servicename default
# Cancel service at 2,3,4,5 Level
update-rc.d servicename remove
# Cancel service at 2,3,4,5 Level, and delete the symlinks even it exists in /etc/init.d
update-rc.d -f servicename remove
# Set service at giving Level
update-rc.d servicename enable  [S|2|3|4|5]
# Cancel service at giving Level
update-rc.d servicename disable  [S|2|3|4|5]
~~~

## service命令

再就是一个很基础的命令: `service`

这个命令主要用途是一次性操作服务 (相当于sysv-rc-conf的`+-`号).

~~~bash
service < option > | --status-all | [ service_name [ command | --full-restart ] ]
## 查看所有服务当前的状态
service --status-all
## 开启/重启服务
service mysql start/restart
## 停止服务 
service mysql stop
~~~

如果服务脚本中还有以下函数定义的还可以执行install/uninstall操作(其实也是操作rc链接):

~~~bash
installD() {
....
}

uninstallD() {
...
}

case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  status)
  .....;;
  restart)
    stop
    start
    ;;
  install)
    installD
    ;;  
  uninstall)
    uninstallD
    ;;
  *)
    echo "Usage: $prog {start|stop|restart|status}"
    exit 1
esac
~~~

另外, 在应用窗口搜索 *startup* 找到`Startup Applications`, 可以图形化管理添加一些开机启动程序, 很方便. 参考[](http://www.howtogeek.com/189995/how-to-manage-startup-applications-in-ubuntu-14.04/)

## Reference

1. [Ubuntu下使用sysv-rc-conf管理服务 ](http://blog.csdn.net/gatieme/article/details/45251389): 作者很好地介绍了相关使用, 并且附有各种常见服务的解释哦!
2. [Linux服务的开机启动和运行级别](http://hlee.iteye.com/blog/530877):主要介绍`chkconfig`的使用, 一些linux系统如RHEL, Debian配有这个命令

------
