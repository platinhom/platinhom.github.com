---
layout: post
title: iframe跳转的攻防:防止子页面自动跳转
date: 2016-02-11 12:09:31
categories: IT
tags: Html Internet
---

有些网页为了别人用iframe加载他的页面, 经常加入例如以下的代码防止加载, 作用就是导致整个页面重定向到该页面的位置(还可能把历史都清了无法后退). 代码原理简单, 就是自动判断当前的location是否是顶层的，即是否被嵌套到iframe里面了，如是则强制跳转: 

~~~html
<script language="javascript">

//use top/parent/self location
if (top.location != self.location) {
	top.location=self.location;
}

//Use self~top~parent
if (self != top){
	top.location = self.location;
}

if (window.top != window.parent) {
    alert("window对象-被嵌套两层");
}

//The following also work
(t = window.top) && t == window.self || alert("短路计算-被嵌套一层或多层");
(t = window.top) && t == window.parent || alert("短路计算-被嵌套两层");
</script>
~~~

这篇[东东](http://seclab.stanford.edu/websec/framebusting/framebust.pdf)十分好的介绍了一些防止加载的防守方法和一些常用进攻方法, 有空的很值得一看.

--------

不过道高一尺魔高一丈, 总有办法应对的. 例如最简单, 老子禁用JS看你跳啥! 然而, 禁止JS会导致一些链接也点不开..这篇[东东](http://blog.codinghorror.com/we-done-been-framed/)就介绍了使用`onbeforeunload`来搞Digg.

### 方法1: 利用HTML5 sandbox

可以参考这篇[Play safely in sandboxed IFrames](http://www.html5rocks.com/en/tutorials/security/sandboxed-iframes/)东东介绍或者SOF上的[讨论](http://stackoverflow.com/questions/369498/how-to-prevent-iframe-from-redirecting-top-level-window). 简单说,HTML的iframe引入`sandbox`属性, 可以通过sandbox属性设置一些权限. 给给sandbox的值是允许可用的, 而不在里面则会被禁用. 例如我们要防top跳转, 就要取消掉`allow-top-navigation`,如: 

~~~html
<iframe sandbox="allow-same-origin allow-scripts allow-popups allow-forms allow-pointer-lock" src="http://www.example.com"</iframe>
~~~

这里最好留着那句`allow-scripts` 来启用JS. 如果要全部取消, 可以`sandbox=""`

对于老的IE还可以`security="restricted"` 来限制(会disable掉JS). 

### 方法2:

双重iframe可以阻止强制跳转。但是，第一层的iframe会覆盖了第二层的。所以要把第一层的做成透明，然后第二层嵌套需要的网页。做起来并不简单..

### 方法3:

在老IE可以:

`<script type="text/javascript"> var location=document.location; </script>`

但在Chrome实践证明会反复跳转死循环.


------
