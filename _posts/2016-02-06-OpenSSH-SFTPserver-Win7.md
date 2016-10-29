---
layout: post
title: Win7下OpenSSH搭建SFTPserver
date: 2016-02-05 22:18:40
categories: IT
tags: Internet Software
---

可以仔细阅读WinSCP上面的官方教程[Installing SFTP/SSH Server on Windows using OpenSSH](https://winscp.net/eng/docs/guide_windows_openssh_server)

## 设置步骤: 

1. 下载带sshd的套件: [下载地址](https://github.com/PowerShell/Win32-OpenSSH/releases/), 可以下64bit或者32bit的, 靠稳就32吧.
2. 解压缩下载的压缩包, 例如解压到`C:\Software\OpenSSH-Win64`
3. 跑到 `C:\Windows\System32`, 找到cmd.exe, 右键, 管理员运行(Run As Administrator). 跑到解压的文件夹, `cd C:\Software\OpenSSH-Win64`
4. 运行命令, 产生服务器 server key: `ssh-keygen.exe -A`
5. 开启防火墙进入的22端口: 打开控制面板, 打开防火墙, 高级设置(Advanced Settings), 选择左边的`Inbound Rules`, 右边选择`New Rules` (第一次时), 弹出个窗口, 选择`Rule Type`为`Port`, 下一步, 选择`TCP`协议, 指定端口`22`, 下一步, 允许连接(第一个, `Allow the connection`), 下一步选择所有域, 好了, 最后起个名字`SSH`, 描述随意. 这一步也可以在Win8以上在刚才的命令行里输入: `New-NetFirewallRule -Protocol TCP -LocalPort 22 -Direction Inbound -Action Allow -DisplayName SSH`. Win7经测不可以.
6. 设置LSA: 继续在刚才的cmd 命令行, 输入 `.\setup-ssh-lsa.cmd` 
7. 重启电脑
8. 重复第三步, **管理员权限** 打开cmd 命令行窗口, 跑到OpenSSH的文件夹.
9. `explorer .` 一下可以打开文件夹窗口, 找个编辑器编辑其中的`sshd_config`文件, 更改两个地方 (主要是指定路径, 这里复制自己的OpenSSH路径):
	- `Subsystem	sftp	C:\Software\OpenSSH-Win64\sftp-server.exe`
	- `Subsystem	scp	C:\Software\OpenSSH-Win64\scp.exe`
10. 安装底层运行的sshd 服务: cmd命令行管理员权限: `sshd.exe install`
11. 开启SSHD服务: 控制面板, 管理工具 (*Administrative Tools*), 服务(*Services*), 往下拉找到 SSHD 服务, 右键, 开启服务. 要是每次开机都想自己启动, 右键->属性-> `Startup Type`-> `Automatic` 
12. 至此, 搞掂. 教材后面的东东不是必须的.

## 登录

- 先要知道自己主机端IP: 打开cmd命令行窗口, `ipconfig`, 找到ipv4地址
- 直接找台有ssh的电脑, 例如linux/mac/mingw都可以. `ssh 用户名@你的IP`. 提示是否保存机子, `yes` 回车. 然后输入密码
- 登录后, 会变成cmd的命令行式样, 比较丑不好用 退格键怪怪的... 稍后再研究怎么用Mingw代替..至此成功登入!~
- 免密码登录:
	- 客户端产生公钥和私钥对. 可以参考以前写的[Putty免密码登录部分](/2015/09/20/ConEMU/)
	- 这边主机端, 弄一个`authorized_keys` 文件(服务器端存运行key的). 打开`C:\Users\用户名\.ssh` 文件夹(没有就创建一个这样的文件夹). 新建一个 `authorized_keys`. 然后写入要登入的机器的公钥pub key (`id_rsa.pub`), 最好复制过来, 例如`scp ~/.ssh/id_rsa.pub 用户名@主机IP:id_rsa.pub`, 然后到`C:\Users\用户名\`下面编辑这个文件, 将内容复制到`authorized_keys`里面, 保存.
	- 再次在客户端用`ssh 用户名@你的IP`, 这次直接就该登上去不用密码了~

---------

- `sshd.exe` 是底层背景运行提供SSH服务的程序, 如果要关掉, 任务管理杀掉就可以了.
- 如果要关闭开机sshd服务, 在设置步骤中第11步, 将服务属性改掉就OK了

------
