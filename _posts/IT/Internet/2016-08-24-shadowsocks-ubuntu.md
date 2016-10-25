---
layout: post
title: Ubuntu下利用ssh和shadowsocks番蔷
date: 2016-08-23 17:21:28
categories: IT
tags: Internet Software System Server Ubuntu Proxy
---

对于范强, 有好几种选择: 买收费VPN, 买收费SS代理, 自己搭建海外VPS(VPN,SS), SSH隧道登陆,HTTP/1.0代理服务器等. 买账号就不提罗. 对于自己搭建VPN,SS都需要你具有自己的VPS海外主机, SSH隧道则可以不用~

## HTTP代理服务器

就是平时最常见的简单的代理. 搭建可以使用Squid. [Squid](http://www.squid-cache.org/)可用于HTTP，HTTPS，FTP等网站的缓存代理服务器。它能通过缓存和重用那些经常被访问的网页l来降低带宽，改善反应速度。Squid有很强的访问控制，是一个出色的服务器加速器。这里简单介绍了如何架设一台透明Squid代理服务器。

~~~bash
## 安装squid和squid-common
sudo aptitude install squid squid-common

## 编辑squid配置文件
sudo vi /etc/squid/squid.conf
##### 设置允许的网站
acl internal_network src 192.168.1.0/24
http_access allow internal_network
##### 上面的192.168.1.0/24是指你的IP范围。

## 设置正确的权限
sudo chown -R proxy:proxy /var/log/squid/
sudo chown proxy:proxy /etc/squid/squid.conf

## 需要重启生效
sudo /etc/init.d/squid restart
~~~

现在打开网页浏览器，设置代理服务器为新的squid服务器，端口为3128试试.

[Squid透明代理(Transparent Proxy)](http://www.linuxidc.com/Linux/2014-03/97511.htm), [百度经验:Squid代理服务器的安装与配置](http://jingyan.baidu.com/article/19192ad815430ee53e5707a7.html)

## SSH隧道登陆

这应该是较简单的方法之一, 要求就是你可以ssh登陆到一个海外的服务器, 这个服务器能打开海外网站~ 简单介绍看[SSH隧道翻墙的原理和实现](https://segmentfault.com/a/1190000003939615)吧. 这玩意又叫 SOCKS/HTTP Proxy Forwarding. 其实就是很简单, 就是SSH登陆时增加`-D 端口号`将本地访问互联网的请求通过该端口转到SSH服务器, 然后再接收回来. 就那么简单.

~~~bash
# 一般执行下面的就行
ssh -N -D 7070 username@ip_address
# 转发远程主机的指定端口到本地端口<local port>
ssh -L <local port>:<remote host>:<remote port> username@ip_address
~~~

- -N : 不执行远程命令,就是不进去交互命令, 只是连接. 尤其在forwarding ports 时就可以用.
- -D : 绑定端口,默认是本机的端口.

- [IBM-实战 SSH 端口转发](http://www.ibm.com/developerworks/cn/linux/l-cn-sshforward/) : 很复杂的关于端口转发的技术文章, 值得一读!
- [SSH代理设置教程（Google Chrome版）](http://terrancesiu.com/post/546.html): 这是个图文并茂的教程从chrome安装switchy开始, 到利用[Tunnelier](https://www.bitvise.com/tunnelier)来构建SSH隧道提供端口. 值得看看吧. 类似于Tunnelier的还有[MyEnTunnel](http://nemesis2.qx.net/pages/MyEnTunnel). 类似地, [SSH代理服务器使用教程](http://u.fishnote.net/) 也介绍了上述两种window ssh软件和mac里面iSSH的使用. 大同小异.
- [Openwrt配置ssh自动登录服务器socks5转发](http://www.haiyun.me/archives/openwrt-ssh-socks5.html) : 在Openwrt设置路由器转发时的教程,用到了`-L`选项转发.

##### 附: 创建给人用的账户(sudo免去):

~~~bash
## 创建用户组internetfreedom
groupadd internetfreedom
## 添加用户freenutsdotcom并设置用户组
useradd -d /home/freenutsdotcom -m -g internetfreedom -s /bin/false freenutsdotcom
## 更改用户密码
passwd freenutsdotcom
~~~

## ShadowSocks 代理登陆 (SS代理)

[shadowsocks](https://shadowsocks.org/en/index.html)是一种基于python的轻量级**SOCKS 5**代理软件, 由大神[@clowwindy](https://twitter.com/clowwindy)开发(另外ChinaDNS也是其开发), 其代码开源在[Github](https://github.com/shadowsocks/shadowsocks/tree/master). SSH虽然简单, 但是手机就不好使了, 另外也容易断线, 而VPN的全局代理有时实在太麻烦了.. shadowsocks使用简易且适用于Win, Mac, Linux, Android, iOS等[多平台](https://shadowsocks.org/en/download/clients.html). 

~~~bash
sudo pip install --upgrade pip
## Install shadowsocks
sudo pip install shadowsocks
## 安装m2crypto 来进行传输加密(对于aes-256-cfb 必须)
sudo apt-get install m2crypto  swig  python-m2crypto

#### 下面的不推荐, 因为会被默认加载,如果只有一个代理那可以这么做.
## Check its location
sudo find / -name shadows*
## Add automatical run config file for it 
sudo vi /usr/local/lib/python2.7/dist-packages/shadowsocks/config.json

nohup ssserver -c /usr/local/lib/python2.7/dist-packages/shadowsocks/config.json > ss.log &
ps -ef | grep ssserver
#kill sss_pid

## To startup when reboot
sudo vim /etc/rc.local
## Add this line:
#> /usr/local/bin/ssserver -c /usr/local/lib/python2.7/dist-packages/shadowsocks/config.json
## If use firewall, add the following to /etc/sysconfig/iptables. The port is that to be release
#>-A INPUT -m state --state NEW -m tcp -p tcp --dport 8388 -j ACCEPT
#sudo service iptables restart
~~~

一键安装版可以使用[shadowsocks_install](https://github.com/teddysun/shadowsocks_install). `git clone https://github.com/teddysun/shadowsocks_install.git`到本地, 运行相应的脚本就可以了~卸载就是`./shadowsocks.sh uninstall`, 配置文件在/etc/shadowsocks.json. 更多参看[Shadowsocks Python版一键安装脚本](https://teddysun.com/342.html). 还可以使用别的例如libdev版本

~~~bash
sudo pip install shadowsocks
###  Error 1
#Traceback (most recent call last):
#  File "/usr/bin/pip", line 11, in <module>
#    sys.exit(main())
# T File "/usr/lib/python2.7/dist-packages/pip/__init__.py", line 215, in main
#    locale.setlocale(locale.LC_ALL, '')
#  File "/usr/lib/python2.7/locale.py", line 581, in setlocaleps -ef | g
#    return _setlocale(category, locale)
#locale.Error: unsupported locale setting

locale
### Error 2
## locale: Cannot set LC_ALL to default locale: No such file or directory

## Solution: 
export LC_CTYPE="en_US.UTF-8" >> ~/.bahsrc
~~~

安装后会在*/usr/bin*加入两个程序: **sslocal**是客户端程序；**ssserver**是服务端程序。

~~~
ssserver -h
usage: ssserver [OPTION]...
A fast tunnel proxy that helps you bypass firewalls.

You can supply configurations via either config file or command line arguments.

Proxy options:
  -c CONFIG              path to config file
  -s SERVER_ADDR         server address, default: 0.0.0.0
  -p SERVER_PORT         server port, default: 8388
  -k PASSWORD            password
  -m METHOD              encryption method, default: aes-256-cfb
  -t TIMEOUT             timeout in seconds, default: 300
  --fast-open            use TCP_FASTOPEN, requires Linux 3.7+
  --workers WORKERS      number of workers, available on Unix/Linux
  --forbidden-ip IPLIST  comma seperated IP list forbidden to connect
  --manager-address ADDR optional server manager UDP address, see wiki

General options:
  -h, --help             show this help message and exit
  -d start/stop/restart  daemon mode 背景守护进程模式.
  --pid-file PID_FILE    pid file for daemon mode
  --log-file LOG_FILE    log file for daemon mode
  --user USER            username to run as (一般用nobody)
  -v, -vv                verbose mode
  -q, -qq                quiet mode, only show warnings/errors
  --version              show version information

Online help: <https://github.com/shadowsocks/shadowsocks>
--------------------------------------------------------------------
sslocal -h
usage: sslocal [OPTION]...
A fast tunnel proxy that helps you bypass firewalls.

You can supply configurations via either config file or command line arguments.

Proxy options:
  -c CONFIG              path to config file
  -s SERVER_ADDR         server address
  -p SERVER_PORT         server port, default: 8388
  -b LOCAL_ADDR          local binding address, default: 127.0.0.1
  -l LOCAL_PORT          local port, default: 1080
  -k PASSWORD            password
  -m METHOD              encryption method, default: aes-256-cfb
  -t TIMEOUT             timeout in seconds, default: 300
  --fast-open            use TCP_FASTOPEN, requires Linux 3.7+

General options:
  -h, --help             show this help message and exit
  -d start/stop/restart  daemon mode
  --pid-file PID_FILE    pid file for daemon mode
  --log-file LOG_FILE    log file for daemon mode
  --user USER            username to run as
  -v, -vv                verbose mode
  -q, -qq                quiet mode, only show warnings/errors
  --version              show version information

Online help: <https://github.com/shadowsocks/shadowsocks>
~~~

一般的配置文件格式是json,如下:

~~~json
{
    "server":"0.0.0.0",
    "server_port":8989,
    "local_address":"127.0.0.1",
    "local_port":1080,
    "password":"yourpassword",
    "timeout":600,
    "method":"aes-256-cfb",
    "fast_open": false
}
~~~

各字段的含义：

- server：服务器 IP (IPv4/IPv6)，注意这也将是客户端监听的IP地址. 注意: 本机运行时设置为 `0.0.0.0` 而不是localhost或者127.0.0.1
- server_port：监听的服务器端口(服务器端输出客户端的输入). 十分注意该端口是否可用! 默认例如8838, 443.
- local_address：本地监听的IP地址. 就是给别的程序代理的IP,一般是localhost或者127.0.0.1
- local_port：本地端端口.一般是1080. 和上面本地端口构成给浏览器等关键的代理参数.
- password：用来加密的密码
- timeout：超时时间（秒）
- method：加密方法，可选择 “bf-cfb”, “aes-256-cfb”, “des-cfb”, “rc4”, 等等。默认是一种不安全的加密table，推荐用 “aes-256-cfb”(需要额外库)或者“bf-cfb”
- fast\_open：true 或 false。如果你的服务器 Linux 内核在3.7+，可以开启 fast\_open 以降低延迟。临时开启方法：`echo 3 > /proc/sys/net/ipv4/tcp_fastopen` (不一定成功).

如果是提供给多人使用,每人用不同的端口,设置不同的密码即可:

~~~json
{
    "server":"0.0.0.0",
    "local_address":"127.0.0.1",
    "local_port":1080,
    "port_password":{
         "8989":"password0",
         "9001":"password1",
         "9002":"password2",
         "9003":"password3",
         "9004":"password4"
    },
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": false
}
~~~

下面的才是更有意义的

~~~bash
## 直接简单开启服务
ssserver -p 443 -k password -m aes-256-cfb
## 使用配置文件在背景开启服务
sudo ssserver -c myconf.json --user nobody -d start
## 停止背景运行的服务
sudo ssserver -d stop
## 查看日子
sudo less /var/log/shadowsocks.log
## 命令行运行ss客户端
sslocal -s 99.99.99.99 -p 8388 -b 127.0.0.1 -l 1080 -k password -m aes-256-cfb -t 600
sslocal -c myconf.json --user nobody -d start
## 通过下面简化命令
alias sss_go="sudo sslocal -c myconf.json -d start"
alias sss_stop="sudo sslocal -c myconf.json -d stop"
~~~

- Win版简易教程:[百度经验-Shadowsocks使用](http://jingyan.baidu.com/article/f3e34a12adf3cff5eb6535e2.html)
- 这篇老高的有教用libdev的(应该更快): [使用shadowsocks轻松搭建翻墙环境教程](https://blog.phpgao.com/shadowsocks_on_linux.html)
- 优化shadowsocks: [Optimizing Shadowsocks](https://github.com/shadowsocks/shadowsocks/wiki/Optimizing-Shadowsocks). 注意关于使用FAST OPEN可以加速, 但是需要服务器端和客户端都要开, 而且Linux内核
- 了解更多参看[shadowsocks wiki](https://github.com/shadowsocks/shadowsocks/wiki)

### Client 客户端

简书的这篇[ShadowSocks—科学上网之瑞士军刀](http://www.jianshu.com/p/08ba65d1f91a)有介绍各个平台的客户端, 算比较新, 可以看看.

##### Linux下首选: [shadowsocks-qt5](https://github.com/shadowsocks/shadowsocks-qt5/wiki/%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C)客户端. 

安装需要加个ppa再apt-get:

~~~bash
sudo add-apt-repository ppa:hzwhuang/ss-qt5
sudo apt-get update
sudo apt-get install shadowsocks-qt5
sudo ss-qt5
~~~

很简单的配置使用. 但注意哦, 要是发现编辑完下一次打开没反应, 请用`sudo ss-qt5` 来打开运行!~设置好后退出(可能会有不停弹窗提示, 要用`ps -ef | grep notify-osd` 找到这个程序再`sudo kill pid`杀掉)

##### Android客户端: [shadowsocks-android](https://github.com/shadowsocks/shadowsocks-android/releases) 

中文名字叫影梭. 只要能上github就能下载 不用通过google play! 下载个新版本自己摸索吧~没啥好说的, 就是那个选择端口很蛋疼..

- [openwrt-shadowsocks](https://github.com/shadowsocks/openwrt-shadowsocks): 用着openwrt写到路由器的客户端. 因为没有这种路由器, 忽略之.
- [shadowsocks-gui](https://sourceforge.net/projects/shadowsocksgui/): 主要是一些window版本, 也有linux版. 已经停止更新很久, 不建议使用.

更多[客户端](https://github.com/shadowsocks/shadowsocks/wiki/Ports-and-Clients)参考.

### 浏览器

浏览器是科学上网的直接大门. 设置一般可以用浏览器内部设置(直接设置或者使用PAC), 系统全局代理或者用工具切换.

- 关于PAC: 就是定义了上网网址代理处理方式的文件 (就是怎么处理代理的文件啦). 一般包括**使用代理的方法**(http?socks?ip?端口?)和**网址处理方法**(例如处理gfwlist). 不设置网址处理方法就是所有网址通通使用该代理. 
- genpac: 生产PAC文件可以利用[genpac](https://github.com/JinnLynn/GenPAC)生成基于**gfwlist**的代理自动配置文件,再在浏览器里自动代理的URL填写PAC文件即可 (或者在自动切换代理软件使用也可). 利用genpac-火狐搭建SS自动代理的例子: [ubuntu 14安装shadowsocks-qt5并配置pac全局代理](http://www.linuxdiyf.com/linux/23564.html). 注意gfwlist的地址是[github](https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt)的, 不是[googlecode svn](https://autoproxy-gfwlist.googlecode.com/svn/trunk/gfwlist.txt)的那个.

~~~bash
# 安装
sudo pip install genpac
# 更新
sudo pip install --upgrade genpac
# 卸载
sudo pip uninstall genpac
# 查看帮助和各个选项
genpac -h
# 如果可以连通gfwlist, 使用这个最简单生成PAC. 产生一个output指定的pac文件. -p指定是必须的
genpac -p "SOCKS5 127.0.0.1:1080" --output="~/autoproxy.pac"
# 使用代理端口来获取gfwlist来生成pac, 防止上面的方法拿不到gfwlist
genpac -p "SOCKS5 127.0.0.1:1080" --gfwlist-proxy="SOCKS5 127.0.0.1:1080" --output="~/autoproxy.pac"
# 如果有非官方的获取gfwlist链接地址, 可以自己指定
genpac -p "SOCKS5 127.0.0.1:1080" --gfwlist-url="gfwlist url" --output="~/autoproxy.pac"
# 如果不能在线获得而有本地gfwlist文件, 则自己指定
genpac -p "SOCKS5 127.0.0.1:1080" --gfwlist-local=gfwlist.txt --output="~/autoproxy.pac"
# 不使用gfwlist 而是全部都代理
genpac -p "SOCKS5 127.0.0.1:1080" --gfwlist-disabled --output="~/autoproxy.pac"
~~~

#### 直接设置

一般的设置就不用我说了吧...区分好http, socks 4/5就好了. 在火狐那些浏览器, 可以设置利用PAC来设置自动代理, 也可以使用系统全局代理. 这个不好玩, 还是玩下面的插件吧~!

#### AutoProxy/FoxyProxy（用于Firefox）

Autoproxy是著名的火狐插件, 用于切换代理. 但经使用有些bug, 例如不能真正切换, 需要重启火狐才起效..因为autoproxy很久没有更新了, 作者也删库了. 替换品是Foxyproxy, 类似于Chrome的proxyswitchy. 可以支持使用gfwlist.

1. 在火狐 Get Add-ons里面 进去后赵更多插件, 然后搜索foxyproxy, 安装foxyproxy standard即可.
2. 安装后在地址栏左边出现一只小狐狸. 深蓝色(Default)和红色代表无代理, **橙色**代表自动根据网址进行代理,可以自行再定义.
3. 点选后进去options设置, 在第一tab的proxies设置添加新代理方式. 
4. general页面可以设置颜色和代理名字. proxy details就是代理方式, 可以自行设置代理(例如SS使用SOCKS5)还可以设定密码啥的.还可以使用WPAD或者PAC来定义. URL pattern可以不理
5. 到Pattern Subscriptions的tab设置**自动代理**的方法. 新添一个(点GO)然后起个名字, subscription url填上gfwlist的url地址, 格式autoproxy, base64加密.proxy部分add proxies添加之前定义的代理方式,然后OK. 这时刚才设置代理时的URL pattern就会自动添加上gfwlist的网址哦~
6. GLobal settings可以设置图标点击的相应, 例如循环切换~ 使用循环切换我一般会编辑default将其取消在切换名单.

平日就切换到自动代理模式, 使用即可~

#### Proxy SwitchySharp（用于Chrome）

1. 去google 商店找SwitchySharp, 或者用上面介绍的这个网址去下:[Chrome Extension Downloader](http://chrome-extension-downloader.com/)或[get Chrome](http://getchrome.sinaapp.com/). 
2. 下载后可以看到这个地球图标和菜单 ![](/blogpic/switchysharp_2.png), 点`options`进行设置.
3. 设置你的SS代理(SOCKS5), IP是localhost或127.0.0.1, 端口就是你自己设的. ![](/blogpic/switchysharp_3.png). 这个设置好后, 可以在上面的弹出菜单看到设置的SS代理. 点选后就进行了该代理. 另外还可以设置不同颜色来显示哦~~
4. 除了上面的SS代理, 你还可以自己设置HTTP代理(例如GoAgent全部都HTTP). 在弹出菜单还可以选择: 直接连接(无代理), 自动代理(使用定义规则)和全局代理(就是系统里面的代理).
5. 自动代理: ![](/blogpic/switchysharp_1.png) 可以用通配符或者正则来定义网站名使用代理, 其余都不用代理. 除此以外, 更简洁是使用GFWlist来定义规则: 去[gfwlist官网](https://github.com/gfwlist/gfwlist)可以找到最新的gfwlist.txt: `https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt` . 填写到相应online rule file位置即可 (`AutoProxy兼容`也要勾上). 记得Proxy Profile那列是使用的代理方式, 就是该规则下使用该代理. 

可以参考[goagent+google Proxy SwitchySharp轻松几步实现fan\|墙教程](http://blog.zhe700.net/140.html)

#### 相关

一些**VPS服务**提供商用于自行搭建SS, 这里十分推荐使用廉价的[搬瓦工](https://bandwagonhost.com/aff.php?aff=10152)来自己搭建:

- [搬瓦工](https://bandwagonhost.com/aff.php?aff=10152): 廉价VPS. 自己搭! 强烈推荐自己搭建, 购买一年的价格和出去买个SS代理差不多, 还可以自己随意搭建VPN啥的哦! 一些中文介绍和使用可以参考[这个网](http://banwagong.cn/). 搭建好后点[Services](https://bandwagonhost.com/clientarea.php?action=products)的KiwiVM可以快速打开管理面板.
- [DigitalOcean](https://www.digitalocean.com/): 国外著名VPS提供商
- [linode](https://www.linode.com/): 国外著名VPS提供商, 配置比较好!
- [ConoHa](https://www.conoha.jp/referral/?token=7mUuW6KxSAzHkZz7WLTGciYPF.zlApL1T_daMICifYe761pwmm0-RPO): 一个日本的服务器, 速度不错, 最低配置是1G内存双核50GSSD,**无限流量**(适合看各种视频哦~),价格900日元每月(大概10刀吧). 支持支付宝!!!
- [vultr](https://www.vultr.com/): 主要是美国服务器, 还有东京巴黎伦敦阿姆斯特丹法兰克福悉尼的服务器. 价格5刀一个月, [SS/Svxn服务器搭建（梅林系路由科学上网）](https://www.chiphell.com/thread-1364921-1-1.html) 里面用到他, 好像速度还可以.

一些相关神器:

- [ChinaDNS](https://github.com/shadowsocks/ChinaDNS): 防止国内的DNS污染. 还有在[SF](https://sourceforge.net/projects/chinadns/)上的编译好的下载. 暂没用到. mark下. 可能是用在openwrt的路由器上面清洁路由器的. Ref: [小米路由器mini折腾之自动翻墙篇](https://blog.phpgao.com/carzy_router.html) 

一些提供SS服务的: 

- [ISS](http://www.ishadowsocks.org): 一个提供免费shadowsock来测试. 不过每几小时就会更新一次.
- [FreeVPNSS](http://i.freevpnss.com/) : 提供免费VPN和SS, 不过是经常改密码那种.
- [佛跳墙](http://www.godusevpn.mobi/) : 提供SS和VPN, 有3天试用哦.
- [shadowsocks.com](https://shadowsocks.com/): 假冒ss网址贩卖shadowsocks, 提供一些客户端下载方案.


可能会用到的: 

- [查IP](http://ip.cn/index.php?ip=): 查IP地址和来源咯, 检查是否代理成功
- [get Chrome](http://getchrome.sinaapp.com/): 提供chrome的各版本下载, 另外还有SwitchySharp插件和ShadowSocks客户端.
- [APK Downloader](https://apps.evozi.com/apk-downloader/) : 一个可以不通过google play来在线下载安卓软件的玩意. 就是帮你抓罗.
- [Chrome Extension Downloader](http://chrome-extension-downloader.com/) : 通过chrome插件URL或者ID来下载插件的东东

## VPN

PPTPD (容易被墙!!) : [Ubuntu搭建VPN服务器pptpd安装配置](http://blog.csdn.net/xanxus46/article/details/15288777), [Ubuntu Server下建立VPN服务器的方法](http://www.jb51.net/os/Ubuntu/34821.html)

[finchvpn](https://www.finchvpn.com/pricing): 一个免费的VPN, 可能会好用吧..

## 另外的方法

- [Nginx反向代理谷歌](http://www.68idc.cn/help/notebook/nginx/20150106161069.html)

不翻墙就google/google scholar:

- [GFSOSO](http://www.gfsoso.net): google + google scholar
- [atlps](http://jwss.atlps.com): 
- [Chongbuluo](http://xs.chongbuluo.com)

------
