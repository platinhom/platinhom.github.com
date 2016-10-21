---
layout: post
title: PaDEL分子描述符软件使用
date: 2015-08-06 14:29:10
categories: CompCB
tags: Software ChemInfo
---

PaDEL-descriptor是新加坡国立的Chun Wei Yap教授开发的分子描述符计算软件.Chun Wei Yap开发了一系列生物化学信息相关的程序PaDEL系列,这是其中分子描述符计算的程序.  
程序是基于JAVA的,并提供了源代码.整合了很多的分子描述符,现在包括1875(1444个1D&2D描述符和431个3D描述符)个描述符以及12种分子指纹,并且有图形界面,输出为csv表格,使用十分方便.这里仅作简介,详情参考Ref1, 相应文献参考Ref2.

包括的分子描述符及分子指纹参考[excel](http://www.yapcwsoft.com/dd/padeldescriptor/Descriptors.xls):  

<iframe src="https://sheet.zoho.com/view.do?url=http://www.yapcwsoft.com/dd/padeldescriptor/Descriptors.xls" style="width:800px; height:600px;" frameborder="0"></iframe>

## 使用:

1. [下载软件包](http://www.yapcwsoft.com/dd/padeldescriptor/PaDEL-Descriptor.zip),不建议下载[源码](http://www.yapcwsoft.com/dd/padeldescriptor/PaDEL-Descriptor_src.zip) 
2. 解压后,在装有JRE的情况下,直接双击`PaDEL-Descriptor.jar`
3. Molecules directory/file 中选择一个文件夹(找不到办法选择指定文件..把文件扔到某个文件夹吧..)
4. 指定输出文件csv格式.
5. General中选择1D&2D/3D/fingerprint进行计算,默认是2D描述符.旁边三个tab可以指定进行计算的具体fingerprint.
6. 点start开始计算

## Reference
1. [PaDEL-descriptor mainpage](http://www.yapcwsoft.com/dd/padeldescriptor/)
2. [PaDEL-descriptor: An open source software to calculate molecular descriptors and fingerprints](http://onlinelibrary.wiley.com/doi/10.1002/jcc.21707/abstract)

------
