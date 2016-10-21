---
layout: post_toc
title: Github相关总结
date: 1233-01-01 00:19:34
categories: IT
tags: Git
---

{::comment}
archive: true
> 本博文已合并到[Github相关总结](/1233/01/01/Github-related/#)中, 不再更新.
{:/comment}

本文将收录并重写和Github相关产品使用的博客并重新进行汇总. 一个艰巨的任务 =.=  
Git未来将再单独起一章汇总 =.=

> 一. Github和相关产品:

- [Gist介绍与用法](/2015/11/26/gist/){: target='_blank'}
- [Speaker Deck在线演示PPT文档](/2015/11/16/speakerdeck/){: target='_blank'}
- [Git大文件储存LFS (Git Large File Storage)](/2015/11/11/git-lfs/){: target='_blank'}
- [Github提交个人修改到开源项目](http://127.0.0.1:4000/2015/10/31/GithubPull/){: target='_blank'}
- [一个客户端拥有多个Github账号](/2015/11/17/diffAccount_Github/){: target='_blank'}

> 二. Github Page 搭建主页:

- [使用Github搭建博客](/2015/06/05/Build-Blog-Github/){: target='_blank'}
- [Project Page in Github Page](/2015/07/09/project-page-github/){: target='_blank'} , [页内](#l2-project-gh-pages)
- [Github Jekyll自定义404页面(MD方式)](/2015/07/09/404Page-Jekyll/){: target='_blank'} , [页内](#l2-404page)
- [将Github Page迁移到GitCafe Page](/2015/07/08/migrate-gitcafe/){: target='_blank'}

> 三. Markdown 撰写博客

- [Markdown 笔记](http://127.0.0.1:4000/2015/06/06/Markdown-note/){: target='_blank'} , [页内](#standard-markdown)
- [kramdown和markdown较大的差异比较](http://127.0.0.1:4000/2015/11/06/Kramdown-note/){: target='_blank'}, [页内](#kramdown-markdown)
- [Markdown中的代码块](http://127.0.0.1:4000/2015/07/10/fench-code-markdown/){: target='_blank'}
- [Pygments语法高亮](http://127.0.0.1:4000/2015/07/29/pygments-highlight/){: target='_blank'}

> 四. Github Page进阶---Jekyll:

- [Jekyll使用](/2015/07/27/Jekyll-usage/){: target='_blank'}
- [jekyll-window安装](/2015/07/30/jekyll-window/){: target='_blank'}
- [Liquid语言(jekyll所需)](/2015/11/28/Liquid-jekyll/){: target='_blank'}

> 五. Git 使用:

- [GIT命令总结](http://127.0.0.1:4000/2015/06/26/GIT-commands/){: target='_blank'}
- [GIT教程(ZZ自廖雪峰)](http://127.0.0.1:4000/2015/10/15/GitLearningExp/){: target='_blank'}

我是华丽丽滴分界线 ☺️

-------------------

# 一. Github和相关产品

## Github以及Github Page介绍

## Github社交

Github也提供了[Speaker Deck在线演示PPT/PDF文档](/1234/06/01/HTML-Language/#l3-speakerdeck)的服务, 方便用户进行交流学习. 通过将PPT转换为PDF后上传到Speaker Deck中, 就可以十分方便地获得嵌入代码, 从而在网页中展示你的报告.

## Gist介绍和应用

## Git大文件储存LFS (Git Large File Storage)

## Github类似产品: GitCafe和Gitlab

## 一个客户端拥有多个Git账号

# 二. Github Page 搭建主页

## 安装Git命令行工具

## 搭建初始化Github Page

## 套用模板

## 项目子页面 {#l2-project-gh-pages}

> 原博文: [Project Page in Github Page](/2015/07/09/project-page-github/){: target='_blank'}

It's very to create the web page for your new repository under your mainpage. Here, I record the procedure.

### Create a New Reposity

- You can easily create a new reposity in Github. At the left bottom corner of the main page of github, you can find your repositories. A "New reposity" button is there!
- Enter the name, describe your project, and choose whether create .gitingore file and license file. Then, create the new project.
- Copy the SSH address of your project, and `git clone git@github.com:username/projectname.git` clone the project with its address to local. It's not nessessary.

### Create a gh-pages branch
![](https://pages.github.com/images/create-branch@2x.png)

- The most easy way is to create the branch `gh-pages` online as the figure shown above. Enter the new name and github will remind you to create a new branch for it.
- You can also do that in command line by git: `git checkout --orphan gh-pages`, it will create a new branch without parent. If you want to create a blank branch only contains the project page, you can `git rm -rf .` to delete all the current files. I don't think it's nessesary indeed. It only need you to have a branch called `gh-pages`, that's enough. `git push -u origin gh-pages` to create your branch on remote.
- You can also change the default branch to gh-pages on repository setting. It will help you to change to gh-pages when you clone the repository.

### Create the page on gh-pages branch

- To create a simple index.html file online/on git is easy. But don't fancy.
- Use Jekyll! Yes, you can copy the jekyll needed files from your mainpage to the project page, such as _config.yml file, _layouts, _includes directory and even .gitignore CNAME 404.md files when you need. Because Jekyll need them to help you to convert markdown file to a page. If you don't copy these from your mainpage repository, the markdown file doesn't work at all!
- CSS/JS files don't need to be copied. Because the page can use them as its mainpage.
- Now you can visit `http://username.github.io/projectname` to visit the project page!

###### Reference
1. [Creating Project Pages manually](https://help.github.com/articles/creating-project-pages-manually/)
2. [GitCafe-Project Page](https://help.gitcafe.com/manuals/help/pages-services#为项目创建-pages-服务)

## 绑定网址

## 404页面 {#l2-404page}

> 原博文: [Github Jekyll自定义404页面(MD方式)](/2015/07/09/404Page-Jekyll/){: target='_blank'}

### Custom 404 Pages with Jekyll markdown style

-----

- It's very easy. Just create a file named `404.md` or `404.html` on the root directory of your homepage.
- Surely, we need to make it more interesting:

~~~markdown
---
title: 404
layout: page
---

<script language="JavaScript"> function myrefresh(){window.location="/";}setTimeout('myrefresh()',5000);</script>

## Error 404. Nothing was found :(   

How did you get to this link?

Please go to [homepage](/) or email me:

    zhaozxcpu@hotmail.com

## The page will redirect to the homepage after 5 seconds.....
~~~

- Here, I use my template "page" layout for it, similar to my homepage. 
- The javascript will refresh the 404 page after 5 second and redirect it to my homepage.
- You can change `window.location="/"` to `window.history.back()`, which could be back to the previous site.
- Below it's something you want to say~

Hey, see the result here: [My 404](http://platinhom.github.io/404)

Ref2 Yi Zeng also told you a method to create a 404.html page and use redirection in head of html. You can read it. But I recommand my method, it's easy and could retain you homepage style easily :)

###### Reference
1. [Custom 404 Pages](https://help.github.com/articles/custom-404-pages/)
2. [Create a custom Jekyll 404 page](http://yizeng.me/2013/05/26/create-a-custom-jekyll-404-page/)

# 三. Markdown 撰写博客

## 标准Markdown语言 {#standard-markdown}

> 原博文 [Markdown 笔记](http://127.0.0.1:4000/2015/06/06/Markdown-note/){: target='_blank'}

扩展名使用md/markdown，在为知当中使用md后缀命名笔记即可识别为markdown.

[英文维基](http://en.wikipedia.org/wiki/Markdown); [中文维基](http://zh.wikipedia.org/wiki/Markdown); [中文教程](http://wowubuntu.com/markdown/)
编辑器可参考: [知乎: 用Markdown 写作用什么文本编辑器？](http://www.zhihu.com/question/19637157)
Window 下软件: [MarkDownPad](http://markdownpad.com/), 
Mac 下软件: [Mou](http://25.io/mou/), ByWord
Online 软件: [Cmd Markdown](https://www.zybuluo.com/mdeditor), [StackEdit](https://stackedit.io/), [Raysnote](https://raysnote.com/). 
Chrome: [Markdown here](https://chrome.google.com/webstore/detail/markdown-here/elifhakcjgalahccnjkneoccemfahfoa), 

--- 


### 以下是一般的规则:
1. **特殊符号**：``#`_`` 等， 要在行头等特殊位置表达，可用转义符`\`， 一般符号后最好跟空格。
2. **强制换行**: 在行最后用两个空格并按下回车
3. **粗体和斜体**： 斜体用`*文字*` 或`_文字_`      粗体用`**文字**`   或` __文字__`   特别强调（粗斜体）用`***文字***` 或   `___文字___`
4. **分隔线**：用多于三个的`*`或者`-` 。
5. **标题**（html的head）：使用`#`作行开头，可以 1-6 个`#`，代表从大到小的六种标题规格，最多6个。若一段文字下一行为`====`或`--------`，该段文字自动处理为一级标题和2级标题。
6. **引用**： `>` 符号开头跟的内容
7. **无序列表**：使用 `-` 作行开头，子列表可以用制表符（tab）或四个空格来示意。 支持用`*` ,`-` 或者`+` 作标符。开头带空格可以作为下级列表.
8. **有序列表**：使用`1.    2.     3.  `等开头。`.`号后有空格.
9. **表格**：用 `|` 分隔，第二行可用 `|--------|:---------:| --------:|` 来分别指明是左对齐（默认），居中和右对齐，此时第一行会作为表头加粗居中。
10. **超链接**： `[显示文字](链接地址)`
11. **图片**： `![显示文字](链接地址)`
12. **代码**：在标准markdown里面支持四个空格或者tab开头自动进入代码块模式，但是这里要用  `` `文字` `` 作代码块. 在行代码内时, \` 需要用 \`\` 作外标.
在为知中根据不同代码不同标记，如下

~~~~~
```cpp  
代码内容
```
~~~~~  
注意: 在kramdown中使用\~ 而不是\` 作代码块. 另外, 长代码块(例如5个\` 优先于3个,可以利用该办法来表达.

### 使用HTML 方法
**字体颜色**：需要使用html方法 例如`<font color="red"> 文字 </font>`  
**居中对齐**: `<center>内容</center>`

### Kramdown
在Github中,旧版默认使用[maruku](http://maruku.rubyforge.org/markdown_syntax.html) 进行jekyll处理, 但由于停止更新, 现需要使用[kramdown](http://kramdown.gettalong.org/syntax.html) 来进行. 注意两者的差异.
- 语法块的下一行可以使用 `{: .language-ruby}` 来注明语言.当然也支持老式方法.

### 比较偏的用法:
- 内标签
`[显示内容][tag名]`
`[tag名]: 链接地址`

### cmd markdown : 网上MD的服务器
[简明语法](https://www.zybuluo.com/mdeditor?url=https://www.zybuluo.com/static/editor/md-help.markdown) ;
[高级语法](https://www.zybuluo.com/mdeditor?url=https://www.zybuluo.com/static/editor/md-help.markdown#cmd-markdown-高阶语法手册)

-  标签: 标签名1 标签名2    (用于归类, 也可用tags)
-  `[TOC]`        (内容目录结构)
-  `~~内容~~`       (删除线)
-  引用
`[^cite1]`    (插入位置,根据位置编号)
`[^cite1]`  : 内容    (对应内容,参考文献)
	
- 数学公式, 请参考[Mathjax](http://meta.math.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference)

~~~
$数学公式$  行内插入数学公式
$$ 数学公式 $$ 整行为一数学
~~~

- [流程图](http://adrai.github.io/flowchart.js/)

~~~
```flow  
内容  
```  
~~~

- 序列图 序列图语法参考. 

~~~
```seq  
内容  
```  
~~~

## 强大的改进版: Kramdown {#kramdown-markdown}

## 代码块与语法着色

# 四. Github Page进阶---Jekyll

## Jekyll介绍和本地化安装

## Jekyll使用

## Jekyll渲染器: Liquid

## Jekyll的插件

# 五. Git 使用



------