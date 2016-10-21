---
layout: post
title: 一个客户端拥有多个Github账号
date: 2015-11-16 17:17:56
categories: IT
tags: Git
---

例如我有两个Github账号, 叫GHA和GHB. 分别邮箱GHA@163.com, GHB@163.com. 其中GHA是我主要使用的账号. GHB是新账号. 如果问题换成了我在Github/Gitcafe/Gitlab上有相同的账号(使用相同的账号名, 相同的邮箱), 那就将正常的公钥复制到不同的服务器端就好了, 木有这种不同账号的问题. 

## 公钥和私钥

在Github里面没法一个ssh的公钥放在两个账号, 所以对于GHB的公钥, 你没办法用之前的. 再说, GHA的公钥包含的邮箱也不适合GHB使用. 所以要新创建一个公钥用于GHB

`ssh-keygen -t rsa -b 4096 -C "GHB@163.com"`{: .language-bash}

创建新公钥, 第一个提示会问保存的公钥地方, 默认是`~/.ssh/id_rsa`.如果你直接enter, 会再询问你是否覆盖. 此时会覆盖掉旧的私钥公钥组合! 这里例如创建新私钥为`~/.ssh/id_rsa2`,对应公钥就是`~/.ssh/id_rsa2.pub`. 保存的私钥名也可以通过`-f "~/.ssh/id_rsa2"`选项来指定. 随后将公钥2放到GHB的账号里. 这是第一步. 

## 设置仓库repository的user信息

默认情况, git提交时使用的是global的`user.name`和`user.email` 信息. 显然, 这里两个账号不可能用同一个global信息 (global信息在`~/.gitconfig`中有). 此时可以设置单独的仓库的信息. 单独的仓库信息在仓库文件夹的`.git/config`文件内. 因为global信息对应GHA的, 所以我就不加设置了, 直接在GHB仓库内设置: `git config --local user.name "GHB"; git config --local user.email "GHB@163.com"`. 这样就OK了. 查看设置信息`git config --list`, 可能有两套user.*, 下面的(local)会覆盖上面的(global). `--local`设置单独仓库信息, 比global优先. 不设定`--global`使用的config默认是`--local`的.

有网上别的说法是, 每个仓库都单独设置, 因为我global信息对应了太多的仓库, 所以我就不这样做了, 有兴趣可以自己尝试:

~~~bash
# 取消global设置
git config --global --unset user.name
git config --global --unset user.email

# 设置每个项目repo的自己的user.email
cd ~/repo_A
git config  user.email "GHA@GHA.com"
git config  user.name "GHA"
cd ~/repo_B
git config  user.email "GHB@GHB.com"
git config  user.name "GHB"
~~~

## 交换通讯私钥

这是最暴力的方法.

如果在上面生成公钥和设置仓库user信息都完成后, 进行提交, 会报错: 

~~~
ERROR: Permission to GHB/GHBtest.git denied to GHA.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
~~~

虽然设置了repo信息, 但是我们提交使用的依然是默认的id_rsa私钥, 其对应的依然是GHA的账号. 最简单暴力的方法, 就是将默认的私钥/公钥换成我所需要提交的. 下面的脚本就可以完成.

~~~bash
#! /bin/bash

prefix="$1"
if [ -z $1 ];then
	prefix="id_rsa2"
fi

mv ~/.ssh/$prefix ~/.ssh/${prefix}_tmp
mv ~/.ssh/${prefix}.pub ~/.ssh/${prefix}_tmp.pub
mv ~/.ssh/id_rsa ~/.ssh/$prefix
mv ~/.ssh/id_rsa.pub ~/.ssh/${prefix}.pub
mv ~/.ssh/${prefix}_tmp ~/.ssh/id_rsa
mv ~/.ssh/${prefix}_tmp.pub ~/.ssh/id_rsa.pub
~~~

使用一个参数, 默认参数1是id\_rsa2. 也就是把id\_rsa[.pub]和 id\_rsa2[.pub] 互换. 执行一次该脚本后, 再进行正常的提交, 即可完成所需. 可以将该脚本放在GHB的仓库内, 需要时执行. 

**切记**: 使用完该脚本后, 再次运行一次, 将私钥和公钥换回默认的!!!

## 修改host信息

这个方法不需要经常交替私钥/公钥文件, 但操作比较麻烦. 原理就是修改新的host, 其hostname指向指定host(例如github.com), 而验证文件则自己指定.

~~~bash
touch ~/.ssh/config #创建一个ssh时信息注册文件, host信息可以从里面解析. 其实有下面一步就不用touch了
echo "# default
Host github.com
HostName github.com
User git
IdentityFile ~/.ssh/id_rsa

# two
Host two.github.com  # 前缀名可以任意设置
HostName github.com
User git
IdentityFile ~/.ssh/id_rsa2
" > ~/.ssh/config 
# 将host信息写入到注册文件, 这里随你怎么搞啦

# 测试连接是否良好
ssh -T git@github.com        # 测试GHA 私钥ssh连接
#Hi ***! You've successfully authenticated, but GitHub does not provide shell access.
ssh -T git@two.github.com    # 测试GHB 私钥ssh连接
#Hi ***! You've successfully authenticated, but GitHub does not provide shell access.

# 去到GHB仓库, 这个地址根据自己需要
cd ~/GHB 

# 查看远程仓库信息
git remote -v
#origin  git@github.com:GHB/GHBtest.git (fetch)
#origin  git@github.com:GHB/GHBtest.git (push)

# 修改远程仓库地址!
# 就是修改上面origin的@github.com部分换成@two.github.com
git remote set-url origin git@two.github.com:GHB/GHBtest.git
~~~

其实就是关键设置`.ssh/config`和`git remote set-url origin 新地址`的两关键步骤了.

## Reference

1. [一个客户端设置多个github账号](http://tmyam.github.io/blog/2014/05/07/duo-githubzhang-hu-she-zhi/)
2. [Gist-同一台电脑多Github账号](https://gist.github.com/suziewong/4378434)
3. [git生成ssh key及本地解决多个ssh key的问题](http://riny.net/2014/git-ssh-key/)
4. [Git 常用命令详解（二）](http://blog.csdn.net/ithomer/article/details/7529022)

------
