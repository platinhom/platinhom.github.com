---
layout: post
title: Sublime:SublimeCodeIntel配置和使用
date: 2015-12-09 07:58:25
categories: IT
tags: IDE
---

这是个Sublime代码自动补全和提示的插件, 很强大! PC介绍参见: <https://packagecontrol.io/packages/SublimeCodeIntel>; Github参见<https://github.com/SublimeCodeIntel/SublimeCodeIntel>

写一个文件: ~/.codeintel/config

~~~
{
    "Python": {
        "python": '/usr/local/bin/python',
        "pythonExtraPaths": ['/usr/local/Cellar/python/2.7.10_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/','/usr/local/Cellar/python/2.7.10_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/']
    }
}
~~~

key-binding

~~~
[
	{ "keys": ["shift+ctrl+space"], "command": "code_intel_auto_complete" },
	{ "keys": ["super+alt+ctrl+up"], "command": "goto_python_definition"},
	{ "keys": ["super+alt+ctrl+left"], "command": "back_to_python_definition"}
]
~~~
~~~

------
