---
layout: post
title: Markdown链接括号的问题
date: 2015-12-24 10:34:05
categories: IT
tags: IDE
---

# Solution for Bracket in markdown link address.

Markdown创造一个链接或者图片是使用 `[title](link)` 和 `![title](link)`. 

我们可以避免`[]`内出现中括号, 或者使用转义. 

但是在小括号的链接里面就可能会出问题. 有些网址上面会具有小括号. 例如, 

<https://msdn.microsoft.com/zh-cn/library/ae5bf541(v=vs.100).aspx> 

如果使用转义, 打开链接时也会出现转义符, 所以网址出错.

例如: 

- 直接: [title](https://msdn.microsoft.com/zh-cn/library/ae5bf541(v=vs.100).aspx)  (居然正常显示?!只是在IDE里面有问题..不过还是不建议这样..)
- 使用转义: [title](https://msdn.microsoft.com/zh-cn/library/ae5bf541\(v=vs.100\).aspx)


解决方法: 

`%28` 代替`(`, `%29`代替`)` 主要是后者会歧义链接部分的结束. 这是使用url符号码去代替ascii的符号. 能够解决这个问题, enjoy it!

- url code: [title](https://msdn.microsoft.com/zh-cn/library/ae5bf541%28v=vs.100%29.aspx)

------
