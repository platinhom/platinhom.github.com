---
layout: post
title: PHP服务器端不显示错误报告的重启解决办法
date: 2015-07-03 21:27:27
categories: Coding
tags: PHP
---

近日不停使用php,在localhost能够显示出第几行出错,经常都是少句末的;啊,少括号啊,拼写错误等等.

但是呢,在服务器端, 只有令人郁闷的一片空白...根本不显示报错...好吧,肯定是报错服务关闭了.记一记怎么更改设置并重启服务吧.

------

随便新建个hi.php, 使用`phpinfo()`来显示PHP的配置

搜索 `Loaded Configuration File` 获得`php.ini` 的位置

修改该配置文件, 找 `display_errors` 一项, 把其改为On.(`display_error On`,取消的话改成注释(前面加;). 将上面一项`error_reporting`改成这样子`error_reporting = E_ALL & ~E_NOTICE`. 注意有些人可能在该文件中有多个设置地方, 多找找..我修改的地方就有两处,前面一处是注释掉的..后面才是没有注释起效的,估计那家伙复制黏贴了再改..

然后`servive apache2 reload` 重新加载apache2配置来生效.

如果运行底层的是httpd而不是apache2来监控,那么可能是 `servive httpd reload`

网上还有种说法是是和php-fpm相关, 使用 /etc/init.d/php-fpm reload重新加载(或者直接php-fpm运行默认的), 也可能是php5-fpm. 但我这里根本没有安装这个服务..

---
