---
layout: post
title: Github使用ajax插入源码并prism着色
date: 2015-07-24 16:39:28
categories: Coding
tags: JS Git Website
---

在学完JQ和AJAX后知道怎么不借助PHP等调用和分析文件, 因此以前用来将代码复制过来再检查是否一致然后再更新内容的做法可以废弃了 ╮(╯▽╰)╭. 成功完成, 记录一下. 添加了`post_jq` 的layout, 以后直接复制pre code 块以及script语句块就OK了.

1. 加载JQuery
2. 设置一个空白的pre code 标签块,注意language后面设置语言,id随便设置一个,后面ajax需要
3. 直接利用ajax的load/get/post来获取文件内容.
4. 将内容后加载到pre code标签块内. 注意这个过程会晚于网页的加载,即晚于prism的解析.
5. 在回调函数中对Prism(或者别的着色器)进行重新调用语法解析.这里必须使用回调函数,否则语法解析会依然早于内容完成加载.


~~~html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>

<pre><code class="language-python" id="src"></code></pre>

<script>
$.get("/other/scripts/pqr2col.py",function(data,status){
	$("#src").html(data);
	//Reload all code highlight
	Prism.highlightAll();
	//Reload a elemennt code highlighting
	//Prism.highlightElement($('#src')[0]);
});
</script>
~~~

效果如下:

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>

<pre><code class="language-python" id="src"></code></pre>

<script>
$.get("/other/scripts/pqr2col.py",function(data,status){
	$("#src").html(data);
	Prism.highlightAll();
	//Prism.highlightElement($('#src')[0]);
});
</script>

## Reference
1. [How To Re-Run Prism.js On AJAX Content](http://schier.co/blog/2013/01/07/how-to-re-run-prismjs-on-ajax-content.html)

------
