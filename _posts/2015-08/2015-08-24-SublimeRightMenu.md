---
layout: post
title: Sublime添加到右键菜单(附注册表文件)
date: 2015-08-24 12:18:05
categories: IT
tags: IDE
---

添加到右键菜单,只能修改注册表了, 也有一些软件可以协助修改右键菜单的,那就更简便了.只是我现在基本不用这些乱七八糟软件了...

## 修改注册表

- 打开注册表编辑器: 开始->运行->regedit (或者直接win键+r然后输入regedit再确定)
- 展开第一个`HKEY_CLASSES_ROOT`,再展开第一个`*`和第二个`shell`
- 右键这个shell, 新建, 项.名字随便,例如叫Sublime3.
- 点击新建的这个项,右边出现子项,例如默认,此时数值名设置,右键,修改,修改成喜欢的显示的名字,例如edit with Sublime Text3. 如果不修改这个,将使用项名作为右键显示的内容
- 在右边空白处,点击新建->字符串值: Icon, 再修改其值为`sublime路径,0`,例如`C:\Program Files\Sublime Text 3\sublime_text.exe,0`
- 继续右键左边的shell->Sublime3这个项,新建->项, 项名为command,其默认值设置为`sublime路径 %1`,例如`C:\Program Files\Sublime Text 3\sublime_text.exe %1`
- 上述修改能对任何文件起效. 如果想对文件夹起效,就要对`HKEY_CLASSES_ROOT\Directory\shell`重复上述的修改.
- 修改完后随便右键一个文件,起效了~

## 使用注册表文件

或者更简单方法就是修改下面这段reg代码, 保存到subl.reg双击运行就好了.

- 新建一个txt文件,将内容复制到里面
- 修改相应sublime信息,尤其是其路径一定要对.相关含义请参考上述修改注册表的教程.
- 修改后缀为reg,双击文件

~~~
Windows Registry Editor Version 5.00
[HKEY_CLASSES_ROOT\*\shell\SubLime3]
@="edit with Sublime Text3"
"Icon"="C:\\Program Files\\Sublime Text 3\\sublime_text.exe,0"
[HKEY_CLASSES_ROOT\*\shell\SubLime3\Command]
@="C:\\Program Files\\Sublime Text 3\\sublime_text.exe \"%1\""
~~~

这个只能修改对文件进行,如果想对文件夹起效,可以继续加入下面的:

~~~
Windows Registry Editor Version 5.00
[HKEY_CLASSES_ROOT\Directory\shell\SubLime3]
@="edit with Sublime Text3"
"Icon"="C:\\Program Files\\Sublime Text 3\\sublime_text.exe,0"
[HKEY_CLASSES_ROOT\Directory\shell\SubLime3\Command]
@="C:\\Program Files\\Sublime Text 3\\sublime_text.exe -a \"%1\""
~~~

PS: 右键文件夹空白地方的添加方法: 其实是在`HKEY_CLASSES_ROOT\Directory\Background`内,如装有git bash可以参考其值. 只针对shell比较有效罢了

------
