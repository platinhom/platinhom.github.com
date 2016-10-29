---
layout: post
title: Gaussian遇到错误汇总
date: 2015-09-05 10:03:42
categories: CompCB
tags: CompChem Gaussian
---

- 权限问题

~~~bash
Files in the Gaussian directory are world accessible.
~~~

权限太高, 在高斯文件夹内,输入chmod -R 750  * 即可.

- 经典写入错误

~~~bash
Erroneous write during file extend. write -1 instead of 4096
Probably out of disk space.
Write error in NtrExt1: Bad address
Segmentation fault
~~~

解决办法：
sudo echo 0 > /proc/sys/kernel/randomize\_va\_spac

- IRC计算L123错误

~~~bash
Maximum number of corrector steps exceded.
Error termination via Lnk1e in /mnt/home/zhaozx/g09/l123.exe
~~~
**解决**: 增大irc(maxcycle=400), 默认20到了.



- 优化计算L502错误不收敛

~~~bash
Convergence failure -- run terminated.
Error termination via Lnk1e in /mnt/home/zhaozx/g09/l502.exe 
~~~

**解决**: 增大scf(maxcycle=500)或者加入SCF(QC)

- 优化结构时l103内坐标系统错误

~~~bash
Error in internal coordinate system.
Error termination via Lnk1e in /mnt/home/zhaozx/g09/l103.exe
~~~

**解决**: 有说增加opt=Cartesian能解决..
- 优化计算L508的SCF不收敛

~~~bash
Search did not lower the energy significantly.
No lower point found -- run aborted.
Error termination via Lnk1e in /mnt/home/zhaozx/g09/l508.exe
~~~
**解决**: 难解. SCF使用QC时不收敛产生,SCF不收敛主要由于结构不合理. 可以用小基组方法先进行计算, 优化结构后再进行进一步优化. 还有什么SCF=XQC/Int(Grid=Ultrafine)/SCF=fermi/scf=noincfock/SCF=VSHIFT=150

------
