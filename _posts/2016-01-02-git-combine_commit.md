---
layout: post
title: git合并多个commit
date: 2016-01-02 11:12:51
categories: IT
tags: Git
---

有时commit多了看着会不爽.所以想合并掉一些commit. 这里是最简单的情况, 一条线下来N个commit, 合并掉末端的(没有branch出去的).

假设有a,b,c,d四个commit, 从新到旧是a, b, c, d (也就是先d->c->b->a). 四个commit的SHA-1分别是a1,b1,c1,d1.

合并commit**只能倒退**, 就是说把a合到b(老的),顺序是abc可以合并起来成k, 最后成k, d这样.

## 过程:

~~~bash
# git log |head 
git rebase -i d1
# if fail, use git rebase --abort
git push --force 
~~~

1. `git log`可以查看commit的情况, 配着head命令可以查看前几个. `git log --pretty=oneline`一行一个commit更好了
2. rebase前需要把状态push掉. 就是说不能有unstaged的修改.
2. `-i` 是选择不动的commit, 比他新的commit都有被修改的可能.
3. 执行rebase后如果出错或者merge冲突什么退出来, rebase会被锁定, 再次执行时, 提示有三个选项: 
	- `git rebase --abort`来忽略之前的rebase尝试,并恢复HEAD到开始的分支. 
	- `git rebase --continue`就继续上次修改, 一般是rebase中间处理merge冲突后使用. 
	- `git rebase --skip`是重新开始rebase并跳过现在所进行的处理.
4. 执行rebase后会像commit一样进入编辑状态, 在开始会是几个commit的SHA值, 从上到下是越来越新的commit. 如果没有比-i指定的心的话会出现noop.
5. 开始状态所有出现的commit前面都是pick. 这个pick是对该commit进行的操作, 有:
	- `pick`就是说保留该commit, 也可以用缩写`p`. (黄色)
	- `squash`, 使用该commit但合并到前一个老的commit去(常用). 可以用缩写`s`代替 (绿色).
	- `reword`, 和pick类似, 但可以修改commit时的提交信息(中间会弹出来让你修改commit).可以用缩写`r`代替 (紫红色). 
	- `edit`, 使用commit, 但停下来进行修改, 可能用于merge冲突.可以用缩写`e`代替.
	- `fixup`, 和squash类似, 但会舍弃commit信息. 可以用缩写`f` (红色)
	- `exec`, 执行shell命令.可以用缩写`x`
6. 如果该commit是空commit, 前面会被注释掉`#`. 会被自动删除.
7. 执行完修改后,`:wq`退出vi, 这时开始进行rebase操作(1/10 这样倒数). 中间会再次弹出修改文件, 此时是修改commit信息, 可以修改每次commit的信息(如果是fixup会忽略掉commit提交信息). 最后这个合并后的新commit显示的信息可能是多个commit的集合(多行).不想修改或改完后直接`:wq`退出vi即可.
8. 所以都完成后需要一次强制的push, 要加入`--force`覆盖掉github上的commit.`git push --force`

例如我上面`-i d1`会修改3个commit, 保留最老最上最靠近d1的c (用reword或者pick都可以),其余a1和b1合并掉(squash或者fixup).最后生成一个新commit叫c2(就是3个合在一起了).所以从新到旧有c2, d1.  

------
