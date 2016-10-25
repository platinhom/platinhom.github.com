---
layout: post
title: 使用Github搭建博客
date: 2015-06-05 13:06:56
categories: IT
tags: Git Website
---

- 简要介绍使用Github Page来制作静态网页作为主页
- Git使用
- Jekyll生成
- Markdown书写

------

### 安装git
- Window推荐使用[Msysgit](http://msysgit.github.io/),安装完毕直接使用命令行(bash)界面登入.注意msysgit和msys还是有区别的,例如前者`~`在我的文档.另外其原生的vim很弱(缺了很多插件)..可以去找官网的下载一些插件下来补充.
- Ubuntu可以直接`sudo apt-get install git`
- Mac我也忘了..
- 图形界面待补充...
- 更多Git命令介绍将在日后介绍

### 在github注册账号
1. **注册**: 到github注册账户[link](https://github.com/)
2. **创建密钥**: 使用`ssh-keygen -t rsa -b 4096 -C "yourmail@hotmail.com"` 来创建公有私有密钥,使用默认的地址,若不输入passphrase则可以跳过每次输入密码(建议passphrase为空).然后复制公钥`~/.ssh/id_rsa.pub`的内容,在github账号中`Settings`,`SSH keys`中黏贴该密钥. 更多ssh key产生和处理请参考[github sshkey generation](https://help.github.com/articles/generating-ssh-keys/),[中文ssh key 介绍](https://wiki.archlinux.org/index.php/SSH_Keys_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\) )
3. **本地库**: 创建一个文件夹如MyGit,`mkdir MyGit`, 然后进去`git init`创建空的本地库(加入`.git`文件夹), 若之前没有设置过,还需要`git config --global user.name "yourname"`以及`git config --global user.email "yourmail@email.com"`来注册基本信息.

### Github上创建博客
- 在Github创建新的Repository[New Repository](https://github.com/new). 在Github主页右下角一般显示了你当前库数量.
- 创建Project Name为`name.github.com`这里name随意,一般使用账号名.主页可不填. 项目不付费只能公开.随后`Create Repository`,页面给出提示,可忽略之.
- Github可以提供一个`<user-id>.github.io`的主页给用户,可以将该主页和我们创建的主页用的库进行绑定.每个项目也可以使用项目主页,此时要新建一个分支`gh-pages`,此时项目的内容可以在`<user-id>.github.io/<project-name>`访问到. 更详细请参考[建立主页](http://www.worldhello.net/gotgithub/03-project-hosting/050-homepage.html#user-homepage)
- `CNAME`文件可以保存映射主页名.
- 更多关于使用Pages创建博客信息可以参考[Github Pages](https://pages.github.com/),包括连接主页名,help等.


### 将项目拉到本地,并修改
1. **库地址**: 在Github中,打开自己的主页项目如`https://github.com/name/name.github.com`,在右下clone URL处选择`SSH`并点图标进行复制
2. **克隆库**在本地需要放置网页的库(文件夹内),克隆远程项目到本地(这里使用ssh协议,所以请确保上述ssh key已正常可用).使用命令来克隆内容到本地(提示是否登录,yes).`git clone git@github.com:name/name.github.com.git`. 很长的地址直接用刚才复制的内容黏贴.
3. **创别名**(非必要): `git remote add myhomepage git@github.com:name/name.github.com.git`可以创建别名为`myhomepage`来代替之前复制那段地址, 可用`git remote rm myhomepage`来删除别名
4. **说明文件**(非必要): `touch readme.md` 创建库的说明文件,编辑内容可在github网页中看到.
5. **主页文件**: 可以自行将主页内容拉到此处,使用 index.html 作主页文件,可以创建或编辑该文件. 也可以使用github的自动生成器来生成个基础模板.
6. **提交修改**: 修改后,使用`git add -A`来将所有修改递交到本地暂存库,再用`git commit -am "your comments"`提交修改到本地库,然后用`git push origin master`将本地库更新提交到远程库, 这里origin可以用之前的myhomepage名替换.OK.
7. 此时已经成功创建主页.简要使用git命令请参考[Git简明指南](http://rogerdudler.github.io/git-guide/index.zh.html),更详细的Git使用请参看[GotGitHub](http://www.worldhello.net/gotgithub/)
8. 可以使用一些Jekyll的主页模板来快速设置你的主页啦! [jekyll主页模板](https://github.com/jekyll/jekyll/wiki/Sites)

### 可以使用Jekyll来构建(非必要)

- **安装Jekyll**:首先需要使用gem,gem是ruby安装后配套产生的. [下载ruby](http://rubyinstaller.org/downloads/)
可以使用 `gem update --system` 来升级gem
在命令行中 `gem install jekyll` 进行安装
- [Github官方介绍使用](https://help.github.com/articles/using-jekyll-with-pages/); [Jekyll中文官方介绍](http://jekyllcn.com/)和[英文介绍](http://jekyllrb.com/)
- **配置文件**: 修改`_config.yml`: 其中source和destination是源文件目录以及生成`_site`网页目录,markdown和highlighter定义语法高亮及着色使用的方法.
- **网页模板**: `_layout`内的为网页模板,一般含有一个主界面一个博文的模板.
- **本地生成**: 直接`jekyll build` 来生成本地的html文件. 其实只是做网页的话,可以不装jekyll.

### 撰写博文

##### 此处推荐使用Markdown格式,更多请网上参考.在Mac可使用Mou来写. 但可惜Mou对Kramdown不咋滴.

- 在`_post`中添加相应博文文件,格式使用`YYYY-MM-DD-name.md/markdown/html`,并需要在文件开头添加一些话,如下:

~~~~
---
layout: post
title: 使用Github搭建博客
date: 2015-06-02 11:06:56
category: Github
tags: Github
---
~~~~

PS: 每项如layout和内容间要留空格!

- `layout`:是使用的模板,在`_layout`文件夹内定义,这里用的是`post.html`
- `title`:是文章显示的一级标题.但是网页地址显示的是文件的名不是这里.
- `date`:是文章的发表日期时间,遵照我显示的格式,一般是`"%Y-%m-%d %H:%M:%S"`.注意Jekyll计算时间是按GMT标准时间来计算的,否则博文显示时间会和博客设置的时区不同.
- `category`或`categories`:文章分类,随意.
- `tags`: 文章标签,可以用多个标签.
- `comment`: true/false,可以相应开启/关闭评论.

- GitHub 使用一种被称为“GitHub 风格的 Markdown 语法”（ [GFM](https://help.github.com/articles/github-flavored-markdown/) ）来书写版本注释、Issue 和评论。它和标准 Markdown 语法（SM）相比，存在一些值得注意的差异，并且增加了一些额外功能。默认GFM使用[maruku](http://maruku.rubyforge.org/markdown_syntax.html),也可以用Jekyll来应用[kramdown](http://kramdown.gettalong.org/syntax.html).(注意:kramdown的语法块使用`~~~`来代替`---`)以及[rdiscount](http://tedwise.com/markdown/)等.语法高亮可以用pygments.

- 避免产生bug和冲突.请阅读一些注意事项[Page构建失败](https://help.github.com/articles/troubleshooting-github-pages-build-failures/). 其中,例如避免两文章时间完全一致,避免文章中有语法错误(尤其markdown)等比较重要.

### 更多功能
- **评论**: 推荐使用国内的duoshuo[介绍](http://wenva.github.io/%E6%8A%80%E5%B7%A7/2015/04/29/%E4%B8%BA%E5%8D%9A%E5%AE%A2%E6%B7%BB%E5%8A%A0%E5%A4%9A%E8%AF%B4%E8%AF%84%E8%AE%BA.html)或者[disqus](https://disqus.com/)
- 分类
- 搜索栏
- 友情链接: 就是新建个页面或者新建个div放链接罢了
- 网站统计: 静态网页简单统计使用第三方的[不蒜子](http://ibruce.info/2015/04/04/busuanzi/),也可以用google,百度一类统计.

##### Other Reference
1. [基础教程网-TeliuTe](http://teliute.org/mix/Tegit/lesson1/lesson1.html)
2. [Github Page极简教程](http://yanping.me/cn/blog/2012/03/18/github-pages-step-by-step)
3. [Jekyll介绍](https://github.com/toolchainX/emacs_config/blob/master/Notes/Jekyll.org)

