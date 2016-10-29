---
layout: post
title: 将Github Page迁移到GitCafe Page
date: 2015-07-07 19:26:18
categories: IT
tags: Git
---

GitCafe是国内的服务,国内用户用GitCafe肯定比GitHub要快多了.如果只是发博客的层次来说,GitCafe是个不错的选择.  
今天为了帮弟弟做介绍,自己大概弄了一下,总结一下吧.

## 注册GitCafe

去主页[注册](https://gitcafe.com/signup)一个账号,就是用户名密码邮箱什么的.注册后绿绿的,比较简陋哇.右上角的图标就是用户信息设置等.

## 同步Github到GitCafe
这部分是针对已有Github Pages进行迁移的童鞋. 没有的看下面:新用户使用GitCafe Pages..

### 连接Github
右上角,点上去后,账户设置,然后左边栏里有连接账号,点进去后可以见到Github了.点连接Github,输入github用户名密码,连接后要稍等.连接中是没成功,红色断开是连接上了.  

### 拉Github项目
连接了Github后,刷新一下页面看到导入项目(或者右上角,导入项目,再点GH猫),然后就可以看到你的项目了,选择你要迁移的博客. 好,然后就是等啊等.....(导入项目导入任意的,不仅仅是自己的博客).  
Github和GitCafe都是基于Git的,所以可以认为,GitCafe是中国版的仓库,一个项目可以推到GH,也可以推到GC.差异就是,GC并无GH那么多项目..  
导入项目需要一定的时间,取决于你的项目的占用空间了,右上角图标,我的主页,可以跳进去自己主页,像GH一样,可以看到项目.这时点你导入的项目,要是能正常打开查看文件了,就完成了.
另外,下一步之前,你需要将你本地的ssh-key密钥像GH一样填到GitCafe里.(右上,设置,导入密钥).

### 使用GitCafe Page

导入项目以后,就是使用GitCafe Page---Github Pages的代替品.也是基于Jekyll的.所以一个主页完全不用改就可以使用..  
Gitcafe page的帮助隐藏得很深([戳这里](https://gitcafe.com/GitCafe/Help/wiki/Pages-%E7%9B%B8%E5%85%B3%E5%B8%AE%E5%8A%A9#wiki))...简单说和GitHub类似,就是要把项目名称改为自己的用户名,并且将项目推送到gitcafe-pages分支(并不需要checkout分支的,直接push -u推送). 注意GH里面新建项目是自己"用户名.github.com"才识别为个人主页项目(项目名+GH网址),而且并不需要你推到gh-pages分支,这里不推送到分支就没有起效...  
熟悉Git的直接在本地仓库(不要告诉我没有本地仓库..)敲下面两个命令就好了(把我用户名platinhom改掉).第一个是创建一个远程仓库gitcafe.第二个是将master推送到远程仓库的gitcafe-pages分支.第二个命令后又是一个漫长等待(包括项目的比较和更新)...  
然后好了以后稍等,就可以在`用户名.gitcafe.io`看到自己的主页了,呵呵.而且你可以将第二句话(不加-u)加入到自己的推送脚本当中,以后就可以两边同时更新了.

~~~
git remote add gitcafe git@gitcafe.com:platinhom/platinhom.git
git push -u gitcafe master:gitcafe-pages
~~~

## 新用户使用GitCafe Pages
这个主要参考我Github 建博客(Ref2). 我这里针对Window用户简单快速交代必要的步骤.

1. 注册后GitCafe后,点右上角图标,再创建项目,项目名和用户名一样,直接创建.
2. 安装[MSYSGIT](http://msysgit.github.io/), 安装时要是有疑惑,记得选装上Bash版,记得在桌面生成图标就可以了.装好后在桌面看到图标,打开,见到命令行,OK,先关掉.
3. 移到你需要放置GC仓库的地方,例如在桌面上新建一个文件夹,叫MyGit.右键后用msysgit bash打开.这时打开命令行并进入到文件夹内.(或者桌面上的MSYSGIT打开,`cd /c/User/Username/Desktop`(Username是用户名,根据自己变化), 然后`mkdir MyGit`新建文件夹, `cd MyGit`进入文件夹,效果和上面新建文件夹右键msysgit一样.)
4. 创建密钥,免密码提交GitCafe修改.`ssh-keygen -t rsa -b 4096 -C "yourmail@hotmail.com"`后面的邮箱是你注册的邮箱,提示时passphrase不输入东西,总之一堆确定过去就可以了.复制公钥.mac可以`pbcopy < ~/.ssh/id_rsa.pub`, window下`clip < ~/.ssh/id_rsa.pub`.或者自行找到这个公钥文件(在我的文档下面),打开复制内容也可以. 
5. 右上角图标,账户设置,SSH公钥管理,添加,将密钥黏贴过来,名字根据你电脑随意起一个,确定就可以了.
6. 在之前新建的MyGit文件夹内,在命令行继续: `git clone git@gitcafe.com:platinhom/platinhom.git`, 这里把我用户名platinhom改成你自己的.然后稍等.
7. 完成`ls`一下,可以看到在MyGit里面有一个你用户名的文件夹, `cd username`进入这个文件夹. 输入`git remote add origin git@gitcafe.com:platinhom/platinhom.git`(替换我的用户名) 将远程仓库以origin名字加入到本地记录.
8. 在这个你用户名的文件夹内,新建一个文件index.txt,往里面输入"<html><body> Hello World </body></html>",保存后,将文件改名为index.html.这个就是你的主页了.
9. `git add -A` 将本地修改提交到临时库,`git commit -am "regular"`将修改提交到本地仓库.
10. `git push -u origin master:gitcafe-pages` 将仓库推送到gitcafe-pages当中. 好了,稍等,然后就去`username.gitcafe.io`这个页面刷一下你的主页吧.
11. 实验成果后,可以到[Github Page模板](https://github.com/jekyll/jekyll/wiki/Sites),点名字打开一些模板看看,看看你喜欢的样式,然后后退回模板页面,点该模板的`source`进入其github仓库,右下角有一个`download zip`,下载下来,解压,将里面的内容剪切到你的本地文件夹(例如桌面/MyGit/用户名/)里面. 继续在这文件夹内敲命令,`git add -A; git commit -am "regular"; git push origin master:gitcafe-pages;` 然后再去看看你自己的主页吧!好了,之后你就自己研究模板和学习Markdown了.有疑问请邮件咨询或qq.


## Reference

1. [GitCafe](https://gitcafe.com/)
2. [使用Github搭建博客](http://platinhom.github.io/2015/06/05/Build-Blog-Github/)

---
