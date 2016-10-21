---
layout: post
title: Sublime2&3 基础使用
date: 2015-06-20 20:07:37
categories: IT
tags: IDE Software
---

Sublime是程序猿很爱用的编辑器,支持语法高亮,跨平台,插件多. 可免费使用,代价是经常保存后就提示购买...可参见主页介绍Ref1.现在分发版本主要有成熟的Sublime2(最新还是2.0.2)和beta版本的Sublime3,后者具有更高级的功能, 例如跳转到函数定义处等. 如果没有部分插件非使用sublime2不可,一般建议使用sublime3. 注意Mac版和Win版菜单稍有区别.这里主要以Mac版.

## 功能介绍

- 庞大的扩展包库:  
提供了各种丰富的功能,对各种应用进行适应.得益于其可编程特点.一般使用Package Control.
- 语法解释和高亮:  
View-Syntax有各种语法解释可用,另还可以装载插件使用.可以使用`open all with current extension as`指定文件解释方法.
- 强大的命令面板:  
`shift+cmd+P` 调出面板,可以调用各种命令和插件功能,十分强大方便.
- 强大的Goto Anything:  
`cmd+P` 可以快速跳转文件,搜本文`#`,跳转行`:`,跳转函数定义`@`等.
- 预览全文窗口:  
在右上角有个预览窗口(带语法着色), 支持快速选择跳转.
- 多重选择:   
只要按着`cmd`或`alt`(win)再进行点选,就可以多个选择,多处同时编辑;选中多行后用`cmd+shift+L`的split into lines功能将多行同时选中编辑.`cmd+D`可以选择更多和现在选中一样的,`cmd+ctrl+G`(Win是`alt+F3`)选择所有现在一样的词; 使用中键等进行纵向选择.
- 可作为IDE进行程序编译:   
在Tools提供编译功能,能够自定义编译条件. 支持Project功能.
- 丰富的主题:  
Color Scheme很多.
- 控制台命令控制:  
实际是Python控制台.提供API可以进行高级开发和功能.一般注册参数文件使用JsoN编写.



### 安装

