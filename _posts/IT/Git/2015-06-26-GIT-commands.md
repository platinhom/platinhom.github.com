---
layout: post
title: GIT命令总结
date: 2015-06-25 17:49:47
categories: IT
tags: Git
---






##基础知识

- 对于任何一个文件, 在 Git 内都只有三种状态：已修改(modified), 已暂存(staged)和已提交(committed),对应文件流转的三个工作区域：Git 的工作目录,暂存区域(staging region或index), 以及本地仓库(git directory). 另外, 远程仓库是需要联网的另一区域. HEAD是最后一次commit的结果. 子命令和各个工作区域间的关系参看下图. [更多基础](http://git-scm.com/book/zh/v1/%E8%B5%B7%E6%AD%A5-Git-%E5%9F%BA%E7%A1%80 )

<center></center>

- 提交对象, 分支, 父节点, HEAD,分叉点, 合并点: **提交对象**就是每次commit产生的记录对象, 一个节点. **分支branch**就是指向commit对象的可变指针,一种标记. **父节点parent**就是指某分支的上上次commit时的记录(即上一个commit对象). **HEAD**就是指向当前工作所在分支的指针(也可以指向没有分支标记的commit对象,此时叫**匿名分支detached HEAD**). **分叉点(共同祖先)**就是两个不同branch分别开发时产生的分叉点,在合并merge时作为**三方合并**参考点, 而进行三方合并后可能产生新的提交记录节点综合各版本信息的**合并点**. 在Git里面, HEAD^或HEAD~ 指head的第一父提交. HEAD~3表示父的父的父, 也可以写成HEAD^^^. 而HEAD^2表示第二父提交, 只在合并提交时有用, 第一父提交是合并时所在分支的父, 而第二父提交指合并时另一分支的父(走位merge选项的分支).  [更多参考:必读](http://git-scm.com/book/zh/v1/Git-%E5%88%86%E6%94%AF  )

-----

##Git命令: 

- 执行命令 ** `Git 子命令 选项 对象` **

**子命令**: add, bisect, brance, checkout, clone, commit, diff, fetch, grep, init, log, merge, mv, pull, push, rebase, reset, rm, show, status, tag 

**十分好的去理解主要命令的原理参考** [图解Git: 必读](http://marklodato.github.io/visual-git-guide/index-zh-cn.html ); [命令参考](http://git-scm.com/docs  )

- ###辅助性子命令

1. #### [git config](http://git-scm.com/docs/git-config ) 配置信息(记录log必须) 

 - `git config --global user.name "hello"`  配置用户名. --global/system global针对某用户全起效,system整个系统起效, 不加该参数只对该工程起效.  (分别保存在 `~/.gitconfig`, `/etc/gitconfig`, `.git/config` 文件内. 一般要设置`user.name` 以及 `user.email`. 如果不指名值(这里hello), 则会返回该变量的值.

 - `git config --list` 列出各种基础配置信息. 可以使用以上方法设置, 或者修改相应config文件
 - `git config --system core.longpaths true` 在msys中文件名过长时会: error: cannot stat '...文件名': ilename too long, pull不过来报错.用这个命令可以解决.[ref](http://stackoverflow.com/questions/22575662/filename-too-long-in-git-for-windows)


2. ####[git help](http://git-scm.com/docs/git-help ) 进行帮助

 - `git help -a` 可以列出所有子命令;  `git help -g` 列出概念,

 - `git help 命令/概念` 可以进行帮助. 子命令选项帮助一般用`git 子命令 --help/-h` 



3. #### [git status](http://git-scm.com/docs/git-status)  查询文件状态

 - `git status` 查询状态, untracked就是文件尚未跟踪(新建), change not stated for commit就是修改未暂存; changes to be commited就是暂存未提交. 不提及的就是commited的.

4. ####[git log](http://git-scm.com/docs/git-log )  查看提交历史

git log 有很多[参数和功能](http://git-scm.com/book/zh/v1/Git-%E5%9F%BA%E7%A1%80-%E6%9F%A5%E7%9C%8B%E6%8F%90%E4%BA%A4%E5%8E%86%E5%8F%B2  ). 也可以用gitk图形界面去弄.

 - `git log` 查看提交commit历史,最近的排最上, 包括commit哈希,作者信息,时间,提交说明. 图形化查询可用gitk或者eclipse的show history

 - `git log -p -2` -2是指定仅显示最近2次更新, -p 是展开每次提交内容差异(相当于git diff ver1 ver2).



5. #### [git diff](http://git-scm.com/docs/git-diff )查看区别

 - `git diff <path>` 查看尚未暂存的该些文件更新了那些部分(当前 vs 已暂存). 一般, -的为旧版, +的为新版. <path>为空即为当前目录所有内容.

 - `git diff --cached <path>` 查看已暂存的和上次提交的版本差异 (已暂存 vs 已提交)

 - `git diff HEAD <path>` 查看当前文件和上次提交的版本差异(好像和上没啥差别) (当前 vs 已提交)

 - `git diff ver1 ver2 <path>` 查看指定版本之间的差别, ver1就是那寸哈希的前面部分.

 - `git diff --word-diff <path>` 查看更新差异, 显示的是单词差异的模式.

6. #### [git show](http://git-scm.com/docs/git-show )

7. #### [git bisect](http://git-scm.com/docs/git-bisect )

8. #### [git grep](http://git-scm.com/docs/git-grep )



- ###本地操作仓库子命令



2. #### [git init](http://git-scm.com/docs/git-init  ) 初始化新仓库

 - `git init ` 初始化新建仓库(新建.git目录).在已有仓库中无影响. 也有专门用于转移和更新目录所在选项.
 - `git init --bare` 裸仓库,只储存历史提交版本信息, 不允许git操作. 一般作为中心库采用, 避免使用中产生的冲突.



7. #### [git tag](http://git-scm.com/docs/git-tag )  设置tag来标记commit,相当于给SHA1哈希串重命名

 - `git tag<tagname> <commit>`  将commit(哈希码前N个字符)设为tag(名为tagnmame,可用中文 ╮(╯▽╰)╭).
 - `git tag -d<tagname>`  删除某个tag.

5. #### [git branch](http://git-scm.com/docs/git-brance )  列出,创建和删除分支.

 - `git branch <branchname>` 当前位置创建一个分支, 但是HEAD并不转移过去(不同于checkout -b)
 - `git branch <branch> <commit>` 在commit(也可以是tag)处创建一个分支, 但是HEAD并不转移过去(不同于checkout -b)
 - `git branch` 参看本地主机分支.
 - `git branch -v` 参看本地主机分支, 并列出具体commit的SHA1哈希以及comments
 - `git branch -r` 参看远程主机分支.
 - `git branch -a` 参看远程主机分支(remotes/主机/分支)以及本地分支(前面打*为当前分支).
 - `git branch -d <分支名>` 删除指定已合并的分支. -D是即使没合并一样删除(强制删除).
 - `git branch --merged/--no-merged` 查看与当前分支合并了的分支(可删)以及未合并的分支.
 - `git branch --set-upstream <本地分支> <远程主机名:远程分支>` 设定本地分支track 指定的远程分支.
 - `git branch show origin` 查看远程分支情况

5. #### [git add](http://git-scm.com/docs/git-add )  将文件加入到暂存区域(索引化); [git rm](http://git-scm.com/docs/git-rm )  删除文件或文件索引; [git mv](http://git-scm.com/docs/git-mv )  移动文件/改名

    add和rm都是针对暂存区域进行操作.

 - `git add *.cpp`   将文件索引化到暂存区域. 后面也可以用文件夹名字来增加.

 - `git add -u`  只加修改過的檔案, 新增的檔案不加入.

 - `git rm filename` 当物理删除(如shell的rm命令)后, 从暂存区域内去除该文件.

 - `git rm -f filename`  删除文件并去除索引状态. 不加-f 删不了文件, 可用一般的rm命令删除

 - `git rm --cached filename`  只删除索引但保留文件(恢复成untracked状态.

 - `git mv file1 file2` 移动本地文件, 并在暂存区进行信息更新(相当于mv f1 f2 + git rm f1 + git add f2)

6. #### [git commit](http://git-scm.com/docs/git-commit )  提交到仓库HEAD, 形成一次版本. 



 - `git commit -m "comments" `   进行提交, -m指明该次提交的

 - `git commit -a ` 提交包括未暂存的, 需要编辑参数去注释, 留一行为提交comments.

 - `git commit --amend` 重新提交,更新刚才的提交. 会使用当前暂存区域快照. 适用于添加文件和修改提交信息. 



7. #### [git revert](http://git-scm.com/docs/git-revert )  撤销提交

 - `git revert HEAD ` 撤销提交, 一般就是撤销上次的提交, 但不影响工作区的文件,可修改后再提交.
 - `git revert <commit>` 撤销提交回到某个commit的父节点, -n 对于多节点恢复有意义, 可避免强制提交.


3. #### [git checkout](http://git-scm.com/docs/git-checkout )  从本地库或暂存区域内拷贝文件到当前工作目录(默认)或暂存区(可选), 也可用于创建和切换分支.

 - `git checkout -- files`  把文件从暂存区域复制到工作目录，用来丢弃本地修改。

 - `git checkout HEAD files`  把文件从HEAD复制到暂存以及工作目录, 此时打--无意义。

 - `git checkout <branch/commit>files`  把文件从某个版本复制到暂存以及工作目录, 是上一种的广泛法。注意有跟file就**不改变HEAD位置**, 只是提取!

 - `git checkout <branch>`  HEAD切换到branch, 并将工作区和索引区均根据branch更新(只存在旧版本的文件被删除).

 - `git checkout <commit/tag/远程分支/master~2等>`  HEAD切换到该位置,得到匿名分支(detached HEAD), 并更新将工作区和索引区. 注意此时位点并非一般分支, 一般操作完需要用checkout跳回某个分支. 对于匿名分支进行commit, 会产生无法再引用的支路(非branch标记)而被丢弃, 此时需要用`git checkout -b newbranch`构建新的branch.

 - `git checkout -b <branch> <place>`  创建一个分支branch, 并将HEAD切换到branch,相当于branch和checkout的合用. 新建位置<place>可以是分支,节点标签等, 省略即在当前位置. 

 - `git checkout --track <remote>/<branch>` 可以创建本地同名分支使其追踪某个远程分支.

4. #### [git reset](http://git-scm.com/docs/git-reset )  改变当前HEAD分支档案位置(也可以不变), 有选择的变动索引(默认)和工作目录. 

 - `git reset -- files` 将**暂存区文件状态恢复**到HEAD中状态而**不影响工作目录**. 等价于 `git reset HEAD files`以及`git reset files`(无法设置--hard之类). PS: 很多教程说用来撤销最后一次git add files的说法有误. f1(Head), 更改f11后add,再改f111后add, 用该指令暂存区恢复到f1状态(即所有add均恢复). 所以实际效果是"索引会回滚到最后一次提交". 

 - `git reset <commit> files` 将暂存区文件状态恢复到<commit>中相应文件状态而**不影响工作目录**, 更一般形式. (无法设置--hard之类).

 - `git reset --hard/soft <commit>` 将**HEAD连同所在branch**切换到commit档案, 并根据参数复制内容到工作目录/暂存区: --soft不改变工作目录和暂存区; --hard 改变工作目录和暂存区. --mixed 改变暂存区但不改变工作目录(**默认形式**). 另外还有--merge和--keep模式. 该模式带有移动branch+HEAD再全文件复制下来的功效. 不能指明具体文件.

#####reset 默认是将commit恢复到" index ", checkout是commit恢复到" workshop ". reset移动HEAD时"连同原分支(不切换分支) "一起移动, 而checkout则只移动HEAD"不移动分支(切换分支) ".

4. #### [git merge](http://git-scm.com/docs/git-merge )  合并两个以上分支的开发历史.

 - `git merge <branch>` 以现在所在分支为主分支, 合并branch分支. 可能出现"Fast-forward":两节点为单线历史分支,快进合并比较容易(直接合并移动到最新分支); "'recursive' strategy" 中间出现过共同祖先分叉点的两个不同版本, 此时需要识别出最佳的同源合并点, 可能会由于内容冲突而出现conflict状态, 需要修改后再add再commit.

 - `git mergetool` 调用可视化合并工具, 需要设置(上网参考合并[冲突处理](http://git-scm.com/book/zh/v1/Git-%E5%88%86%E6%94%AF-%E5%88%86%E6%94%AF%E7%9A%84%E6%96%B0%E5%BB%BA%E4%B8%8E%E5%90%88%E5%B9%B6 )细节)

4. #### [git rebase](http://git-scm.com/docs/git-rebase )  分支的衍合

 - `git rebase <branch>` 将共同祖先到现所在节点的变化作为补丁, 以该branch为基础进行衍生. 会改变原来所在的分支. 此时branch成为祖先, 可进一步快进合并.衍合和三分合并区别: 三方合并不改变原来两节点,新建一节点, 衍合则直接将所在节点进行迁移,另一节点不变; 从两分支直接变成一主线. 一旦分支中的提交对象发布到公共仓库，就千万不要对该分支进行衍合操作, 因为衍合会在本地迁移分支, 而被迁移部分在公共仓库被不会被迁移, 会被保留, 造成重复混乱.

 - `git rebase <主分支> <特性分支>` 将共同祖先到特性分支的变化作为补丁, 以主分支为基础进行衍生. 该指令会先checkout到特性分支, 再进行衍合. 上面的命令是特性分支=HEAD的缩写.

 - `git rebase -onto <主分支> <上游> <特性分支>` 将特性分支到上游的变化作为补丁, 以主分支为基础进行衍生.  -onto是指明主分支点, 当三个branch时需要指明哪个是主分支. 另外, 主分支和上游不一定是branch, 任意有效的commit都可以.

5. #### [git cherry-pick](http://git-scm.com/docs/git-cherry-pick  ) 打某个commit的补丁, 不常用.

 - `git cherry-pick <commit>` 将commit的修正打到当前HEAD上.

- ###远程交互相关子命令



1. #### [git clone](http://git-scm.com/docs/git-clone)   克隆版本库 

 - `git clone https://github.com/jquery/jquery.git ` 克隆版本库. 可以后跟本地目录名. 支持多种协议.如http[s], git, ssh(user@host:/path),file,ftp[s],rsync等
 - `git clone -o hostname <主机地址>` 指定远程主机名,而不是默认origin

4. #### [git remote](http://git-scm.com/docs/git-remote )  管理远程主机名.(其实信息储存在本地并不与远程同步)

 - `git remote`列出所有主机名, 需要在git相应项目内才能用. 默认clone的主机是origin
 - `git remote -v` 参看主机网址.
 - `git remote show <主机名>` 查看主机详细信息,包括master与branch等.
 - `git remote add <主机名> <网址>`    添加远程主机, 尤其是在本地新建项目**没有克隆时**需要,新建时主机名一般为origin!
 - `git remote rm <主机名>` 删除远程主机
 - `git remote rename <原主机名> <新主机名>`   主机改名
 - `git remote prune 主机名` 可以将本地显示的不存在的远程主机删掉



3. #### [git fetch](http://git-scm.com/docs/git-fetch )    取回版本库更新(commit),同步更新远程主机/分支信息.

 - `git fetch`  更新远程索引

 - `git fetch <主机名> <分支名>`   不指定分支名则取回远程主机所有更新, 指定分支名则只取回分支更新. 但不合并到HEAD,只有用merge才合并









4. #### [git pull](http://git-scm.com/docs/git-pull )  取回主机某分支更新并与本地指定分支合并.相当于fetch+merge

 - `git pull <远程主机名> <远程分支名>:<本地分支名>` 取回分支内容并与本地分支合并. 
 - `git pull <远程主机名> <远程分支名>` 取回分支内容并与**当前分支**合并. 

5. #### [git push](http://git-scm.com/docs/git-push )  推送本地更新到远程主机

 - `git push <远程主机名> <本地分支名>:<远程分支名>` 将本地分支推送到远程分支.gitconfig里注册默认远程主机后可以省掉后面的.
 - `git push <远程主机名> <本地分支名>` 将本地分支推送到远程同名分支.
 - `git push <远程主机名> ::<远程分支名>`  将空白推送到远程分支, 即删除远程分支. 慎用.
 - `git push 远程主机名 --delete 远程分支名`: 删除远程分支,对于首选分支会报错. 可用`git branch show origin`查看分支情况
 - `git push origin :master`: 可以删除远程分支


错误master:
在.git/config里查看master指向另一个远程主机的master.此时checkout -b mmm origin/master 创建新分支,切换过去,然后 -D master删除旧的master分支,再 -b master origin/master, -D mmm 就好了.




-----

##配置文件

一般地使用`#` 为注释,支持标准glob模式匹配.

#### .gitignore 文件, 忽略跟踪某些文件. 

若要忽略本地库某些文件而非针对整个项目, 修改`.git/info/exclude`, 语法同.gitignore

~~~ 
# 此为注释 – 将被 Git 忽略

# 忽略所有 .a 或*.o 结尾的文件, 忽略所有~结尾文件(vim临时)

*.[ao]

*~

# 但 lib.a 除外. !为要忽略指定模式以外的文件或目录

!lib.a

# 仅仅忽略项目根目录下的 TODO 文件，不包括 subdir/TODO

/TODO

# 忽略 build/ 目录下的所有文件. 匹配模式最后跟反斜杠（/）说明要忽略的是目录。

build/

# 会忽略 doc/notes.txt 但不包括 doc/server/arch.txt

doc/*.txt

# ignore all .txt files in the doc/ directory

doc/**/*.txt
~~~

## Reference

1. [Git简明介绍](http://rogerdudler.github.io/git-guide/index.zh.html ) 
2. [Git Cheat Sheet](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf  ) PS: 注意简明介绍的checkout -- file 说明有误.
3. [Git Reference](http://gitref.org/index.html )
4. [Pro Git](http://git-scm.com/book/zh/v1  )
5. [蒋鑫的GotGitHub](http://www.worldhello.net/gotgithub/  )
6. [Git详解之一 Git起步](http://www.open-open.com/lib/view/open1328069609436.html )
7. [Git基础](http://www.open-open.com/lib/view/open1328069733264.html  )
8. [Git分支](http://www.open-open.com/lib/view/open1328069889514.html )
9. [分布式Git](http://www.open-open.com/lib/view/open1328070090108.html  )等一个系列
10. [MSYSGit项目](http://msysgit.github.io/  )
11. [Git笔记](http://blogread.cn/it/article/7296?f=wb  )




TODO: many thing to be completed, especially the picture.


---
