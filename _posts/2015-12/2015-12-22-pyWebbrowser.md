---
layout: post
title: Python:使用浏览器打开网页
date: 2015-12-22 06:34:17
categories: Coding
tags: Python
---

可以使用Python用浏览器打开指定网址.

### 五个主函数:

- webbrowser.**open**(url, new=0, autoraise=True)  
用默认浏览器打开url, new=0是当前窗口, 1: 新窗口, 2: 新tab. autoraise 可能是自动切换到浏览器..测试无效. **最常用**函数.
- webbrowser.open_new(url)  
使用新窗口打开网页
- webbrowser.open\_new_tab(url)   
使用新tab打开网页.
- webbrowser.get([name])  
使用类型名来获得浏览器控制器对象. 不常用.
- webbrowser.register(name, constructor[, instance])  
注册新的浏览器控制器, 比较高级..更不常用.

> 1.新窗口和新tab在我测试的mac/win7下均无效..所以可以忽略了  
> 2.需要打"http://", 或者"file:///" 一类. 否则返回True 但无响应

### Browser Controller Object (浏览器控制器对象)

通过`webbrowser.classname()`来创建, 或者通过`webbrowser.get(typename)` 来创建获得. 具有和webbrowser一样的 open, open\_new 和 open\_new_tab 方法.

使用对应方法可以获得浏览器控制对象, 默认采用默认浏览器, 可以指定浏览器(但不一定起效..例如我测试windows-default 就无效..), 然后再打开网页. 例如

~~~python
import webbrowser
a=webbrowser.get('safari')
#a=webbrowser.MacOSX('safari')
a.open("http://www.baidu.com")
~~~

Type Name	| Class Name
------|-------
'mozilla'	| Mozilla('mozilla')	 
'firefox'	| Mozilla('mozilla')	 
'netscape'	| Mozilla('netscape')	 
'galeon'	| Galeon('galeon')	 
'epiphany'	| Galeon('epiphany')	 
'skipstone'	| BackgroundBrowser('skipstone')	 
'kfmclient'	| Konqueror()
'konqueror'	| Konqueror()
'kfm'	|	Konqueror()
'mosaic'	|	BackgroundBrowser('mosaic')	 
'opera'		|	Opera()	 
'grail'		|	Grail()	 
'links'		|	GenericBrowser('links')	 
'elinks'	|	Elinks('elinks')	 
'lynx'	|	GenericBrowser('lynx')	 
'w3m'	|	GenericBrowser('w3m')	 
'windows-default'	|	WindowsDefault
'macosx'	|	MacOSX('default')
'safari'	|	MacOSX('safari')

另外还见到 *Chrome*, *Chromium* 和 *MacOSXOSAScript*类.

<iframe src="https://docs.python.org/2/library/webbrowser.html" width="100%" height="800" frameborder="1" scrolling="auto"></iframe>

> Referece: [python-doc-webbrowser](https://docs.python.org/2/library/webbrowser.html); 
[inside: python-doc-webbrowser](/ManualHom/Coding/Python/python-2.7.11rc1-docs-html/library/webbrowser.html)

------