- 软件安装
到官网下载即可.[sublime3](http://www.sublimetext.com/3); [Sublime2](http://www.sublimetext.com/2). 装完后,右键文件会有编辑选项,在OSX中普通的sublime text是3版. 要在shell中调用,可以`ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" ~/bin/sl` 类似地创建快键方式执行(我这里`~/bin`加入到`$PATH`中).

- 破解:  
**win64**: sublime 2.02 64 bit, 如经济允许,请支持正版!(见详细信息)   
**Mac**: [3083](http://www.douban.com/note/486407873/) 
<details>
复制一个sublime.exe文件, 用ultraedit打开编辑(sublime保存2进制有点问题), 查找到4333 3342 3032, 修改3342->3242 然后将该文件放回执行文件夹, 打开后 Help->Enter License输入以下内容就OK了.   
—–BEGIN LICENSE—–
hiwanz
Unlimited User License 
EA7E-26838 
5B320641E6E11F5C6E16553C438A6839
72BA70FE439203367920D70E7DEB0E92
436D756177BBE49EFC9FBBB3420DB9D3
6AA8307E845B6AB8AF99D81734EEA961
02402C853F1FFF9854D94799D1317F37
1DAB52730F6CADDE701BF3BE03C34EF2
85E053D2B5E16502F4B009DE413591DE
0840D6E2CBF0A3049E2FAD940A53FF67
—–END LICENSE—–
</details>


- [Package Control](https://packagecontrol.io/)
Package Control是ST最基本的插件,用来安装别的插件用.
到主页页面的[安装](https://packagecontrol.io/installation)去选择sublime2/3的安装代码,复制.`` ctrl+` ``调出命令行,将代码黏贴,回车.然后重启sublime即可.  
测试: `cmd+shift+p`调出命令面板,输入`PCI`缩写定位,然后选择后,随便输入个东东,选择后即会自动安装. 卸载插件时使用`PCRP`来定位选择即可.



### 快捷键:
快捷方式的设置可以在`ST-Preference-Key Binding-Default`中设置基本快捷键.

#### ST功能

- \* `` Ctrl+` ``   开启控制命令行;   
- \*`cmd+shift+P`    命令面板,支持缩写名称. 例如PCI就是安装软件. 
- `cmd+P` Goto Anything, 跳到指定地方. 高级跳转查找.
- `Ctrl+K+B `    开关侧栏
- `cmd+B`    使用预设编译设置来编译   
- `cmd+shift+B`    编译运行
- `F6`    检查语法错误(再按取消)
- `cmd+ +`和`cmd+ -` 字体放大/缩小

#### 一般通用
- `cmd+S`  保存文件, `cmd+shift+s` 另存为.
- `cmd+O`  打开文件, `cmd+N` 新建文件
- `cmd+w` 关闭文件.
- `cmd+z` 撤销, `cmd+y` 重做
- `cmd+C/V/X` 复制黏贴剪切
- `F11`    全屏

#### 选择功能
- `cmd+A` 全选, 反选要用Selection菜单
- `cmd`或`alt`(win): 多重选择功能,任意点选
- `Ctrl+shift+上下` 纵向多重选择(我设多了个`alt`).也可以利用`鼠标中键`或者`左键+alt`(mac)或`右键+shift`(win/linux)
- \* `Cmd+D`    选词, 可以反复向下选词(多选词)
- \* `cmd+ctrl+G`    选所有该词.
- `cmd+L`    选中一行.
- `cmd+shift+L`   选择多行后,使用split into lines功能可以切换到多重选择各行的末末尾(最后一行不一定.)
- `shift+ctrl+M`    选中括号内所有内容. 有说是cmd+ctrl+M的.参考括号跳转`cmd+M`
- `cmd+shift+space` 选择一段.注意可能会和输入法冲突.一般更常用菜单.
- `cmd+左右` 跳到行头或行末

#### 编辑功能
- \*`cmd+/`    注释该行    `cmd+alt+/`    块注释
- `cmd+shift+enter`    直接在该行前插入行(不断行)     `cmd+enter`    直接在该行后插入行(不断行) 
- `cmd+shift+[或]`    折叠/展开代码
- `cmd+shift+ 上或下`    移动该行代码, 上下行互换
- `cmd+shift+ T`    重新打开刚关闭的标签页
- `cmd+F2` 和 `F2` 设置以及跳到下一个标签
- `ctrl+空白` 补全功能, 注意Mac默认的spotlight会与此冲突.

#### 查找定位
- `cmd+F` 查找, 出现下方的查找栏.可以用`cmd+G`和`cmd+shift+G`或按钮进行查找下一个,上一个.
- `shift+G` 跳到某行,也可以在跳转命令框(`cmd+p`)中用`:100`指定行数.
- \*`cmd+E` 将选中内容作为查找内容(自动复制)
- `ctrl+M`    括号前后跳转
- `ctrl+alt+up/down` 视觉上下移动一行



### 插件
安装插件两种方式,最方便是使用Package Control进行(`cmd+shift+P,PCI`); 另外也可以网上的相应插件放到插件库中(`Preference-Browse Packages`).  
插件可以利用PCI搜索,但是不方便看介绍.可以去PC的[搜索页](https://packagecontrol.io/search)搜索.  
插件的设置使用和更新: 在Preference中, Package Setting可以设置插件; Browse Package可以跳转到插件文件夹; Package Control可以来用命令控制更新卸载; Package使用一般在Tools里底部.  

- bracket highlighter: 括号高亮
 preferences->package settings->brackethighlighter->bracket settings default, 打开文件后编辑bracket_styles{} 将default的改underline为highlight, color更改为entity.name.class 即可. 更多设置[参考](http://blog.sserhuangdong.com/2014/04/22/my-sublime-setting/#BracketHighlighter配置  )
还可以实现快捷键选取括号内容, 跳转到开头/结尾等.

- sublimeLinter: 代码错误提示
- Alignment: 以等号为准对齐, Ctrl+Alt+A 使用
- Emmet(Zen Coding): 高效编写html和css
- [Terminal](https://packagecontrol.io/packages/Terminal): 可以方便地在文件中调出命令行. 可以右键文件来调用, 也可以`cmd+shift+T`. 可配置iTerm.
- [IMESupport](https://github.com/chikatoike/IMESupport): 部分电脑使用ST时输入法不跟随光标...使用该插件即可解决.

#### Markdown 相关
- [Markdown Extended](https://packagecontrol.io/packages/Markdown%20Extended): 扩展的markdown着色,支持GFM的代码块,可以在代码块中根据标示来着色.
- [Monokai Extender](https://packagecontrol.io/packages/Monokai%20Extended): 使用md时必须的着色工具,在`Color Scheme`中设置即可.
- [Markdown Preview](https://packagecontrol.io/packages/MarkdownEditing): 支持将md文件编译,并用浏览器浏览,使用参看[ref](http://www.jianshu.com/p/378338f10263),我设了快捷键`super+ctrl+m`.
- [Mou MD App](https://packagecontrol.io/packages/Mou%20Markdown%20App%20\(OSX\)): 在Tools中增加选项使用Mou编辑.
- [Markmon real-time](https://packagecontrol.io/packages/Markmon%20real-time%20markdown%20preview): 实时浏览,比较复杂需要插件.
- [MakrdownEditing](https://packagecontrol.io/packages/MarkdownEditing): 貌似很强大的插件,但装了后取代了原来的markdown语法,monokai不能用.只能把ST3配置全删了重新设置.折腾.


### 使用技巧

- **竖向选择**:  
利用鼠标: OSX: 左键+Opt或者直接中键;多选区或移除:Cmd和Cmd+Shift;  Win: 右键+Shift或者中键; Linux: 右键+Shift; Win/linux多个选区或移除: Ctrl和Alt;  
利用键盘: OSX: Ctrl+shift+上下 (注意:ctrl+shift+上下可能会是慢速的显示多任务,因为ctrl+上/下被OSX占用,shift起到慢速的作用.这时解决办法两个,1:在系统设定中取消Ctrl+上/下快捷键; 2:在Key-Binding,default中搜索`select_lines`并改变快捷键,例如我改为没有用到的`Ctrl+shift+alt+上下`); Win/linux: Ctrl+Alt+上下.

- **Project功能**:Ref7.  
	- 先使用`Add folder to project`功能,将文件夹加入到project.可用快捷键`cmd+K,cmd+B`组合来调出左边工具栏.
	- 可以保存project`Save Project As`到`sublime-project`文件,里面包括文件夹信息,配置等.另外还有`sublime-workspace`文件,里面记录了更多缓冲细节信息,包括正在编辑文件信息.
	- 可以关闭project(`Close Project`,会自动保存信息)再打开(`Quick Switch Project`,`Ctrl+Cmd+P`).此时之前编辑的文件及设置又出现了.
	- 可以利用`cmd+P`快速搜索project内文件.
	- 可以`Edit Project`,添加配置信息.例如`"settings"`,`"build_systems"`.可以在此自行新建相应的build的信息(会出现在build里).

### 注意事项

- fortran语法高亮
可以直接自动安装MinimalFortran package, 但该版本的语法比较傻, 不好用.
[建议](http://stackoverflow.com/questions/13713577/how-to-get-proper-text-color-highlighting-for-fortran-90-in-sublime-text-2)安装: [textmate/fortran.tmbundle](https://github.com/textmate/fortran.tmbundle  ) 下载zip整个文件夹解压后, 直接放到AppData\Roaming\Sublime Text 3\Packages 文件夹夹内(改名为Fortran文件夹哦!)

- Mac双击打开时在不新建窗口:
Perference->Setting Default->搜索New_Window, 打开文件在新窗口设为false. (ST3有bug, 要在Preference->browse package中打开文件夹, 并自己新建一个Default文件夹..保存setting文件再打开.)


## Reference

1. [主页](http://www.sublimetext.com/)
2. [手册](http://docs.sublimetext.info/en/latest/)
3. [知乎:sublime有哪些实用技巧?](http://www.zhihu.com/question/19976788 )
4. [sublime非官方文档](http://sublime-text.readthedocs.org/en/latest/intro.html)
5. [善用佳软视频介绍](http://xbeta.info/sublime-text2.htm)
6. [Sublime编译build设置](/2015/06/21/sublime-build/)
7. [Understanding projects in sublime text saving switching etc](http://www.joshuawinn.com/understanding-projects-in-sublime-text-saving-switching-etc/)
8. [带动图教程](http://lucida.me/blog/sublime-text-complete-guide/?comefrom=http://blogread.cn/news/)


---
