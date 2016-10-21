---
layout: post
title: HTML的锚标签和跳转
date: 2015-06-30 21:12:35
categories: Coding
tags: HTML
---

`<a href=""></a>`标签以及页面跳转功能是个是造网页时十分重要的标签, 对于写入各种子链接十分重要. 这里总结一下.

## 锚([Anchor](http://www.w3school.com.cn/tags/tag_a.asp))和超链接 `<a>`

### 属性和方法

- `href`: 定义超链接指向的页面的 URL。也可以页内跳转(利用锚`"#name"`),可以发送邮件. 注意若为文件夹网址,最好在最后加上`/`
- `target`: 规定何处打开超链接文档 
	- `_self`: 本窗口,默认值; 
	- `_blank`: 新窗口; 
	- `framename`: 这里是具体某个frame的"name", 将在这个frame打开这个超链接.当前frame/页面不变.
	- `_parent`: 在父框架集中打开被链接文档;  
	- `_top`: 用来清除frame的限制,使得在frame内点超链接会变回整个窗口化.
	- 不存在的名称: 如果这个指定名称或id的框架或者窗口不存在,浏览器将打开一个新的窗口,给这个窗口一个指定的标记,然后将新的文档载入那个窗口.从此以后,超链接文档就可以指向这个新的窗口。以后点击指向这个target的超链接都会在这个新窗口中打开并跳转过去.
- `rel`: 规定当前文档与被链接文档之间的关系,一般给搜索引擎使用.
- `hreflang`: 规定被链接文档的语言。
- `name`: 定义锚名称, HTML5不支持
- `rev`: 和rel一样,HTML5不支持
- `shape`: 规定链接的形状(default,rect,circle,poly)。HTML5不支持.很多浏览器不支持.
- `charset`: 规定被链接文档的字符集。HTML5不支持
- `coords`: 规定链接的坐标。HTML5不支持
- `type`: 指明链接目标的MINE类型,如text/html.
- `download`: 规定被下载的超链接目标(其实就是下载后的名字,对于图片等可以自动后缀.真实连接还是在href). HTML5新属性
- `media`: 规定被链接文档是为何种媒介/设备优化的,如打印机,手机等会进行一些跳转后的设置. HTML5新属性
- 支持全局属性

### [DOM对象](http://www.w3school.com.cn/jsref/dom_obj_anchor.asp)

- `document.getElementById(ID)` 来调用
- `anchors[]`数组访问锚
- `blur()`, a对象方法把焦点从链接上移开
- `focus()`,给连接应用焦点.


### CSS pseudo-class属性

- `a:link {color: #FF0000}`		/* 未访问的链接 */
- `a:visited {color: #00FF00}`	/* 已访问的链接 */
- `a:hover {color: #FF00FF}`	/* 鼠标移动到链接上 */
- `a:active {color: #0000FF}`	/* 选定的链接 */
- a:hover 必须被置于 a:link 和 a:visited 之后，才是有效的。a:active 必须被置于 a:hover 之后，才是有效的。

## 应用

### 文字或图片提供超链接

- `<a href="/example/html">我是超链接</a>`  文字作为超链接
- `<a href="/example/html"><img src="/eg_buttonnext.gif" /></a>` 图片作为超链接

### 页内跳转

- `<a name="tips">基本的注意事项 - 有用的提示</a>` 命名锚. 不仅仅是`<a>`可以,别的标签也可以.id是name的升级版,也可使用.
- `<a href="#tips">有用的提示</a>` 跳转到锚.
- `<a href="http://www.w3school.com.cn/html/html_links.asp#tips">有用的提示</a>` 直接在链接中新页面中跳转到媌
- `<a href="#top">Top</a>` 跳转到顶部(不需定义锚). 找不到已定义的命名锚也会跳转到top.

### 邮件

- `href="mailto:yourmail@microsoft.com?subject=Hello%20again"` subject是题目, `%20`是空格.

### 新窗口打开

`<a href="http://platinhom.github.io/" target="_blank">My Blog!</a>`

<a href="http://platinhom.github.io/" target="_blank">My Blog!</a>

### PHP实现弹出消息框并自动返回
因为PHP无法操作客户端, 只能echo出HTML代码,利用JS来操控DOM.

- 使用JS的`history.back()`来返回,就是一般的返回后退,之前的表单输入会保留.  
`echo "<script>alert('We will go back! The old input will be kept!'); history.back();</script>"`
- 使用JS的`location.href='../index.html'`来返回. 注意这是重新进入页面,并不是真正返回, 输入内容会重置!  
`echo "<script>alert('We will go back by redirection! The old input will lost!');location.href='../index.html';</script>";`

### 刷新页面或跳转

- `echo “<meta http-equiv=\”refresh\” content=\”1;url=’index.php’\”>”;`设定时间进入网页后几秒自动跳转. 不写后面的url就是自动刷新.
- `echo “<script>window.location=’index.php’;</script>”;`跳转到指定页面, 例如本页
- `echo “<script language=JavaScript>parent.mainFrame.location.reload();</script>”;` 可以刷新别的页面(框架)而不跳转

~~~ php

# JS实现
//top.location.href   顶级窗口的地址
//this.location.href  当前窗口的地址

#测试网址:     http://localhost/blog/testurl.php?id=5

//获取域名或主机地址 
echo $_SERVER['HTTP_HOST']."<br>"; #localhost

//获取网页地址 
echo $_SERVER['PHP_SELF']."<br>"; #/blog/testurl.php

//获取网址参数 
echo $_SERVER["QUERY_STRING"]."<br>"; #id=5

//获取用户代理 
echo $_SERVER['HTTP_REFERER']."<br>"; 

//获取完整的url
echo 'http://'.$_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI'];
echo 'http://'.$_SERVER['HTTP_HOST'].$_SERVER['PHP_SELF'].'?'.$_SERVER['QUERY_STRING'];
#http://localhost/blog/testurl.php?id=5

//包含端口号的完整url
echo 'http://'.$_SERVER['SERVER_NAME'].':'.$_SERVER["SERVER_PORT"].$_SERVER["REQUEST_URI"]; 
#http://localhost:80/blog/testurl.php?id=5

//只取路径
$url='http://'.$_SERVER['SERVER_NAME'].$_SERVER["REQUEST_URI"]; 
echo dirname($url);
#http://localhost/blog
~~~

---
