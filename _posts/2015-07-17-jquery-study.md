---
layout: post
title: JQuery学习笔记
date: 2015-07-16 17:20:07
categories: Coding
tags: JS
---

Jquery是JS的一个函数库,更为方便地进行HTML元素选取, HTML元素,操作CSS, 操作HTML, DOM 遍历和修改AJAX, 具有常用的事件函数JavaScript, 特效和动画HTML以及有更多Utilities.

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>

## 安装
1. 直接使用google CDN上提供的库([Link](https://developers.google.com/speed/libraries/#jquery))  
`*<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>`  
微软也提供: `<script src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.8.0.js"></script>`  
可以省略掉1.11.3后面的,例如1.11表示最新的1.11.x  
在线版的优势是用户之前可能加载过,所以打开网页就不用再加载了.
2. 直接下载下来放到服务器上  
两个版本,一个版本是常用的 *jquery.min.js* 精简压缩版和 *jquery-1.8.0.js* 测试开发版, 前者密密麻麻的,后者有序比较容易编辑.

## 基本语法

- 选取元素 `$(selector).action()`  
selector就是某种元素,CSS(前7种)和XPath(后几种)选择器的组合.action就是操作元素的函数.常用选择器:
	1. **this** 自身
	2. **"tagname"** 选取所有某种标签
	3. **".classname"** 选取所有类名的元素
	4. **"#idname"** 选取所有指定id的元素
	5. **"tagname#idname"** 选取某种标签下ID为指定的元素
	6. **"tagname.classname"** 选取某种标签下类名为指定的元素
	7. **"ul li:first"** 每个 \<ul\> 的第一个 \<li\> 元素
	7. **"[href]"** 所有带有href属性的元素
	8. **"[href='#']"** 选取所有带有 href 值等于 "#" 的元素。
	9. **"[href!='#']"** 选取所有带有 href 值不等于 "#" 的元素。
	10. **"[href$='.jpg']"** 选取所有 href 值以 ".jpg" 结尾的元素。 
- $和jQuery:  
实际`$`就是jQuery对象的简写.有时别的JS框架也使用`$`,此时要使用noConflict来处理.  
	1. `$.noConflict()`会释放`$`的控制, 使得别的框架可以使用.此时仍然可以使用`jQuery`进行调用.
	2. `var jq = $.noConflict();`可以将其存到一个变量内供使用.
	3. `$.noConflict();jQuery(document).ready(function($){$("button").click(function(){$("p").text("jQuery 仍在运行！");});});` 可以将`$`传给ready方法,这样jQuery代码块就可以继续使用`$`简写

## 事件
**$("button").action(function() {..some code... } )**

1. 把所有 jQuery 代码置于事件处理函数中
1. 把所有事件处理函数置于文档就绪事件(*$(document).ready*)处理器中
1. 把 jQuery 代码置于单独的 **.js** 文件中
1. 如果存在名称冲突(`jQuery.noConflict()` 判断)，则重命名 jQuery 库

- `$(document).ready(function)` 将函数绑定到文档的就绪事件（当文档完成加载时）
- `$(selector).click(function)` 触发或将函数绑定到被选元素的点击事件
- `$(selector).dblclick(function)` 触发或将函数绑定到被选元素的双击事件
- `$(selector).focus(function)` 触发或将函数绑定到被选元素的获得焦点事件
- `$(selector).mouseover(function)` 触发或将函数绑定到被选元素的鼠标悬停事件

## 获取返回和设置DOM

- `html([content])` 返回或设置标签innerHTML的内容(包括html标记)
- `text([content])` 返回或设置标签文本内容, 其实是innerHTML的实际显示
- `val([value])` 返回或设置标签的value值
- `attr(attrname[,value])` 返回或设置指定属性attrname的值. 支持`attr({a1:v1,a2,v2..})`来同时设置多个属性
- `append("...")` 在元素内容的最后追加内容
- `prepend("...")` 在元素内容前追加内容
- `after("..")` 在元素后追加内容, 内容一般是html代码
- `before("..")` 在元素前追加内容, 内容一般是html代码
- `remove([selector])` 删除整个元素及子元素, 也可以只删除selector符合的某些元素及子元素
- `empty()` 清空子元素

## 回调函数Callback和串联Chaining
- 回调如 *$(selector).hide(10000,callback)* 中,如果把回调函数内容放在hide的后面单独进行,则没等hide完成就会执行,有时下一个动作依赖于上一个的结果,此时需要等待上一个结果才能再进行. 要是连续进行时处理.
- 串联如 *$("#p1").css("color","red").slideUp(2000).slideDown(2000);* 一个动作一个动作执行

## 遍历
- `parent()` 返回上级父对象
- `parents([selector])` 返回所有父对象或者满足selector的父对象
- `parentsUntil(selector)` 返回对象到指定另一父对象之间的对象
- `children([selector])` 返回所有直接的子对象,也可以进行过滤
- `find(selector)` 返回所有子级元素满足selector的.所有返回用"*".
- `siblings([selector])` 返回所有同胞(同级)元素或进行过滤
- `next()` 下一个同胞元素
- `nextAll()` 后面的所有同胞元素
- `nextUntil(sel)` 两个同胞元素间的所有同胞元素
- `prev()` 上一个同胞元素
- `prevAll()` 前面的所有同胞元素
- `prevUntil(sel)` 两个同胞元素间的所有同胞元素
- `first(), last() 和 eq(n)` 返回在选取器多个满足结果或上次结果中的第一个/最后一个/第N个元素
- `filter(sel) 和 not(sel)`返回满足/不满足sel条件的结果

## Jquery常用函数
所有JQ的函数都放在 *$(document).ready(function(){...});* 内,防止提前加载函数.

- `css("property","value")` 设置css属性,不写值可以返回属性.多个css可以用`{p1:v1,p2:v2...}`
- `addClass/removeClass/toggleClass(classname)` 添加/删除/切换添加删除类属性.类属性可以在css控制
- `width()/height()` 返回宽和高.还有`innerWidth`,`outerWidth`等
- `hide/show/toggle([speed,callback])` 隐藏/显示/切换显示隐藏元素,speed可以设置隐藏需要的时间(ms),可以`"slow"`,`"fast"`.
- `fadeIn/fadeOut/fadeToggle(speed,callback)` 淡入/淡出/切换淡入淡出,速度ms.
- `fadeTo(speed,opacity,callback)` 渐变为一定不透明度(0~1),越大越不透明
- `slideDown/slideUp/slideToggle(speed,callback)` 向下滑动/收回/切换滑动元素
- `animate({params},speed,callback)` 根据给定CSS进行动画变化,params是Camel 标记法的CSS. [介绍](http://www.w3school.com.cn/jquery/jquery_animate.asp)
- `stop(stopAll,goToEnd)` 停止动画.第一参数是是否全部停止还是挺过该步而已;第二参数是是否直接跳到结尾.均为false.



## Reference
1. [Jquery选择器参考手册](http://www.w3school.com.cn/jquery/jquery_ref_selectors.asp)
2. [JQuery事件参考手册](http://www.w3school.com.cn/jquery/jquery_ref_events.asp)
3. [JQuery文档操作参考手册](http://www.w3school.com.cn/jquery/jquery_ref_manipulation.asp)
4. [JQuery效果参考手册](http://www.w3school.com.cn/jquery/jquery_ref_effects.asp)
5. [JQuery属性操作参考手册](http://www.w3school.com.cn/jquery/jquery_ref_attributes.asp)
6. [JQuery CSS操作参考手册](http://www.w3school.com.cn/jquery/jquery_ref_css.asp)
7. [JQuery遍历参考手册](http://www.w3school.com.cn/jquery/jquery_ref_traversing.asp)

------
