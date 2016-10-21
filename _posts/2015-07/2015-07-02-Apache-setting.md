---
layout: post
title: Apache设置解释
date: 2015-07-01 19:55:02
categories: IT
tags: Website
---

一般地Apache或Apache2 的设置放置在/etc/apache2 里面, apache模块路径：/usr/sbin/apachectl
控制Apache2重启: sudo /etc/init.d/apache2 restart/start/stop

/etc/apache2/conf.d/charset 字符集
/etc/apache2/apache2.conf Apache的主要配置文件,里面一堆include调用别的文件.
/etc/apache2/sites-enabled/ 这里才是放核心配置,像每个虚拟主机的配置. 其实是/etc/apache2/sites-available/里面某些配置文件的链接.

## Reference
1. [Ubuntu-Apache](http://wiki.ubuntu.org.cn/index.php?title=Apache&variant=zh-cn)
2. [Apache虚拟主机指南](http://wiki.ubuntu.org.cn/index.php?title=Apache%E8%99%9A%E6%8B%9F%E4%B8%BB%E6%9C%BA%E6%8C%87%E5%8D%97&variant=zh-cn)
3. [Apache虚拟主机VirtualHost的目录访问权限](http://blog.csdn.net/geekcoder/article/details/8937968)

---
