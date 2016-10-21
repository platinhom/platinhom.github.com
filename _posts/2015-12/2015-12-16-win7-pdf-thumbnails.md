---
layout: post
title: win7下PDF显示缩略图thumbnails
date: 2015-12-16 06:50:01
categories: IT
tags: Software
---

Win7下很奇怪不能显示PDF文件的缩略图 **Thumbnails**. 预览倒是可以的. 原因是64-bit Window下PDF阅读器缩略图产生器的不兼容. Adobe貌似说由于安全问题不去理这个..于是就成了个千年问题..现在新版本的Adobe DC版还彻底移除了缩略图功能[^adobedcremove]..

试了一堆网上的方法, 最后终于成功了..小结一下吧..

### PDF preview for win 7

根据一个帖子讨论Adobe的预览问题[^preview], 里面提到使用[PDF preview for win 7](http://www.win7pdf.com/pdf-preview.html)这个软件. 这个软件能够一次解决掉预览和缩略图问题. 然而感觉有bug, 速度较卡, 而且多个pdf时缩略图产生爆慢, 还经常性导致explorer 挂掉重启...使用时还需要将该PDF阅读器设为默认才有效,否则还是不显示缩略图...这个软件看PDF打开非常快, 但是十分不方便, 非常不好用...不建议安装..

### Adobe\_Reader\_x64_fixes\_v3

很多帖子都提到这个[补丁](http://www.pretentiousname.com/adobe_pdf_x64_fix/). 用法很简单, 下载Installer版本下来然后安装. 安装完点Apply Fix即可. 然而在我的机子上尝试对于Adobe 依然不起鸟用.. 可能这个版本还是依然对于老的Adobe起效..补丁针对预览功能和缩略图功能, 据介绍要不是从Vista升级到Win7不会有预览的问题. 所以还是针对缩略图功能, 开发者针对的是Adobe 9,  但几年没有更新了..说2014年12月出更强大版本后来没一回事了.. ╮(╯▽╰)╭ 尝试折腾了几次依然无效, 所以也可以跳过了. 

### 结合Foxit

后来参考到一个[帖子](https://forums.adobe.com/thread/1812515?start=80&tstart=0), 里面介绍了解决办法:

1. 安装[sagethumbs](http://sourceforge.net/projects/sagethumbs/), 一个对图格式文件缩略图预览的程序. 还有一些图片处理功能. 不知道究竟有何神奇影响..照做罢了..
2. 安装Adobe Reader preview handler x64 fixer, 就是上面提及的补丁. 安装完后同上, 依然无效..
3. 安装[Foxit](https://www.foxitsoftware.com/). 下载新版本的Foxit. 原帖说要重启, 我没有重启..就是杀了explorer再开..╮(╯▽╰)╭ 
4. 设置Foxit为默认阅读器.此时就可以使用Foxit来进行缩略图了!!!速度还很快~
5. 重设Adobe为默认阅读器, 此时就发现用Adobe也可以预览缩略图了!!! 可能是Foxit提供了一些接口, Adobe可以借用这些借口来解决问题吧...

-------

好了, 回去把PDF Preview卸掉, 再试试卸掉Adobe Reader preview handler x64 fixer..

Good Luck~

[^adobedcremove]: [File preview thumbnails aren't working for Acrobat DC files in Windows Explorer](https://forums.adobe.com/thread/1812515)

[^preview]: [How to preview PDFs in Windows Explorer](http://www.pcworld.com/article/2082239/how-to-preview-pdfs-in-windows-explorer.html)


------
