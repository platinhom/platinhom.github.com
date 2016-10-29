---
layout: post
title: proxy代理类型:透明代理 匿名代理 混淆代理和高匿代理
date: 2016-01-20 06:23:41
categories: IT
tags: Internet
---

使用代理可以做很多事, 例如匿名爬虫不被封IP, 获取特殊权限(例如大学代理获取文献), 爬墙等. 代理分几种种类, 常见就是透明,匿名和高匿. 例如[西刺代理](http://www.xicidaili.com/)就提供透明和高匿代理(其实是不是高匿也不知道 ╮(╯▽╰)╭)

这4种代理，主要是在代理服务器端的配置不同，导致其向目标地址发送请求时，`REMOTE_ADDR`， `HTTP_VIA`，`HTTP_X_FORWARDED_FOR`三个变量不同。从安全程度来说, 高匿>混淆>匿名>透明.

## 1.透明代理(Transparent Proxy)

~~~bash
REMOTE_ADDR = Proxy IP
HTTP_VIA = Proxy IP
HTTP_X_FORWARDED_FOR = Your IP
~~~

透明代理虽然可以直接“隐藏”你的IP地址，但是还是可以从`HTTP_X_FORWARDED_FOR`来查到你是谁。

## 2.匿名代理(Anonymous Proxy)

~~~bash
REMOTE_ADDR = proxy IP
HTTP_VIA = proxy IP
HTTP_X_FORWARDED_FOR = proxy IP
~~~

匿名代理比透明代理进步了一点：别人只能知道你用了代理，无法知道你是谁。

还有一种比纯匿名代理更先进一点的：混淆代理，见下节。

## 3.混淆代理(Distorting Proxies)

~~~bash
REMOTE_ADDR = Proxy IP
HTTP_VIA = Proxy IP
HTTP_X_FORWARDED_FOR = Random IP address
~~~

如上，与匿名代理相同，如果使用了混淆代理，别人还是能知道你在用代理，但是会得到一个假的IP地址，伪装的更逼真：-）

## 4.高匿代理(Elite proxy或High Anonymity Proxy)

~~~bash
REMOTE_ADDR = Proxy IP
HTTP_VIA = not determined
HTTP_X_FORWARDED_FOR = not determined
~~~

可以看出来，高匿代理让别人根本无法发现你是在用代理，所以是最好的选择。

----

- 高度匿名代理不改变客户机的请求，这样在服务器看来就像有个真正的客户浏览器在访问它，这时客户的真实IP是隐藏的，服务器端不会认为我们使用了代理。
- 普通匿名代理能隐藏客户机的真实IP，但会改变我们的请求信息，服务器端有可能会认为我们使用了代理。不过使用此种代理时，虽然被访问的网站不能知道你的ip地址，但仍然可以知道你在使用代理，当然某些能够侦测ip的网页仍然可以查到你的ip。
- 透明代理，它不但改变了我们的请求信息，还会传送真实的IP地址。

### 代理的一些参数

- 匿名Level: 上面那几种,很少混淆的.一般是Elite或High Anonymity, Anoymity, Transparent, Not Transparent(非透明的另外2种)
- 类型: HTTP/HTTPS/Socks
- IP: 就是代理的IP罗
- Port: 代理的端口, 很重要! 一般就是 `IP:端口`才是一个代理
- Uptime(L/D): 就是代理的存活比率, L是live活着的次数, D是没响应挂掉的次数. 这个次数是由代理提供者一定时间检测一次的次数.
- Reponse Times: 相应时间, 越短越快. 一般是ms.
- Country/City: 就是代理所在的国家地方

------
