---
layout: post
title: Xshell使用公钥免密码登录
date: 2015-11-18 17:34:32
categories: IT
tags: Software
---

使用的是[Xmanger](https://www.netsarang.com/products/xme_overview.html)的Xshell和Xftp.

对于SSH登录, 很多时候使用账号名+密码, 将信息注册好就可以免密码瞬间登录了. 但是在SUSE系统或者使用Putty时, 不能用用户名+密码的方式登录, 这时就要使用公钥-私钥的方法免密码登录了.在[ConEMU-多tab Terminal的实现](/2015/09/19/ConEMU/)一文中就提及如何使用putty免密码登录. 其实原理都是一样的.

## 原理

- 服务器端(要访问的地方, 本来要输入用户名-密码的地方)保存公钥
- 在客户端(用户电脑)保存私钥

通过客户端的私钥和服务器端的公钥进行比较验证, 从而实现免密码登录.

## Xshell/Xftp的实现

- 在Xshell中, 菜单 `Tools -> User Key Generation Wizard` 打开产生公钥的窗口.
- `Key Type`选RSA, `Key length` 1024 bits (足够了), 然后Next
- 等待产生key pair. 很快就好了, 点Next
- User Key Information窗口, 输入`Key name`, 随意(可以区分就好了)..Passphrase是用key登录时输入的"密码", 不填写就是免密码登录. 这里不填写. Next.
- `Public Key Format` 选择SSH2 - OpenSSH. 下面的框中出现公钥. 全选后复制. 最后点Finish, 搞掂.
- 在菜单`Tools-User Keys Manager` 里面可以查看产生的公钥, 可以进行管理, 查看, 重新复制公钥等.

以上是公钥产生过程, OK后需要在服务器端保存公钥, 并且注册Xshell登录使用公钥方式.

- 登录你的服务器, 编辑`vim ~/.ssh/authorized_keys` 文件, 新加一行, 粘贴刚才复制的公钥 (忘记了可以在`Tools-User Keys Manager`重新查看).
- 点击Xshell 的 Session图标, 打开选择注册的登录信息, 右键选Properties, 修改登录信息(就是可以填写登录方法, 名称, 用户名密码一栏)
- 在Method中选择Public Key (原来是Password, 另外还可以Keyboard Interactive), 在下面出现User Key选择框, 下拉选择相应的刚才注册的公钥. 如果有Passphrase可以在下面注册. 也可以使用Browse来找保存下来的User Key文件.

好了,操作完后就可以直接使用公钥免密码登录了~~ xftp同样在登录session的属性修改登录方式即可. Enjoy it~

------
