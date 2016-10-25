---
layout: post
title: CSS-blockquote引用样式
date: 2015-11-09 18:15:04
categories: Coding
tags: CSS HTML
---

本博客引用样式: 

> The blockquote XHTML tag is a fairly useful (if somewhat underused) element. Semantically speaking, a blockquote should be used any time you’re quoting a longer piece of text from another source – another speaker, another website, whatever. It’s a way of setting the text apart, and showing that it came from some other source. Stylistically, you could accomplish all this with a special class on your paragraph tags… but that wouldn’t be as semantically useful, now, would it?  
> Blockquotes do have some styling by default. Most browsers will indent the text in a blockquote tag, which helps the user recognize that the text is different somehow. But who's to say that we need to stop there? Here are six different ways you could style your blockquotes using CSS.

测试文件test-css.html, css部分额外加到html主体内即可:

~~~html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en-us">
<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Test CSS blockquote</title>
</head>
<blockquote>
  <p>The blockquote XHTML tag is a fairly useful (if somewhat underused) element. Semantically speaking, a blockquote should be used any time you’re quoting a longer piece of text from another source – another speaker, another website, whatever. It’s a way of setting the text apart, and showing that it came from some other source. Stylistically, you could accomplish all this with a special class on your paragraph tags… but that wouldn’t be as semantically useful, now, would it?<br>
  Blockquotes do have some styling by default. Most browsers will indent the text in a blockquote tag, which helps the user recognize that the text is different somehow. But who's to say that we need to stop there? Here are six different ways you could style your blockquotes using CSS.</p>
</blockquote>
</body>
</html>
~~~

## 引用样式 blockquote

引用样式决定了主体文字(大小,颜色), 背景颜色, 空隙, 边界等.

### 带边界样式

这个样式比较简单, 就是设置一个左边界, 设置好粗度. color控制字体颜色, background-color控制背景颜色(或者直接backgroup也可以). margin控制引用到窗口元素的距离, border-left控制左边界样式, padding(尤其左边界距离padding-left)控制文字到(左)边界的距离. 这种样式简明扼要, 适用于朴素的博客.

