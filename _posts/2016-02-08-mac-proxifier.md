---
layout: post
title: Mac下使用proxifier使用网易云音乐
date: 2016-02-08 02:54:58
categories: IT
tags: Software
---

猴年大家新年快乐!~~ 也祝自己今年也有所进步和归宿~

## Proxifier

这玩意读博时就经常使用, 尤其其全局代理功能很赞. 可以将整台电脑网络使用代理, 或者针对某个程序使用代理. 如果某个程序不提供接口, 有时他就不能使用代理了, 这时Proxifier就能帮你解决! Proxifier 支持HTTP/HTTPS/Socks5/Socks4, 支持验证和多次代理(代理链). 更多可以参考[主页](https://www.proxifier.com/index.htm).

[下载地址](https://www.proxifier.com/download.htm), [Mac版](https://www.proxifier.com/mac/).

Proxifier是收费软件, 售价为40刀. 注册码和绿色版网上一堆...例如[这里](http://bbs.feng.com/read-htm-tid-5594745.html)

<details id="myDetails">P427L-9Y552-5433E-8DSR3-58Z68</details>

至于使用, 参考[CN-proxy:Proxifier教程](http://cn-proxy.com/archives/139) 即可, CN-proxy还可以找到可用较好的国内代理哦~

步骤简单说就是:

1. 开启HTTP代理(否则不显示) **Advanced** -> **HTTP Proxy** -> Enable 就好了
2. 设置一个代理服务器, **Proxies** -> Add -> 选HTTP, 一般不要账号密码 (自己搭的例外) 
3. 添加使用控制规则 (就是指定程序代理, 全局代理): **Rules** -> **Add** -> **Application** 选上需要使用代理的程序 (全局可以是**Any**), Action 选上刚才创建的代理服务器.

Action中, Direct是不适用代理. 默认有两个规则, 一个是localhost即本地跳转, 这个一般不要改. 一个名称Direct 基本上是控制全局, 要全局变更时改这个. 单个程序代理用刚才方法.

重新打开需要代理的程序, 看看Proxifier主窗口下面那个大框框有木有红字, 木有红字报错就是OK了~

如果设置了全局代理, 可以看看[这个网](http://ip138.com)是不是变成国内代理了.

代理获取地址[CN-proxy](http://cn-proxy.com/)

要更多方法翻回国内可以参考[知乎这个贴](https://www.zhihu.com/question/33757121), Iphone一类的可以参考[海外破解网易云音乐和QQ音乐的版权限制](https://www.seavia.com/share/oversea-163-cloud-music-qq-music.html)和[unblockCN](https://www.seavia.com/share/unblockcn-%E4%BD%BF%E7%94%A8%E6%95%99%E7%A8%8B-mac-%E5%AE%89%E5%8D%93-iphone-ipad-pc%E7%89%88-%E4%B8%8B%E8%BD%BD.html)

------
