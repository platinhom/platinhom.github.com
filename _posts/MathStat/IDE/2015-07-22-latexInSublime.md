---
layout: post
title: Latex in Sublime
date: 2015-07-21 16:53:49
categories: MathStat
tags: IDE Software
---



基础使用sublime以及安装Package Control请参考[Ref1](http://platinhom.github.io/2015/06/21/sublime-usage/). 直接进入正题.

## 安装

- 安装[MacTex](https://tug.org/mactex/),这是Mac里面的MacTex解释版. 装最简单的,使用[简化基础版即可](https://tug.org/mactex/morepackages.html).

- 安装[Skim](http://sourceforge.net/projects/skim-app/?source=directory), 一个PDF阅读器. 安装后打开，进入选项设置——同步，在PDF-Tex同步支持那里选择自定义，选择sublime相应版本。这样，当你在Sublime Text里修改tex文件时，Skim预览也会相应变更.如果装了sidebar增强,可以右键open with-Edit Application来编辑参数文件.加入下面这段子项到children{}里面,然后就可以打开了.

~~~
{
	"caption": "Skim",
	"id": "side-bar-files-open-with-skim",

	"command": "side_bar_files_open_with",
	"args": {
						"paths": [],
						"application": "Skim.app", // OSX
						"extensions":"pdf",  //any file with these extensions
						"args":[]
					},
	"open_automatically" : true // will close the view/tab and launch the application
},
~~~

- cmd+shift+p 调开命令行. 输入PCI找到Package Control Install, 输入`LaTexTools` 找到包后双击或确定即可安装.

- 新建一个tex结尾的文件,例如test.tex, 然后编辑. 输入一些内容, 然后 sublime的-Tools->Build System->选择LaTex. 随后cmd+B编译即可.随后用skim打开.

## 使用

- cmd+l,delete 连续快捷键, 将临时文件删除(注意英文输入法..)

[latex在线编辑器](http://www.codecogs.com/latex/eqneditor.php)

## Reference
1. [Sublime2&3 基础使用](http://platinhom.github.io/2015/06/21/sublime-usage/)
2. [LaTexTools](https://github.com/SublimeText/LaTeXTools)
3. [Making your first PDF with LaTeX and Sublime Text 2 for Mac](http://economistry.com/2013/01/installing-and-using-latex-for-mac/)
4. [部署MAC上的Sublime Text+LaTex中文环境](http://www.readern.com/sublime-text-latex-chinese-under-mac.html)


------
