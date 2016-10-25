---
layout: post
title: Amber组氨酸HIS-HID-HIE-HIP问题
date: 2015-12-26 09:26:52
categories: CompCB
tags: CompCB MD
---

组氨酸是含有咪唑官能团的碱性氨基酸, 氨基酸上有两个可质子化位点, 另外还可以通过共振产生异构体.

根据质子化和状态和共振状态, 共有HID(离侧链近的带H)-HIE(离侧链远的带H)-HIP(两个N都带H)三种具体状态, 而一般所见HIS只是代表他是组氨酸, 但不确认具体异构体结构.

![](http://4.bp.blogspot.com/-RmyyiotHrZo/TbMKLXpRksI/AAAAAAAAAWU/Zt0ObNvpYzs/s1600/his01.png)

如果我们不用管质子化状态, 或者MD之前不进行氢原子网络优化, 可以让Amber自行加氢和处理. 但要是事先进行了质子化和氢键网络优化处理, 最好还是保持残基的质子化状态, 并且按规范命名.

我采用的是Schrodinger的蛋白处理系统进行复合物质子化和氢键网络优化. 但Schrodinger并的原子和残基命名策略和Amber进行MD不太一致, 所以要采用PDB2PQR再进行重命名.

在PDB2PQR中可以对残基进行根据策略命名, 例如使用Amber方法命名残基和原子. 但是在跑的时候发现, 我一个CHID没有正确命名而是保留了HIS的名字, 在Amber中则作为了CHIP, 从而导致H原子问题而报错.

以下脚本根据HID的 **HD1** 和HIE的 **HE2** 原子命名来重新判断残基命名. 可以对PDB2PQR的PQR结果进行再处理.

<script src="https://gist.github.com/platinhom/bcef539bd97bc192e231.js?file=HIS-HIE-HID-HIP-rename.py"></script>

使用就是脚本名+pdb/pqr文件名.

------
