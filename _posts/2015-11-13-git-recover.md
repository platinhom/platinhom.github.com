---
layout: post
title: Git仓库恢复
date: 2015-11-13 12:38:38
categories: IT
tags: Git
---

今天为了更新Gitcafe, 因为Gitcafe没有办法删除网上的远程分支, 只能借git的`git push origin :master`来实现...谁知道一个不小心在github博客上运行了...一上去发现全没了......整个master分支和仓库全没了.......T_T. 马上把整个本地文件夹复制到别的地方, 重新克隆远程过来, 然后复制那个备份文件夹的文件到这里来. 接着赶紧push到master去..然后发现...github上的master是有了..但是所有commit都没了... 不行, 得把修改记录弄回啦! 查到以下的方法, 能行!

-----

## 数据恢复

在使用 Git 的过程中，有时会不小心丢失 commit 信息。这一般出现在以下情况下：强制删除了一个分支而后又想重新使用这个分支，hard-reset 了一个分支从而丢弃了分支的部分 commit。如果这真的发生了，有什么办法把丢失的 commit 找回来呢？

下面的示例演示了对 test 仓库主分支进行 hard-reset 到一个老版本的 commit 的操作，然后恢复丢失的 commit 。首先查看一下当前的仓库状态：

~~~
$ git log --pretty=oneline
ab1afef80fac8e34258ff41fc1b867c702daa24b modified repo a bit
484a59275031909e19aadb7c92262719cfcdf19a added repo.rb
1a410efbd13591db07496601ebc7a059dd55cfe9 third commit
cac0cab538b970a37ea1e769cbbde608743bc96d second commit
fdf4fc3344e67ab068f836878b6c4951e3b15f3d first commit
~~~

最上的是最新的. 把老的库重新拷贝回来(包括.git文件夹)运行后发现, 的确存在之前的commit记录!

接着将 master 分支移回至中间的一个 commit (这里演示是第三个,我是用最新的.)：

~~~
$ git reset --hard 1a410efbd13591db07496601ebc7a059dd55cfe9
HEAD is now at 1a410ef third commit
$ git log --pretty=oneline
1a410efbd13591db07496601ebc7a059dd55cfe9 third commit
cac0cab538b970a37ea1e769cbbde608743bc96d second commit
fdf4fc3344e67ab068f836878b6c4951e3b15f3d first commit
~~~
这样就丢弃了最新的两个 commit ── 包含这两个 commit 的分支不存在了。现在要做的是找出最新的那个 commit 的 SHA，然后添加一个指它它的分支。关键在于找出**最新的 commit** 的 SHA ── 你不大可能记住了这个 SHA，是吧？

通常最快捷的办法是使用 `git reflog` 工具。当你 (在一个仓库下) 工作时，Git 会在你每次修改了 HEAD 时悄悄地将改动记录下来。当你提交或修改分支时，reflog 就会更新。`git update-ref` 命令也可以更新 reflog，这是在本章前面的 "Git References" 部分我们使用该命令而不是手工将 SHA 值写入 ref 文件的理由。任何时间运行 git reflog 命令可以查看当前的状态：

~~~
$ git reflog
1a410ef HEAD@{0}: 1a410efbd13591db07496601ebc7a059dd55cfe9: updating HEAD
ab1afef HEAD@{1}: ab1afef80fac8e34258ff41fc1b867c702daa24b: updating HEAD
~~~

可以看到我们签出的两个 commit ，但没有更多的相关信息。运行 `git log -g` 会输出 reflog 的正常日志，从而显示更多有用信息：

~~~
$ git log -g
commit 1a410efbd13591db07496601ebc7a059dd55cfe9
Reflog: HEAD@{0} (Scott Chacon <schacon@gmail.com>)
Reflog message: updating HEAD
Author: Scott Chacon <schacon@gmail.com>
Date:   Fri May 22 18:22:37 2009 -0700

    third commit

