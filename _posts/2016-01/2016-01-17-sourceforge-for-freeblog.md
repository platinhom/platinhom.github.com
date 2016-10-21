---
layout: post
title: SourceForge用于免费博客搭建(1)-SSH+SFTP+SCP
date: 2016-01-17 13:06:10
categories: IT
tags: Internet
---

## 前言

因为项目零散文件太多太多, 使用git来提交的话实在太慢太慢了. Github的纯静态网页不支持php/python等动态语言处理的风格实在是太约束...数据库也不支持, 真是个代码仓库罢了...

找一些别的解决方案, 看看有木有免费的服务器可用. 先找到的是新浪的云计算[SAE](http://sae.sina.com.cn), 其他的什么百度的[BAE](https://bce.baidu.com/product/bae.html), 亚马逊的云, 阿里巴巴啥的都是收费的...SAE是用什么豆, 低使用量的话可能够用, 但是对访问次数啊什么都有限定, 超过了就给money了..因为我是用来自检的, 访问量暴大.. 所以对响应时间也有要求.

我只是想找个免费的可以提供1G以下大小的地方啊啊啊!! (最好当然有mysql, php/python一类的啦~)

然后看到一个帖子介绍托管静态网页的一些服务商:

服务名称				|绑定域名		|空间大小	|	发布方式		|	托管内容
--------------------|-----------|-------|---------------|-----------------------
GitHub Pages		|支持		|1GB 	|	Git 		|	静态网站或 Jekyll 站点
GitCafe Pages		|支持		|512MB 	|	Git			|	静态网站或 |	Jekyll 站点
七牛云存储			|支持(需备案)	|10GB	|	七牛同步工具	|	静态网站
Google App Engine	|新版不支持  	|1GB	|Git 或 GAE 工具	|	静态、Python、Java、PHP 站点
Opoo Pages			|暂不支持	  	|不限	|	Git			|	OpooPress 站点
SourceForge.net		|支持       	|不限	|	SCP/FTP		|	静态、PHP、Python 等站点

> [几种可以免费托管静态网站的服务对比](http://opoo.org/2014/free-service-for-static-site/)

- Github Page/Gitcafe page 是基于Git+Jekyll的, 一般也就够了. 但我的需求比较奇怪: 几十万上百甚至千万的空白文件....
- [七牛云](https://portal.qiniu.com/)虽然也不错, 但是还是有访问次数的限制的,空间嘛, 也够用啦~ 
- 至于GAE, 嗯, Google那种都爬几次都验证码的公司的产品服务肯定不是那么free和nice的...

最后, 咦, 原来SourceForge也可以托管静态网页还不限空间, 还支持PHP/Python这么diao?!!! 于是我就去看了看. 实在太TM赞了!

## SourceForge对于项目的支持功能:

- SSH登录服务器 !!
- 网页上传, SFTP/SCP/Rsync !!
- SSH上去后提供 cgi-bin, htdocs 文件夹(你懂), Apache + MySQL!!
- 可以使用 GIT/SVN  

更多简介和帮助请看[Document的TOC](https://sourceforge.net/p/forge/documentation/ToC/)

## 可以访问的目录

这里面有四组地址要记住:

1. 用户目录: `/home/users/首字母/首2字母/用户名`
2. project 主页(就是`project.sourceforge.net/`)内容所在 `/home/project-web/PROJECTNAME/`, cgi-bin定向到网页`/cgi-bin/`下. htdocs就是主页所在咯.
3. files 位置(就是发布的文件啊, 各个版本zip啊之类): `/home/frs/project/PROJECTNAME/`
4. 用户的主页: `/home/user-web/USERNAME/`, 里面也有cgi-bin和htdocs

## SSH

> 免登陆准备: 如果不想每次都输入账号密码, 当然就是使用公钥私钥啦..在 `Account Setting` 里头的 `SSH Setting` 里头黏贴你的公钥就可以了. 每行一个. 不明白的就自己百度或者戳官方[这里](https://sourceforge.net/p/forge/documentation/SSH%20Keys/)..

> 支持使用`USER`和`USER,PROJECT`的格式(用`,`分割两者识别究竟是何project.). 两者有差异, SSH时都是登录到用户HOME目录. SCP/SFTP使用用户名到的是用户目录, 使用 用户名,PROJECTNAME 登录的是PROJECT的web目录.

登录格式是 `ssh USER,PROJECT@shell.sourceforge.net`, 即门户是 **shell.**sourceforge.net.

但登录会报错: 

~~~
>> ssh user,project@shell.sourceforge.net
Logging in to your interactive shell...

You don't have an active shell at this time.  For basic file transfers and
management, use web.sourceforge.net -- it allows rsync, sftp, and scp access.

If you would like to create a shell, use ssh to login using a USER,PROJECT
username with the "create" command.  If you tell ssh to allocate a tty
(e.g. using -t), an interactive shell will be opened when the create is
done.  Otherwise, the create command will exit when the shell becomes
ready for use.  An example create that enters the shell when ready:

    ssh -t USER,PROJECT@shell.sourceforge.net create

Connection to shell.sourceforge.net closed.
~~~

因为SF每个登录对话都是有个有效期的(4小时), 需要登录就要:

- 创建新登录对话, 如提示: `ssh -t USER,PROJECT@shell.sourceforge.net create` (没有`-t`创建后会退出)
- 等待后登录进去就能使用.
- 退出后从创建登录后4小时内, 只要 `ssh User,Project@shell.sourceforge.net`即可.
- 登录进去好, 假设用户名是 `hello`, 那么路径是`/home/users/h/he/hello`. 即`/home/users/首字母/首2字母/用户名` 登陆进去后啥都木有, 不过可以设置`.bashrc`等东西, 例如我就设置了:

~~~bash
# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

# User specific aliases and functions
alias goto_home='cd /home/users/p/pl/platinhom'
alias goto_cgi='cd /home/project-web/myproject/cgi-bin'
alias goto_web='cd /home/project-web/myproject/htdocs'
alias goto_file='cd /home/frs/project/myproject'
alias goto_userweb='cd /home/user-web/platinhom'
~~~

## SCP

可以使用命令行来上传文件! 

`scp filename USER,PROJECT@frs.sourceforge.net:/home/frs/project/PROJECTNAME/DIRNAME`

## SFTP

可以使用命令行`sftp USER,PROJECT@frs.sourceforge.net` 来登录到SFTP, 然后用命令行方式操作, 支持操作[参考](/2016/01/08/sftp-cmd/).

另外当然可以使用GUI界面例如FileZilla, WinSCP一类软件啦, 配置是:

- 服务器: `frs.sourceforge.net` 或者 `web.sourceforge.net` (后者我在GUI时登不上去..)
- 端口: 22
- 用户名: USER,PROJECT
- 密码自己设定..

使用`USER,PROJECT`去到的是Project的web 文件目录. 如果用户名不加PROJECT就会跑到用户 Home 目录. 貌似没有办法直接上去就是frs文件目录, 只能使用绝对路径.


## RSYNC

- 上传同步:

`rsync -avP -e ssh LOCALDIR/ USER@web.sourceforge.net:/home/project-web/PROJECTNAME/htdocs/`

- 备份到本地同步

`rsync -avP -e ssh USER@web.sourceforge.net:/home/project-web/PROJECTNAME/htdocs/ LOCALDIR/ `

### Reference

1. [官方文件管理介绍](https://sourceforge.net/p/forge/documentation/File%20Management/)
2. [官方SSH介绍](https://sourceforge.net/p/forge/documentation/SSH/)
3. [官方SCP使用介绍](https://sourceforge.net/p/forge/documentation/SCP/)
4. [官方SFTP使用介绍](https://sourceforge.net/p/forge/documentation/SFTP/)
5. [Project Web and Developer Web Server Configuration Details](https://sourceforge.net/p/forge/documentation/Project%20Web%20and%20Developer%20Web/)
6. [Project Web Filesystem Permissions](https://sourceforge.net/p/forge/documentation/Project%20Web%20Filesystem%20Permissions/)
7. [Project Web](https://sourceforge.net/p/forge/documentation/Project%20Web%20Services/)

------
