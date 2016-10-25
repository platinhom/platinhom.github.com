---
layout: post
title: Github:重命名仓库
date: 2015-12-16 19:53:30
categories: IT
tags: Git
---

Git类工具可以重命名仓库, 这里介绍Github上的

#### 1.Github页面修改仓库信息

跑到自己的仓库那,找到`Setting`的tag, 点进去后Options的Settings就可以设定Repository name.

#### 2.修改本地仓库信息

因为远程的仓库名改了, 本地的对应仓库名也要改. 这里假设远程仓库本地命名为origin.

- git remote -v  
列出所有远程仓库信息, 包括网址.

- git remote set-url origin git@github.com:username/newrepo.git  
修改远程仓库对应的网址.

就这么就够了. 这是最简单的. 还有种比较愚蠢的做法...不喜好的就不用看下面了..这是我根据网上一些贴的失败尝试..

- git remote rm origin  
删掉本地的远程仓库信息
- git remote add origin git@github.com:username/newrepo.git  
添加新的远程仓库, 相当于本地远程仓库信息变更了...
- git branch --set-upstream-to=origin/master master  
上面这么做还不够..因为没有追踪相应的branch..上面的指令可以使这个"新"的仓库follow远程的master分支

另外还有个可能可以参考的指令:

- git remote rename hi hello  
重命名本地远程仓库名, 从hi改为hello


------
