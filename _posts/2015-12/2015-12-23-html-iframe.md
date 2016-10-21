---
layout: post
title: html:iframe嵌入框架
date: 2015-12-23 02:24:01
categories: Coding
tags: HTML Website
---


`<iframe src="嵌入目标连接" width="宽度" height="高度" frameborder="边框参数" scrolling="滚动条参数"></iframe>`

- 宽度和高度: 可以用'600px',可以用'100%'这样
- 边框参数: '0' 表示无边框, '1' 表示有边框
- 滚动条参数: 'yes' 表示有滚动条, 'no' 表示无滚动条, 'auto'表示自动根据内容判断

例如

`<iframe src="/2015/06/22/HTML-basic/" width="100%" height="600px" frameborder="1" scrolling="auto"></iframe>`

<iframe src="/2015/06/22/HTML-basic/" width="100%" height="600px" frameborder="1" scrolling="auto"></iframe>

如果边框内容内链接是 `<a href='链接' target='_parent'>`, 则连接会使整个网页跳转, 而不是框架内跳转. `_self`是框架内, `_blank`是新页面.

例如点击上面框架底部的W3School的连接(设置了\_parent) 和 HTML标签参考手册 的连接(设置了\_blank). 其他均会在框架内跳转.

------
