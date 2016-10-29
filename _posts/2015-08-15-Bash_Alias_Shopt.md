---
layout: post
title: 在shell脚本中使用alias(shopt)
date: 2015-08-15 11:47:20
categories: IT
tags: Bash ZZ
---

转载自: [在shell脚本中使用alias](http://www.cnblogs.com/qcly/p/3219780.html)

------

Linux shell有交互式与非交互式两种工作模式。我们日常使用shell输入命令得到结果的方式是交互式的方式，而shell脚本使用的是非交互式方式。 

 
shell提供了alias功能来简化我们的日常操作，使得我们可以为一个复杂的命令取一个简单的名字，从而提高我们的工作效率。在交互式模式下，shell的alias扩展功能是打开的，因此我们可以键入自己定义的alias别名来执行对应的命令。
 
但是，在非交互式模式下alias扩展功能默认是关闭的，此时仍然可以定义alias别名，但是shell不会将alias别名扩展成对应的命令，而是将alias别名本身当作命令执行，如果shell内置命令和PATH中均没有与alias别名同名的命令，则shell会“抱怨”找不到指定的命令。
 
那么，有没有办法在非交互式模式下启用alias扩展呢？答案是使用shell内置命令shopt命令来开启alias扩展选项。shopt是shell的内置命令，可以控制shell功能选项的开启和关闭，从而控制shell的行为。shopt的使用方式如下：

~~~bash
shopt -s opt_name                 Enable (set) opt_name.
shopt -u opt_name                 Disable (unset) opt_name.
shopt opt_name                    Show current status of opt_name.
~~~

alias扩展功能的选项名称是expand_aliases，我们可以在交互式模式下查看此选项是否开启：

~~~bash
->>  shopt expand_aliases
expand_aliases  on
->> 
~~~
可见在交互式模式下alias扩展功能的确是开启的，因此我们才能使用alias别名。
 
我们编写一个脚本来验证一下非交互式模式下alias扩展的设置：

~~~bash
#!/bin/bash --login

alias echo_hello="echo Hello!"
shopt expand_aliases   
echo_hello

shopt -s  expand_aliases  
shopt expand_aliases   
echo_hello
~~~

脚本执行结果如下：

~~~bash
./test.sh 
->> expand_aliases  off
./test.sh: line 5: echo_hello: command not found
expand_aliases  on
Hello!
->>
~~~
可以看到，在非交互式模式下alias扩展功能默认是关闭的，但是我们可以用shopt来将其开启。
 
另外，alias别名只在当前shell有效，不能被子shell继承，也不能像环境变量一样export。可以把alias别名定义写在.bashrc文件中，这样如果启动交互式的子shell，则子shell会读取.bashrc，从而得到alias别名定义。但是执行shell脚本时，启动的子shell处于非交互式模式，是不会读取.bashrc的。
 
不过，如果你一定要让执行shell脚本的子shell读取.bashrc的话，可以给shell脚本第一行的解释器加上参数：

`#!/bin/bash --login`  

--login使得执行脚本的子shell成为一个login shell，login shell会读取系统和用户的profile及rc文件，因此用户自定义的.bashrc文件中的内容将在执行脚本的子shell中生效。
 
还有一个简单的办法让执行脚本的shell读取.bashrc，在脚本中主动source ~/.bashrc即可。

------