commit ab1afef80fac8e34258ff41fc1b867c702daa24b
Reflog: HEAD@{1} (Scott Chacon <schacon@gmail.com>)
Reflog message: updating HEAD
Author: Scott Chacon <schacon@gmail.com>
Date:   Fri May 22 18:15:24 2009 -0700

     modified repo a bit
~~~

看起来弄丢了的 commit 是底下那个，这样在那个 commit 上创建一个新分支就能把它恢复过来。比方说，可以在那个 commit (ab1afef) 上创建一个名为 recover-branch 的分支：

我就是用最新的commit SHA恢复了最新的这个recover-brance的分支.

~~~
$ git branch recover-branch ab1afef
$ git log --pretty=oneline recover-branch
ab1afef80fac8e34258ff41fc1b867c702daa24b modified repo a bit
484a59275031909e19aadb7c92262719cfcdf19a added repo.rb
1a410efbd13591db07496601ebc7a059dd55cfe9 third commit
cac0cab538b970a37ea1e769cbbde608743bc96d second commit
fdf4fc3344e67ab068f836878b6c4951e3b15f3d first commit
~~~

酷！这样有了一个跟原来 master 一样的 recover-branch 分支，最新的两个 commit 又找回来了。接着，假设引起 commit 丢失的原因并没有记录在 reflog 中 ── 可以通过删除 recover-branch 和 reflog 来模拟这种情况。这样最新的两个 commit 不会被任何东西引用到：

~~~
$ git branch -D recover-branch
$ rm -Rf .git/logs/
~~~

因为 reflog 数据是保存在 .git/logs/ 目录下的，这样就没有 reflog 了。现在要怎样恢复 commit 呢？办法之一是使用 git fsck 工具，该工具会检查仓库的数据完整性。如果指定 --full 选项，该命令显示所有未被其他对象引用 (指向) 的所有对象：

~~~
$ git fsck --full
dangling blob d670460b4b4aece5915caf5c68d12f560a9fe3e4
dangling commit ab1afef80fac8e34258ff41fc1b867c702daa24b
dangling tree aea790b9a58f6cf6f2804eeac9f0abbe9631e4c9
dangling blob 7108f7ecb345ee9d0084193f147cdad4d2998293
~~~
本例中，可以从 dangling commit 找到丢失了的 commit。用相同的方法就可以恢复它，即创建一个指向该 SHA 的分支。


## 处理方法

1. 先用 `git log --pretty=oneline` 调出所有commit记录, 或者 `git reflog` 调出所有在HEAD上的记录, 或者`git fsck --full`找出没有被指向的记录.找出相应SHA值.
2. 创建一个新分支, `git branch recover-branch SHAvalue`, 并`git push origin recover-branch:recover-branch` 推送上去创建一个分支. 此时发现commit已经回来了. 
3. 使用`git push origin :master` 删除老的无commit记录的master分支. 或者`git reset --hard SHAvalue`强制切换HEAD到最新分支, 再推送该分支到master. 推送不能的话, 先删掉相应远程的master分支(先切换默认分支到某个分支).
4. 重新推送到master分支, 如`git push origin recover-branch:master` (使用新分支法)或者`git push origin master`(用硬恢复的方法). 推送成功后commit就回来了!!

PS: 经测试, 主要恢复不过来原因是我拿最新的仓库复制过来再把文件推到GH, 导致master更新为光光的状态. 只要删除仓库后淡定, 马上运行一次`git push origin master` 即可完成恢复(因为此时已经有相关信息了..). 千万不要克隆一个空库过来再提交!!

## Reference
1. [Git 内部原理 - 维护及数据恢复](https://git-scm.com/book/zh/v1/Git-%E5%86%85%E9%83%A8%E5%8E%9F%E7%90%86-%E7%BB%B4%E6%8A%A4%E5%8F%8A%E6%95%B0%E6%8D%AE%E6%81%A2%E5%A4%8D)

------
