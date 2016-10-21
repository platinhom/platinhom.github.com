---
layout: post
title: jekyll-window安装
date: 2015-07-29 16:05:09
categories: IT
tags: Website Git
---

之前window安装一直没成功...今天再尝试一下,终于弄好了. Thanks to  Julian Thilo! (Ref1)

- 安装[Ruby](http://rubyinstaller.org/downloads/).注意mingw的版本,要是32位版本,即使是64位系统也要下32位版本(就是没有x64的). 默认安装后ruby的路径会加入到环境变量(安装时有勾选),即可以直接运行.当然, 没有的话自己设置一下.

- 安装[Gem](https://rubygems.org/pages/download) Gem是Ruby里的软件包管理器,类似于python的PIP.下载后解压,`ruby setup.rb` 就可以了.根据教程貌似不用安装,但安装jekyll时需要gem命令,不知道ruby是否自带(更新: 经再次安装,发现是自带的).我之前装过了.

- 安装[DevKit](http://rubyinstaller.org/downloads/). `ruby -v` 查看ruby版本,注意后面是i386还是x64位.前者的话下载(DevKit-mingw64-32-\*-sfx.exe).也要根据你的ruby版本选择啦.双击可执行文件,指定一个解压路径,例如解压到 *C:\Software\RubyDevKit* .进入该文件夹,运行命令`ruby dk.rb init;ruby dk.rb install`, 将devkit注册到ruby相关并安装.

- 安装Jekyll: 命令: `gem install jekyll`. 要是运行后失败,在devkit文件夹内双击msys.bat打开相应的shell再执行.然后就等啊等.直到安装完成. 此时运行jekyll server 会发现失败.主要是highlighter问题. 提示新版里,pygments选项已经过时,需要使用highlighter.如果不使用pygments,装rouge的话,`gem install rouge`安装. _config.yml注册:`highlighter: rouge`即可.


- 安装[PIP](https://pip.pypa.io/en/latest/installing.html).有了PIP才好装pygments. 新版本python自带PIP,否则下载get-pip.py运行`python get-pip.py`即可安装完成(会自动装setuptools). 此时pip还不能运行,除非你用绝对路径. 把*C:\Python27\Scripts*(根据自己python的路径)加入到环境变量,就可以直接运行pip了. 

- 安装Pygments: `pip install Pygments`, 要是能直接pip的话,如果你很懒不把pip加到环境变量,那就`python -m pip install Pygments`也可以. 并设置_config.yml 中`highlighter: pygments`. 好了,运行`jekyll server`试试!

- 重装hitimes: 要是运行jekyll server报错 *kernel_require.rb:54:in  'require': cannot load such file -- hitimes/hitimes (LoadError)*, 恩, 你就要重装hitimes了. 原因见[here](https://github.com/copiousfreetime/hitimes/issues/32), 因为发行人没有为window编译该东东.解决办法: `gem uni hitimes` 卸载hitimes, `gem ins hitimes -v 1.2.1 --platform ruby`重装.我的ruby 2.2带的hitimes是1.2.2的.

最后虽然成功了,但我运行时还会出现以下的话:  

> Deprecation: Auto-regeneration can no longer be set from your configuration file(s). Use the --[no-]watch/-w command-line option instead.  
> Deprecation: The 'pygments' configuration option has been renamed to 'highlighter'. Please update your config file accordingly. The allowed values are 'rouge', 'pygments' or null.  
> ...  
> Please add the following to your Gemfile to avoid polling for changes: gem 'wdm', '>= 0.1.0' if Gem.win_platform?  

原因是jekyll在新版里废弃了一些关键词,例如pygments,auto. 我_config.yml文件里面就有这两个设为true.开头加`#`注释掉,添加`highligher: pygments`.  最后一句是因为window要额外装一个东东来watch你修改的变化(其实改了也是马上更新的..),不过为了防止报bug,`gem install wdm` 安装一个程序就好了. 他最后一句的意思是,如果你使用Gemfile,就把那句话加入.

浏览器看[http://127.0.0.1:4000/](http://127.0.0.1:4000/)吧!

貌似响应比Mac慢多了...而且,时区居然失效了...显示a/S..推测是mingw功能太弱? 毕竟功能还是和linux比差..可能对timezone时区识别不好..凑合着用吧..对时间敏感的博客地址可能会失效.

## Reference
1. [jekyll-windows](http://jekyll-windows.juthilo.com/)

------
