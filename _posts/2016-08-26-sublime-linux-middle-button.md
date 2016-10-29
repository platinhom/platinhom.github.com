---
layout: post
title: Linux系统sublime的中键选择和重映射鼠标键
date: 2016-08-25 19:12:24
categories: IT
tags: IDE
---

在Linux里面中键用于黏贴选择的内容, 所以在sublime里面也是, 因此其功能也默认是黏贴选择的内容.

这样导致原来在Win和Mac里面中键选择纵列的功能失效!! 

现在想把游戏鼠标的左边两个副键功能加进去, 作为纵列选择!

## 打开配置文件

首先, 要找到这个鼠标的配置文件. 在ubuntu里加载的默认的是`~/.config/sublime-text-3/Packages/Default/Default\ \(Linux\).sublime-mousemap` 文件(不太清楚的话, 菜单Key binding-Default 就可以知道具体文件位置, 对应的罢了). 但默认情况下, 事没有这个文件夹和文件的. 而缺省的鼠标配置文件也是未知的.

- 创建默认配置的文件夹: `mkdir ~/.config/sublime-text-3/Packages/Default`
- 安装一个插件: [PackageResourceViewer](https://github.com/skuroda/PackageResourceViewer) : `ctrl+shift+P` -> pci -> PackageResourceViewer. 这个插件能够帮助编辑sublime的一个叫Default的资源包, 打开相应配置文件
- `ctrl+shift+P` -> `PackageResourceViewer: Open Resource`-> `Default` -> `Default (...OS...).sublime-mousemap`. 打开鼠标配置文件.
- ctrl + s 保存一下. 这个文件就出来啦!~ (确保上面的Default文件夹存在)

## 重设鼠标键

鼠标的几个键对应名字:

- button1 : 左键
- button2 : 右键
- button3 : 中键
- button4 : 上滚轮
- button5 : 下滚轮
- button6 : ??
- button7 : ??
- button8 : 左侧的副键1
- button9 : 左侧的副键2

这些键的位置可以通过命令`xev` 然后在小白框里面按键, 然后会反映在命令行里面. 

> 注意: 这里`xev` 的中键右键可能和配置文件里不太一样! 以配置文件为准!

好了, 然后更改这个配置文件, 注释掉键8和键9的左右, 然后将他们都映射为纵向选择~~

~~~json
	// 注释掉原来设置
	//{ "button": "button8", "modifiers": [], "command": "prev_view" },
	//{ "button": "button9", "modifiers": [], "command": "next_view" },

	// 添加以下两块
	// Map column selection to 4th mouse button ("button8").
    {
        "button": "button8",
        "press_command": "drag_select",
        "press_args": {"by": "columns"}
    },

	// Map column selection to 5th mouse button ("button9").
    {
        "button": "button9",
        "press_command": "drag_select",
        "press_args": {"by": "columns"}
    },

    // 下面是本来中键的功能
    // Middle click paste
	{ "button": "button3", "command": "paste_selection_clipboard" },
~~~

纵向选择的代码其实就是仿照上面一个`"button": "button2", "modifiers": ["shift"],` 来改的.

整个文件如下, enjoy it:

~~~json
[
	// Basic drag select
	{
		"button": "button1", "count": 1,
		"press_command": "drag_select"
	},
	{
		"button": "button1", "count": 1, "modifiers": ["ctrl"],
		"press_command": "drag_select",
		"press_args": {"additive": true}
	},
	{
		"button": "button1", "count": 1, "modifiers": ["alt"],
		"press_command": "drag_select",
		"press_args": {"subtractive": true}
	},

	// Select between selection and click location
	{
		"button": "button1", "modifiers": ["shift"],
		"press_command": "drag_select",
		"press_args": {"extend": true}
	},
	{
		"button": "button1", "modifiers": ["shift", "ctrl"],
		"press_command": "drag_select",
		"press_args": {"additive": true, "extend": true}
	},
	{
		"button": "button1", "modifiers": ["shift", "alt"],
		"press_command": "drag_select",
		"press_args": {"subtractive": true, "extend": true}
	},

	// Drag select by words
	{
		"button": "button1", "count": 2,
		"press_command": "drag_select",
		"press_args": {"by": "words"}
	},
	{
		"button": "button1", "count": 2, "modifiers": ["ctrl"],
		"press_command": "drag_select",
		"press_args": {"by": "words", "additive": true}
	},
	{
		"button": "button1", "count": 2, "modifiers": ["alt"],
		"press_command": "drag_select",
		"press_args": {"by": "words", "subtractive": true}
	},

	// Drag select by lines
	{
		"button": "button1", "count": 3,
		"press_command": "drag_select",
		"press_args": {"by": "lines"}
	},
	{
		"button": "button1", "count": 3, "modifiers": ["ctrl"],
		"press_command": "drag_select",
		"press_args": {"by": "lines", "additive": true}
	},
	{
		"button": "button1", "count": 3, "modifiers": ["alt"],
		"press_command": "drag_select",
		"press_args": {"by": "lines", "subtractive": true}
	},

	// Column select
	{
		"button": "button2", "modifiers": ["shift"],
		"press_command": "drag_select",
		"press_args": {"by": "columns"}
	},
	{
		"button": "button2", "modifiers": ["shift", "ctrl"],
		"press_command": "drag_select",
		"press_args": {"by": "columns", "additive": true}
	},
	{
		"button": "button2", "modifiers": ["shift", "alt"],
		"press_command": "drag_select",
		"press_args": {"by": "columns", "subtractive": true}
	},

	// Map column selection to 4th mouse button ("button8").
    {
        "button": "button8",
        "press_command": "drag_select",
        "press_args": {"by": "columns"}
    },

	// Map column selection to 5th mouse button ("button9").
    {
        "button": "button9",
        "press_command": "drag_select",
        "press_args": {"by": "columns"}
    },

	// Middle click paste
	{ "button": "button3", "command": "paste_selection_clipboard" },

	// Switch files with buttons 4 and 5, as well as 8 and 9
	{ "button": "button4", "modifiers": [], "command": "prev_view" },
	{ "button": "button5", "modifiers": [], "command": "next_view" },
	//{ "button": "button8", "modifiers": [], "command": "prev_view" },
	//{ "button": "button9", "modifiers": [], "command": "next_view" },

	// Change font size with ctrl+scroll wheel
	{ "button": "scroll_down", "modifiers": ["ctrl"], "command": "decrease_font_size" },
	{ "button": "scroll_up", "modifiers": ["ctrl"], "command": "increase_font_size" },

	{ "button": "button2", "modifiers": [], "press_command": "context_menu" }
]
~~~

------
