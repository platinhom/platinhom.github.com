---
layout: post
title: GIT教程(ZZ自廖雪峰)
date: 2015-10-14 16:37:13
categories: IT
tags: Git ZZ
---

#前言

为了学习Git，查阅了很多资料，比如：

- [Git与Github入门资料](http://www.yangzhiping.com/tech/git.html)
- [git-简明指南](http://rogerdudler.github.io/git-guide/index.zh.html)

前者太过精简，无法按照该教程一步一步来。后者页面设计的很花哨，也无法按照例程一步一步来。
最后在微博里，看到Python发烧友推荐的Python教程（从小白到大神）什么的，后来索性点击进去看看。接着就看到了作者的个人主页，[廖雪峰](http://www.liaoxuefeng.com/),然后发现边上的[Git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)。
只是读了第一段就被深深的吸引了，这就是我想要的。下面附上作者的简介，以及我自己在根据教程学习的笔记和摘要。

##Git教程
![](http://www.liaoxuefeng.com/files/attachments/0013848605496402772ffdb6ab448deb7eef7baa124171b000/0)

史上**最浅显易懂**的Git教程！

为什么要编写这个教程？因为我在学习Git的过程中，买过书，也在网上Google了一堆Git相关的文章和教程，但令人失望的是，这些教程不是难得令人发指，就是简单得一笔带过，或者，只支离破碎地介绍Git的某几个命令，还有直接从Git手册粘贴帮助文档的，总之，初学者很难找到一个由浅入深，学完后能立刻上手的Git教程。

既然号称史上最浅显易懂的Git教程，那这个教程有什么让你怦然心动的特点呢？

首先，本教程绝对面向初学者，没有接触过版本控制概念的读者也可以轻松入门，不必担心起步难度；

其次，本教程实用性超强，边学边练，一点也不觉得枯燥。而且，你所学的Git命令是“充分且必要”的，掌握了这些东西，你就可以通过Git轻松地完成你的工作。
##文字+图片还看不明白？有视频！！！
本教程只会让你成为Git用户，不会让你成为Git专家。很多Git命令只有那些专家才明白（事实上我也不明白，因为我不是Git专家），但我保证这些命令可能你一辈子都不会用到。既然Git是一个工具，就没必要把时间浪费在那些“高级”但几乎永远不会用到的命令上。一旦你真的非用不可了，到时候再自行Google或者请教专家也未迟。

如果你是一个开发人员，想用上这个世界上目前最先进的分布式版本控制系统，那么，赶快开始学习吧！

-----

#Git学习心得
本篇文档是根据对该教程的学习时写的**笔记**或者**摘要**，比较粗糙。好了，废话不多说进入正文。心得根据教程顺序记录。

-----------

##建立仓库
本地建立仓库，就是找个目录作为代码存放地方。
所以在Msysgit中，cd到某个目录，mkdir建立一个存放代码的目录，并进入该目录
比如：
> cd Document

> mkdir GitProject

> cd GitProject

进入到GitProject目录下后，使用git init命令对该目录进行初始化，
会生成.git文件，该文件Git的版本库
命令:
> git init

##git add filename
使用git add 添加文件，不论该文件是修改的，还是新添加的，都是采用git add filename
##git status
可以查看是否有文件修改或者添加进来
##git diff filename
可以查看该文件与已经提交过的文件的不同。
其中（还不确定），
- 红色字体表示完全不同，并且会带有符号减
- 白色表示二者皆有，行前无符号
- 绿色表示新添加的，行前有加号

##git log
显示commit记录

##git log --pretty=oneline
以一行记录来显示commit记录，包括commit的版本号和-m后的消息，该版本号由SHA1计算出来。

##git reset --hard HEAD^
用于回退到某个commit，其中HEAD^表示回退到上一个提交版本
HEAD^^表示回退到上上个版本，HEAD~100表示回退到100个提交版本之前
这就好比穿越时光机
此时，在用git log就不会出现该版本之后的版本了
但只要该命令行窗口未关闭，你可以查看之前使用git log显示的版本号前几位
比如0a33aaa,无需全部的版本号，前几位即可。

## git reflog
该命令即是为了在关闭命令行窗口后，如何寻找之前的命令记录
该命令会显示所有的commit 记录。

> HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，使用命令git reset --hard commit_id。
> 穿梭前，用git log可以查看提交历史，以便确定要回退到哪个版本。
> 要重返未来，用git reflog查看命令历史，以便确定要回到未来的哪个版本。

## 工作区和暂存区
分为工作区和版本库，其中版本库包括一个暂存区Stage和一个Master，HEAD指针指向Mater。
工作区，是还未进行add和commit的文件，此时的通过git status查看，这样的文件是untracked的。

当执行add时，将工作区的文件add到Stage中，接着使用commit就会将stage区中的文件提交到Master分支中。
关系如下图所示。

![](http://www.liaoxuefeng.com/files/attachments/001384907720458e56751df1c474485b697575073c40ae9000/0)

暂存区是很重要的概念。

##管理修改
为什么Git比其他版本控制系统设计得优秀，因为Git跟踪并管理的是修改，而非文件。

##git checkout -- filename
场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令
> git checkout -- file。

## git reset HEAD filename
场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令

> git reset HEAD file

就回到了场景1，第二步按场景1操作。

## git reset --hard HEAD^^
场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考版本回退一节，不过前提是没有推送到远程库。


## 删除文件
> rm filename

删除工作区中的文件，如果此时该文件已经在暂存区Stage或者Mater中，那么git status就会检测到不一致，
所以接着就是使用

> git rm filename

删除在版本库中的记录，接着commit提交。此时还可以使用
> git checkout -- filename

来撤销对工作区的修改。
Tips 

> 命令git rm用于删除一个文件。如果一个文件已经被提交到版本库，那么你永远不用担心误删，但是要小心，你只能恢复文件到最新版本，你会丢失最近一次提交后你修改的内容。

## 建立远程仓库
1. 注册github账号
2. 本地msysgit命令行中使用命令生成SSH秘钥

>  ssh-keygen -t rsa -C "youremail@example.com"

将生成的秘钥id_rsa.pub这个公钥中的内容拷贝出来
3. 在GitHub中账户设置“Account Setting”中Add SSH settings，然后将拷贝的秘钥赋值进去。
5. 在GitHub中新建新的仓库，账户边上的+号中“create new repo”,设置项目名，比如Test

## 连接远程仓库
在msysgit中使用
> git remote add origin git@github.com:KylinGu/Test.git

其中KylinGu改为自己的用户名。
这个就是将本地的仓库与GitHub的仓库关联上，origin为你的远程仓库的别名。
接着：
> git push -u origin master

将本地仓库的master分支推送至远程仓库origin的master分支上。
-u第一次推送时使用，之后无需再加-u.

> 要关联一个远程库，使用命令**git remote add origin git@server-name:path/repo-name.git**；

关联后，使用命令**git push -u origin master**第一次推送master分支的所有内容；

此后，每次本地提交后，只要有必要，就可以使用命令**git push origin master**推送最新修改；

## 分支
git的分支解释，HEAD指向分支，也即指向Master，Master指向提交commit。
创建分支，就是将HEAD指向分支,比如dev，然后dev指向commit。
所以Master的版本还是Master.

创建一个dev的分支

> git branch dev
 
切换到dev分支
> git checkout dev

查看分支
> git branch

创建+切换分支
> git checkout -b name

合并某分支name到当前分支
> git merge name

删除分支
> git branch -d name

当Git无法自动合并分支时，可根据git status提示，查看冲突文件。Git用如下的方式标记冲突内容。
- <<<<<<<HEAD
- master 内容
- =======
- 分支内容
- >>>>>>>feature1 

然后手工调整，解决冲突，之后再添加提交。可以通过**git log --graph**查看分支合并情况
> git log --graph --pretty=oneline --abbrev-commit

##分支策略

- Matster分支作为仅用来发布稳定版

- 干活在Dev分支上，每个人的各自分支都向Dev分支上合并，最终发布稳定版，就向Master合并

- 团队合作就如图所示:

![](http://www.liaoxuefeng.com/files/attachments/001384909239390d355eb07d9d64305b6322aaf4edac1e3000/0)

**Tips**
> 合并分支时，加上**--no-ff**参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，而fast forward合并就看不出来曾经做过合并。

##Bug 分支
git提供了一个stash分支，可以把工作区的未提交修改“储藏起来”，等以后恢复现场后继续工作。
> git stash

保存工作区，进入master分支，建立bug分支，修复后提交到master分区。删除bug分支，切换回dev分支

> git  stash pop

恢复工作区。

## feature分支
开发一个新feature，最好新建一个分支；如果要丢弃一个没有被合并过的分支，使用
> git branch -d branchname

将提示无法删除，可以通过一下命令强行删除。
> git branch -D branchname

##多人协作
> git push origin master

其中origin表示远程分支，master表示本地分支。
> git push origin dev

###Tips
- master分支是主分支，因此要时刻与远程同步；
- dev分支是开发分支，团队所有成员都需要在上面工作，所以也需要与远程同步；
- bug分支只用于在本地修复bug，就没必要推到远程了，除非老板要看看你每周到底修复了几个bug；
- feature分支是否推到远程，取决于你是否和你的小伙伴合作在上面开发。

将dev分支推送至远程仓库的dev分支，这样其它人就可以建立dev的分支branchname，建立方法如下：
>  git checkout -b branchname origin/dev

之后就可以使用git push 推送到远程dev仓库里
> git push origin branchname

若是两个人对同一个文件进行了修改，那么push将导致出错。

解决方法：
- git branch --set-upstream branchname origin/dev
- git pull
- 解决冲突文件,然后add,commit 再push

###Tips
1. 首先，可以试图用git push origin branch-name推送自己的修改；

2. 如果推送失败，则因为远程分支比你的本地更新，需要先用git pull试图合并；
3. 如果合并有冲突，则解决冲突，并在本地提交；
4. 没有冲突或者解决掉冲突后，再用git push origin branch-name推送就能成功！

如果git pull提示“no tracking information”，则说明本地分支和远程分支的链接关系没有创建，用命令**git branch --set-upstream branch-name origin/branch-name**。

这就是多人协作的工作模式，一旦熟悉了，就非常简单。

## 标签

- 给当前的HEAD打一个标签tagname

> git tag tagname 

- 给commitid打一个标签tagname

> git tag tagname commitid
 
- 查看所有标签

> git tag

- 查看标签信息

> git show tagname

- 创建带有标签说明的标签-a 指定标签名，-m 指明说明

> git tag -a v0.1 -m "version 0.1 released" 3628164

- 删除标签

> 命令**git tag -d tagname**可以删除一个本地标签；命令git push origin :refs/tags/tagname可以删除一个远程标签。

- 推送标签

> 命令**git push origin tagname**可以推送一个本地标签；命令**git push origin --tags**可以推送全部未推送过的本地标签；

## GitHub
首先要Fork别人的项目，然后再本地clone下来，接着自己可以更改并push。
如果不Fork直接Clone别人的项目是无法push的，权限问题。

**Tips**

> 在GitHub上，可以任意Fork开源仓库；自己拥有Fork后的仓库的读写权限；可以推送pull request给官方仓库来贡献代码。

-------------------

## 搭建Git服务器
这个不学习喽。
贴下[网址](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/00137583770360579bc4b458f044ce7afed3df579123eca000)，有需要再去看。

-------------------

学习完毕。廖雪峰大神写的教程写的真好，通俗易懂。
准备去拜读他写的Python教程。


------------------------
# git比较本地仓库和远程仓库差异
转载自[git 如何比较本地仓库和远程仓库之间的差异？](http://hi.baidu.com/configuration/item/02329df98b43d40cd89e725d)

在pull之前，可以先比较本地仓库和远程仓库之间的差异
1. 添加需要比较的远程仓库；
> git remote add foobar git://github.com/user/foobar.git

2. 取回foobar的内容，fetch不会修改本地的内容；
> git fetch foobar

3. 比较本地分支和远程分支之间的差异
> git diff master foobar/master

4. 远程分支已经修改，本地未同步的变更；
> git diff HEAD...origin/master

5. 本地分支已经修改，远程未同步的变更；
> git diff origin/master...HEAD




















