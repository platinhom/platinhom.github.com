---
layout: post
title: HTML5新控件元素的介绍
date: 2015-06-27 06:53:02
categories: Coding
tags: HTML Website
---

## 滑块控件 Range 对象
[Range](http://www.w3school.com.cn/jsref/dom_obj_range.asp)主代码`<input type="range">`. HTML5新元素.

~~~ html
<input type="range" id="myRange">

<p>点击按钮来获得滑块控件的值。</p>

<button onclick="myFunctionRange()">试一下</button>

<p id="demoRange"></p>

<script>
function myFunctionRange() {
    var x = document.getElementById("myRange").value;
    document.getElementById("demoRange").innerHTML = x;
}
</script>
~~~
<input type="range" id="myRange"><p>点击按钮来获得滑块控件的值。</p><button onclick="myFunctionRange()">试一下</button><p id="demoRange"></p><script>function myFunctionRange() {var x = document.getElementById("myRange").value;document.getElementById("demoRange").innerHTML = x;}</script>

## 数值选择 Number 控件
[Number](http://www.w3school.com.cn/jsref/dom_obj_number.asp)主代码:`<input type="number">`. HTML5新元素.

~~~ html
<input type="number" id="myNumber" value="2" max="10" min="-2">

<p>点击按钮来获得 number 字段的数字。</p>

<button onclick="myFunctionNumber()">试一下</button>

<p id="demoNumber"></p>

<script>
function myFunctionNumber() {
    var x = document.getElementById("myNumber").value;
    document.getElementById("demoNumber").innerHTML = x;
}
</script>
~~~

<input type="number" id="myNumber" value="2" max="10" min="-2"><p>点击按钮来获得 number 字段的数字。</p><button onclick="myFunctionNumber()">试一下</button><p id="demoNumber"></p><script>function myFunctionNumber() { var x = document.getElementById("myNumber").value; document.getElementById("demoNumber").innerHTML = x;}</script>

## 日期选择 Date 对象
[Date](http://www.w3school.com.cn/jsref/dom_obj_date.asp)主代码`<input type="date">` (HTML5才支持)

~~~ html
<input type="date" id="myDate" value="2014-06-01">

<p>点击按钮来获得 date 字段的日期。</p>

<button onclick="myFunctionDate()">试一下</button>

<p id="demoDate"></p>

<script>
function myFunctionDate() {
    var x = document.getElementById("myDate").value;
    document.getElementById("demoDate").innerHTML = x;
}
</script>
~~~

<input type="date" id="myDate" value="2014-06-01">

<p>点击按钮来获得 date 字段的日期。</p>

<button onclick="myFunctionDate()">试一下</button>

<p id="demoDate"></p>

<script>function myFunctionDate() {var x = document.getElementById("myDate").value;document.getElementById("demoDate").innerHTML = x;}</script>


## 拾色器 color 对象
[Color](http://www.w3school.com.cn/jsref/dom_obj_color.asp) 主代码: `<input type="color">`. HTML5新元素.

~~~ html
选择您喜爱的颜色：<input type="color" id="myColor">

<p>请点击按钮来获得颜色选择器的颜色。</p>

<p id="demoColor"></p>

<button onclick="myFunctionColor()">试一下</button>

<script>
function myFunctionColor() {
    var x = document.getElementById("myColor").value;
    document.getElementById("demoColor").innerHTML = x;
}
</script>
~~~

选择您喜爱的颜色：
<input type="color" id="myColor">
<p>请点击按钮来获得颜色选择器的颜色。</p>
<p id="demoColor"></p>
<button onclick="myFunctionColor()">试一下</button>

<script>function myFunctionColor(){var x = document.getElementById("myColor").value;document.getElementById("demoColor").innerHTML = x;}</script>


-------
比较次要不常用的元素..

## 网址 url 对象
[url](http://www.w3school.com.cn/jsref/dom_obj_url.asp) 主代码`<input type="url">` HTML5新元素.
形式和text输入框类似.

## 搜索 search 对象
[Search](http://www.w3school.com.cn/jsref/dom_obj_search.asp) 主代码`<input type="search">` HTML5新元素.
形式和text输入框类似.

## Email 对象
[Email]对象(http://www.w3school.com.cn/jsref/dom_obj_email.asp) 主代码`<input type="email">` HTML5新元素.
形式和text输入框类似.

---