~~~css
blockquote {
	margin: 1em 3em;
	padding: .5em 1em;
	border-left: 5px solid #fce27c;
	background-color: #f6ebc1; }
blockquote p {
	margin: 0; }
~~~

![blockquote-style-border](/other/pic/blog-tmp/css-blockquote-4.png)

### 带背景的样式

~~~css
blockquote {
	margin: 1em 20px;
	padding-left: 50px;
	background: transparent url(http://www.gesep.com/uploads/News/admin/20130822/2013082217083237496.jpg) no-repeat; }
~~~

![blockquote-style-pic](/other/pic/blog-tmp/css-blockquote-5.png)

### 控制引用文字

控制引用文字莫非就是颜色粗体斜体那些. 这里使用`blockquote p:before/after`控制在文字的两端加入`"`.注意不是`blockquote:before/after`, 是专门针对引用的段落的(一般引用的文字其实是blockquote p以内的).

~~~css
blockquote {
	color: #66a;
	font-weight: bold;
	font-style: italic;
	margin: 1em 3em;
	padding-left: 1em;
	border-left: 5px solid #fce27c; }
blockquote p:before {
	content: '"'; }
blockquote p:after {
	content: '"'; }
~~~

![blockquote-style-p-font](/other/pic/blog-tmp/css-blockquote-7.png)

### 第一字符不同的式样

其实用到了引用段落`blockquote p`的伪元素`first-letter`和`first-line`来控制首字符/首行与众不同. 这里通过放大首字符到220% 来实现其占两行的效果. 并且要用到float和margin控制位置. 首行使用了文字样式的变化.

~~~css
blockquote {
	margin: 1em 2em;
	border-left: 1px dashed #999;
	padding-left: 1em; }
blockquote p:first-letter {
	float: left;
	margin: .2em .3em .1em 0;
	font-family: "Monotype Corsiva", "Apple Chancery", fantasy;
	font-size: 220%;
	font-weight: bold; }
blockquote p:first-line {
	font-variant: small-caps; }
~~~

![blockquote-style-firstletter](/other/pic/blog-tmp/css-blockquote-6.png)

## 伪元素 blockquote:before 和 blockquote:after

`blockquote:before/after`是引用(非引用文字!)的前后修饰的伪元素. 默认不显示出来. css加入以下内容后, 将会在引用之前和之后显示出一个引号 (类似于本博客旧样式所示). 更多效果和样式可参考ref1. 可以做到很fancy...

~~~css
blockquote:before {
 content: open-quote;
}
blockquote:after {
 content: close-quote;
}
~~~

## 博客引用形式测试

这里是本博客的变化.

### Old style: Same side

~~~css
blockquote,q{
	font:bold 21px/1.5 Consolas,"Courier New","KaiTi","KaiTi_GB2312","FangSong_GB2312",SimHei,arial,Monaco,monospace;
	color:#000;
	margin:2em;
	padding:0;
	max-width:80%;
	quotes:"\201C""\201D""\2018""\2019";
	background:#f9f9f9; }
q:before,blockquote:before{
	content:open-quote;
	font-size:2em;
	color:#ccc;
	line-height:.01em;
	margin-left:-.5em;
	vertical-align:-0.5em; }
q:after, blockquote:after{content:close-quote}
blockquote ol{margin:.2em;padding:0}
blockquote li{margin:.2em;padding:0}
~~~

效果: 

![blockquote-style-1](/other/pic/blog-tmp/css-blockquote-1.png)

### New style: Both sides

修改前后引号相对位置(position/float/top/bottom/margin-left/margin-right), 分开前后样式: 

~~~css
blockquote,q{
	font:bold 21px/1.5 Consolas,"Courier New","KaiTi","KaiTi_GB2312","FangSong_GB2312",SimHei,arial,Monaco,monospace;
	color:#000;
	margin:1em;
	margin-left:2em;
	margin-right:2em;
	padding:0;
	max-width:80%;
	quotes:"\201C""\201D""\2018""\2019";
	background:#f9f9f9; 
}
q:before,blockquote:before,q:after, blockquote:after{
	font-size:2em;
	color:#ccc;
	line-height:.01em;
	vertical-align:-0.5em;
}
q:before,blockquote:before{
	content:open-quote;
	top: 20px;
	float: left;
	position: relative;
	margin-left:-.8em;
}
q:after, blockquote:after{
	float: right;
 	position: relative;
	content:close-quote;
	bottom: 20px;
	margin-right:-.8em;
}
blockquote ol{margin:.2em;padding:0}
blockquote li{margin:.2em;padding:0}
~~~

效果: 

![blockquote-style-2](/other/pic/blog-tmp/css-blockquote-2.png)


### Other style: Long quote

只修改伪元素, 长条形的引用

~~~css
blockquote:before {
        content: open-quote;
        font-size: 24pt;
        text-align: center;
        line-height: 42px;
        color: #fff;
        background: #ddd;
        float: left;
        position: relative;
        top: 5px;
        margin-left:-0.8em;
}

blockquote:after {
        content: close-quote;
        font-size: 24pt;
        text-align: center;
        line-height: 42px;
        color: #fff;
        background: #ddd;
        float: right;
        position: relative;
        bottom: 65px;
        margin-right:-0.8em;
}
~~~

效果: 

![blockquote-style-3](/other/pic/blog-tmp/css-blockquote-3.png)

只修改伪元素, 圆形的引用: 

~~~css
q:before,blockquote:before{
	 content: open-quote;
	 font-size: 24pt;
	 text-align: center;
	 line-height: 42px;
	 color: #fff;
	 background: #ddd;
	 float: left;
	 position: relative;
	 top: 5px;
	 margin-left:-1em;
	 border-radius: 25px;
	 height: 25px;
	 width: 25px;
}
q:after,blockquote:after{
	 content: close-quote;
	 font-size: 24pt;
	 text-align: center;
	 line-height: 42px;
	 color: #fff;
	 background: #ddd;
	 float: right;
	 position: relative;
	 bottom: 50px;
	 margin-right:-1em;
	 border-radius: 25px;
	 height: 25px;
	 width: 25px;
}
~~~

效果: 

![blockquote-style-8](/other/pic/blog-tmp/css-blockquote-8.png)

## Reference

1. [理解 CSS 中的伪元素 :before 和 :after](http://www.cnblogs.com/oooweb/p/css-pseudo-element-before-and-after.html)
2. [CSS quotes Property](http://www.w3schools.com/cssref/pr_gen_quotes.asp)


------
