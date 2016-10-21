---
layout: post
title: Github提交个人修改到开源项目
date: 2015-10-31 00:28:26
categories: IT
tags: Git
---

今天发现openbabel的pqr处理有点问题,所以想将修改提交上去. 查了一下, 做法其实很简单.

1. fork那个项目
2. 修改自己fork的项目
3. 进入github自己的该项目, 点pull requese

简要流程以[openbabel项目](git@github.com:openbabel/openbabel.git)为例:

1. 进入[openbabel项目](git@github.com:openbabel/openbabel.git), 点右上的分叉的Fork. 会等一段时间, fork该项目到自己的repository. 这个项目分支是你的,可以随便改; 而原来的项目则由管理员管理, 你是不能修改的.
2. 本地新建一个文件夹,例如ob. (因为我要在别的地方调试,这个新文件夹内用于与原来的repository保持一致)
3. 克隆该项目: `git clone git@github.com:openbabel/openbabel.git`
4. 进入该文件夹并进行修改,例如`cd openbabel/src/formats`修改了`pqrformat.cpp`
5. 修改后,首先提交修改的文件记录到本地库进行更新.`git add pqrformat.cpp;git commit -m "myComment"`.add是提交到临时库,commit是执行一次修改并提交到本地仓库.
6. 将修改提交push到github上自己的库内,`git push origin master`
7. 回到自己的github, 点到fork的自己的openbabel repository, 在中间找到pull request; 或者绿色方块内有Compare到某个分支的按钮也可以实现pull request. 更多细节可参考ref2.
8. base fork部分是要提交的地方,head fork是自己的,可以选择对比对象. 填上这次提交的主题和细节, 方便管理员管理. 在下面可以看到你修改的变化的细节. 最后提交上去就好了.
9. 要是提交了pull request而管理员没通过, 此时又进行了修改, 继续将修改提交到自己的库, 点pull request后, 会进行相应的将两次修改进行合并(要是不一致可能会要进行选择).
10. 提交后, 在Github上面的`Pull Requests`可以看到自己的提交, 开始时不是绿的,系统会进行审查比较, 系统通过后会变成绿色, 状态open. 然后就等管理员的批复吧.

## Reference

1. [github的多人协作](https://gist.github.com/suziewong/4378619)
2. [Github-Pull Request](https://help.github.com/articles/using-pull-requests/)

------
