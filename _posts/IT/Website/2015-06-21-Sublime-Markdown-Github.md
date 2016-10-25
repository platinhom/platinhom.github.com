---
layout: post
title: Sublime-Markdown-Github联合使用
date: 2015-06-21 05:54:45
categories: IT
tags: Website Git IDE
---

今天测试了使用Sublime来代替Mou进行Markdown的编写,并接合Github使用.很爽! 

使用Github可参考Ref1, 使用Markdown语法可参考Ref2, 安装Sublime2/3请参考Ref3. 都是之前写的三篇博客.这里只挑重点简要介绍.

### 准备条件

- 注册并使用Github, 并且已经完成自己的Github Pages.
- 安装好Sublime2/3, 并且安装好Package Control. 设置好命令行快速打开sublime,如`sl`命令来打开.
- 具备命令行,可以利用命令行执行Git操作.

### Sublime需要的插件:

- [Markdown Extended](https://packagecontrol.io/packages/Markdown%20Extended): 扩展的markdown着色,支持GFM的代码块,可以在代码块中根据标示来着色,甚至可以对行末空格着色.
- [Monokai Extender](https://packagecontrol.io/packages/Monokai%20Extended): 使用md时必须的着色工具,在`Color Scheme`中设置即可,推荐使用 `Monokai Extended Bright` 策略.
- [Markdown Preview](https://packagecontrol.io/packages/MarkdownEditing): 支持将md文件编译,并用浏览器浏览,使用参看[ref](http://www.jianshu.com/p/378338f10263),主要是需要加入`{ "keys": ["ctrl+alt+m"], "command": "markdown_preview", "args": { "target": "browser"} }`这么一段代码到Key-binding-user(不是markdown preview里面的setting!).我设了快捷键`super+ctrl+m`.
- [Terminal](https://packagecontrol.io/packages/Terminal): 可以方便地在文件中调出命令行. 可以右键文件来调用, 也可以`cmd+shift+T`. 可配置iTerm.

### 利用Project:
Project就是当前工作状态. 可以储存很多和当前工作相关信息, 可以将相关文件加入到project. 利用这个特性,我们可以用于快速博文搜索, 快速打开之前的编辑状态. 

- 先使用`Add folder to project`功能,将自己主页的文件夹加入到project.可用快捷键`cmd+K,cmd+B`组合来调出左边工具栏查看加入情况.
- 可以保存project`Save Project As`到`sublime-project`文件,里面包括文件夹信息,配置等.另外还有`sublime-workspace`文件,里面记录了更多缓冲细节信息,包括正在编辑文件信息. 不推荐保存到主页文件夹内,推荐在外一层位置,不提交到Github.
- 可以关闭project(`Close Project`,会自动保存信息)再打开(`Quick Switch Project`,`Ctrl+Cmd+P`).此时之前编辑的文件及设置又出现了.
- 可以利用`cmd+P`快速搜索project内文件.
- 可以`Edit Project`,添加配置信息.例如`"settings"`,`"build_systems"`.可以在此自行新建相应的build的信息(会出现在build里).

这里我的project设置为:

~~~ javascript
{
	"folders":
	[
		{
			"path": "/Users/Hom/MyGit/Homepage/platinhom.github.com"
		}
	],
	"build_systems":
    [
        {
            "name": "submitGIT",
            "cmd": ["/Users/Hom/MyGit/Homepage/platinhom.github.com/submit.sh"]
        }
    ]
}
~~~
这里的`submit.sh`是我提交更改到服务器的脚本.设置好`build_systems`后,`cmd+b`可以进行选择`submitGIT`,然后就快速提交了.当然,你要设置好本地的Git提交任务到Github的设置(最好无密码提交).

~~~ bash
#! /bin/bash
# file: submit.sh

git add -A
git commit -am "regular"
git push origin master
~~~

- 对于Window系统,就不太友善了.Terminal默认是PowerShell.我们使用MSYSGit的bash来实现自动Build. 此时, Project 设置文件为:

~~~ javascript
{
	"folders":
	[
		{
			"path": "platinhom.github.com"
		}
	],
		"build_systems":
    [
        {
            "name": "submitGIT",
            "cmd": ["C:\\Program Files (x86)\\Git\\bin\\sh.exe", "--login", "-i","C:\\Users\\Hom\\Desktop\\MyGit\\platinhom\\platinhom.github.com\\submit.sh"]
        }
    ]
}
~~~
其中, --login 和 -i分别两个选项用来登入, 后面是submit脚本的绝对路径.搞掂~


### 撰写博文
- `cmd+shift+t` 调出命令行,或者在左侧side bar右键一个文件,`open terminal here`.
- `./newblog.sh myblog category tag1 tag2` 的命令快速创建新日志文件.
- 可以用sublime打开新日志文件.脚本中直接使用`sl`来打开. 可以根据自己喜好

###### FILE: [newblog.sh](/scripts/newblog.sh)

~~~ bash
#! /bin/bash
# file: newblog.sh
# Author: PlatinHom
# Last: 2015-06-21

# Full Usage: "./newblog.sh title category tag1 tag2"
# Simple Usage without category and tag: ".newblog/.sh title"

# You can register your sublime here. It's not nessary.
sublimecmd="/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl"

title=$1
category=$2
tag="${@:3}"

if [ -z $1 ];then
title="TempTitle-`date +%H%M%S`"
fi

if [ -z $2 ];then
category="Other"
fi

if [ -z $3 ];then
tag="Other"
fi

# My blog use GMT+8:00 time zone-China
# For MacOS
if [ `uname -s` == "Darwin" ];then
	today=`date -u -v "+8H" +"%Y-%m-%d"`
# Other OS
else
	today=`date -u -d "+8 hour" +"%Y-%m-%d"`
fi

# In github's jekyll,you should enter GMT time (time zone UTC(+0:00))
nowGMT=`date -u +"%Y-%m-%d %H:%M:%S"`
 
touch _posts/"${today}-${title}.md"
echo "---" >>_posts/"${today}-${title}.md"
echo "layout: post" >>_posts/"${today}-${title}.md"
echo "title: $title" >>_posts/"${today}-${title}.md"
echo "date: $nowGMT" >>_posts/"${today}-${title}.md"
echo "categories: $category" >>_posts/"${today}-${title}.md"
echo "tags: $tag" >>_posts/"${today}-${title}.md"
echo "---" >>_posts/"${today}-${title}.md"
echo "" >>_posts/"${today}-${title}.md"
echo "" >>_posts/"${today}-${title}.md"
echo "---" >>_posts/"${today}-${title}.md"

# Open the new blog by sublime.
# You can modify the program as you like.
if $(which sl);then
	sl _posts/"${today}-${title}.md" &
elif [ -x "$sublimecmd" ];then
	"$sublimecmd" _posts/"${today}-${title}.md" &
fi
~~~

这里也提供一个python脚本用于实现上述功能,可以用于Window系统(PS:先要环境里能自动运行python). 这里需要先设置好你`_post`文件夹的路径. 该脚本还提供相应函数,可以加载后使用函数调用.


###### FILE: [pynewblog.py](/scripts/pynewblog.py)

~~~ python
#! /usr/bin/env python
# -*- coding: utf8 -*-

# file: pynewblog.py
# Author: Hom, Date: 2015.6.22
# A easy script to create new blog for Github with Jekyll
# Usage as: python pynewblog.py title [category tags]

import time,os,sys

# Here, you should assign the _post directory for creating blogs 
wd="C:\\Users\\Hom\\Desktop\\MyGit\\platinhom\\platinhom.github.com\\_posts"
#pwd="."

def newblog(title="Template",category="Other",*args):
	title=str(title);
	category=str(category);
	tags="Other"
	if (len(args)>0):
			tags=" ".join(str(args).strip("(',)").split(", '"));
			tags=tags.replace("'","");
	
	# Change to work directory
	nowwd=os.getcwd()
	os.chdir(wd)

	# Jekyll use GM time in blog time, I use GM+8 time in title.
	gmnow=time.gmtime();
	gm8now=time.localtime(time.mktime(gmnow)+8*3600.0);

	gmstr=time.strftime("%Y-%m-%d %H:%M:%S",gmnow)
	gm8str=time.strftime("%Y-%m-%d",gm8now)

		# create the new blog
	f=open(gm8str+"-"+title+".md",'w');
	f.write("---\nlayout: post\ntitle: "+title+"\ndate: "+gmstr+"\ncategories: "+category+"\ntags: "+tags+"\n---\n\n---")
	f.close()

	os.chdir(nowwd)
	
if (__name__ == '__main__'):
	# Setup template information
	title="Template"
	category="Other"
	tags="Other"

	# Get the parameters
	argc=len(sys.argv)
	if (argc>1):
		title=sys.argv[1];
		if (argc>2):
			category=sys.argv[2];
			if (argc>3):
				tags=" ".join(sys.argv[3:])
	newblog(title,category,tags);
#end main
~~~

## Reference
1. [使用Github搭建博客](http://platinhom.github.io/2015/06/05/Build-Blog-Github/)
2. [Markdown 笔记](http://platinhom.github.io/2015/06/06/Markdown-note/)
3. [Sublime2&3 基础使用](http://platinhom.github.io/2015/06/21/sublime-usage/)

---
