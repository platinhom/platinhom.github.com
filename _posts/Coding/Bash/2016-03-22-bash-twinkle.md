---
layout: post
title: Bash输出效果带闪烁
date: 2016-03-21 19:47:27
categories: Coding
tags: Bash
---

最近一段时间在找工作, 也发生了一些十分不顺心的事. 没怎么写blog. 今天登陆HPCC看着那个闪烁的NOTICE, 就探究一下怎么实现的吧.

这个是通过控制输出式样来实现的, 例如`echo`, 例如我们的命令行前面的提示符受`PS1`, `PS2`环境变量控制显示效果.

先以比较容易测试的`echo`为例

~~~bash
echo -e "\033[5;32;49;1m Hello World! \033[25;39;49;0m"
~~~

这个命令输出为一个背景黑色(49)闪烁的(5)绿色(32)加粗(1)字体的Hello World. 这里面的1,5,32,49 分别对应下面的颜色动作控制 (见后续解析) 

### echo -e

echo 是输出命令啦, 和今天这个主题相关的有`-e`和`-E`选项, 后者是默认:

- `-e` : 开启转义符解析
- `-E` : 关闭转义符解析 (默认)

默认下, 是关闭转义符功能的(但我在HPCC测试下, 默认却是`-e`, 在MinGW中测试默认是`-E`). 但我们最好要使用转义时都使用`-e`. 简单测试:

`echo -e "\a"` 会产生蜂鸣声. 这里转义的内容要在`""`内!否则会输出a.

编码 |	转义
----|----
\\\\   |	输出转义符斜杠
\a     |	警告声
\b     |	回退 backspace
\c     |	不再输出后面的结果
\e     |	转义后面的内容
\f     |	换页 form feed
\n     |	换行
\r     |	回车键CR, carriage return
\t     |	水平tab
\v     |	垂直tab
\0NNN  |	8进制值 NNN (1 to 3 数字)
\xHH   |	16进制值 HH (1 to 2 数字字母)

在这个转义编码中, 上述echo helloworld例子的`\033`相当于`\e`,表示将转义后面的内容,一般是跟随非常规字符序列(后面部分). `007`相当于`\a`

### `[5;0m` 非常规字符序列

当使用`\033`或`\e`转义码时, 后面可以跟随非常规字符序列. 这个字符序列可以设置多项, 使用`;`分隔.

- `[`是表示非常规字符序列的开始
- `m`是表示非常规字符序列的结束,并且设置输出属性

除了`[m`的组合, 还有如

- `\033[2J` : 清除屏幕
- `\033[0q` :　关闭所有的键盘指示灯
- `\033[1q` :　设置“滚动锁定”指示灯 (Scroll Lock) (实际只影响这次输出,而且是硬件响应)
- `\033[2q` :　设置“数值锁定”指示灯 (Num Lock) (实际只影响这次输出,而且是硬件响应)
- `\033[3q` :　设置“大写锁定”指示灯 (Caps Lock) (实际只影响这次输出,而且是硬件响应)
- `\033[0:1H` :	设置控制输出到屏幕第几条指令(前者)第几行(>=0). `\033[H`实际是清屏..有些地方说是row和column关系, 但测试不太像..

以下是`[m`控制的编码数值(前景就是字体颜色), 字体颜色在30~37, 背景颜色40~47, 闪烁是5/25, 下划线2,38/24,39 :

编码 |	颜色/动作
----|----
0 |	重新设置属性到缺省设置
1 |	设置粗体
2 |	设置一半亮度（模拟彩色显示器的颜色）
4 |	设置下划线（模拟彩色显示器的颜色）
5 |	设置闪烁
7 |	设置反向图象
22 |	设置一般密度
24 |	关闭下划线
25 |	关闭闪烁
27 |	关闭反向图象
30 |	设置黑色前景
31 |	设置红色前景
32 |	设置绿色前景
33 |	设置棕色前景
34 |	设置蓝色前景
35 |	设置紫色前景
36 |	设置青色前景
37 |	设置白色前景
38 |	在缺省的前景颜色上设置下划线
39 |	在缺省的前景颜色上关闭下划线
40 |	设置黑色背景
41 |	设置红色背景
42 |	设置绿色背景
43 |	设置棕色背景
44 |	设置蓝色背景
45 |	设置紫色背景
46 |	设置青色背景
47 |	设置白色背景
49 |	设置缺省黑色背景

所以, `echo -e "\033[5;32;49;1m Hello World! \033[25;39;49;0m"` 实际是`[m`控制了输出格式后, 输出字符, 再重新设回格式. 一般只输出一次的话, 只要前面那段控制即可

### PS1/PS2/PS3/PS4

这个是我们在Shell敲命令时前面的提示符, 例如名字,主机和路径信息等.

~~~
PS1    The  value  of  this parameter is expanded (see PROMPTING below)
      and used as the primary prompt string.   The  default  value  is
      ``\s-\v\$ ''.
PS2    The  value of this parameter is expanded as with PS1 and used as
      the secondary prompt string.  The default is ``> ''.
PS3    The value of this parameter is used as the prompt for the select
      command (see SHELL GRAMMAR above).
PS4    The  value  of  this  parameter  is expanded as with PS1 and the
      value is printed before each command  bash  displays  during  an
      execution  trace.  The first character of PS4 is replicated mul‐
      tiple times, as necessary, to indicate multiple levels of  indi‐
      rection.  The default is ``+ ''.
~~~

PS1是主提示符(每句命令前面的提示), PS2是副提示符 (例如for之类换行后提示信息符, 默认">"), PS3是使用`select`命令时的提示符, PS4是在`set -x`这种跟踪命令和输出的情况下命令的提示符. 关于这四个变量的使用, 参考[PS1,PS2,PS3,PS4和PROMPT_COMMAND](http://dongweiming.github.io/blog/archives/ps1ps2ps3ps4%E5%92%8Cprompt_command/)和[deepin: [提示] Linux Deepin 中 $PS1, $PS2, $PS3, $PS4 等变量的解释](https://blog.deepin.org/2012/12/ps1-ps2-ps3-ps4-variables-explained/). PS4一般是调试时使用, 一般使用PS1和PS2足够了.

编码 |	转义
----|----
\d	|	代表日期，格式为weekday month date，例如："Thu Mar 30"
\H	|	完整的主机名称。例如：我的机器名称为：`Hom.linux`，则这个名称就是Hom.linux
\h	|	仅取主机的第一个名字，如上例，则为Hom，`.linux`则被省略
\t	|	显示时间为24小时格式，如：HH：MM：SS
\T	|	显示时间为12小时格式
\A	|	显示时间为24小时格式：HH：MM
\u	|	当前用户的账号名称
\v	|	BASH的版本信息
\w	|	完整的工作目录名称。用户目录会以 ~代替
\W	|	利用basename取得工作目录名称，所以只会列出最后一个目录
`\#`	|	下达的第几个命令
`\$`	|	提示字符，如果是root时，提示符为：# ，普通用户则为：$
`\[`	|	字符"["
`\]`	|	字符"]"
`\!`	|	命令行动态统计历史命令次数

例如:

~~~bash
PS1="[\e[32;1m\u@\e[35;1m\h \e[31;1m\W]\$"
~~~

实际输出[用户名@主机首名 当前目录名]$ , 当然包括各种格式控制咯.

------
