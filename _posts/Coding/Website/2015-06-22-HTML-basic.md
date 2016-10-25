---
layout: post
title: HTML基础篇
date: 2015-06-21 20:37:29
categories: Coding
tags: Website HTML
---

新手可到[CodeCademy](http://www.codecademy.com/)进行简单的学习, [中文版地址](http://www.codecademy.com/zh).  
更详细的可到中文版的[w3school](http://www.w3school.com.cn/h.asp)进行学习!

HTML全称超文本标签语言,使用markup语言进行编写. 新一代的为HTML5,具有更多特性.

## 基础要素

### 基础知识
- `<**>` - `</**>` 标签（开始标签和结束标签），定义一系列内容，标签和内容组成一个html的元素。`<> </>`两者间为内容，`<>`内可加属性定义, 属性和标签名间加空格，内容`bgcolor="red"`这样，定义值为引号内，可用单引号或双引号。注意元素内的内容的多个连续空格会合并成一个，也会忽略你的换行等书写格式(此时需要`<br>`)。各种tag说明请参见**[w3c-tags](http://www.w3schools.com.cn/tags/)**
- `<** />` self-closing标签，无结束标签。例如`<br />` 不写`/`也行。
- `<! *****>`: 注释内容，新版用`<!--****-->`
- 要表达大于小于,请使用`&gt &lt`

### 主要要素：

- `<!DOCTYPE html>` : 标记为html语言，一般在第一行.
- `<html> </html>` : 主体部分,包含了head,body等. 一般如`<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en-us"> ... </html>`
- `<head> </head>` : 头信息，不被显示，可以放一些参数样式和js脚本等。主要是方便搜索引擎。
- `<body> </body>` : 主体, 显示的内容.
- `<footer> </footer>`: 页脚,底注.

head元素一般包括title，style，script,meta等

- `<title> </title>` : 网页标题。一般写在head内。基本要素之一.
- `<style> </style>`: 定义样式，和css文件一样写法。参看css文件。
- `<link />`: 定义载入连接文件，例如css：`<link type="text/css" rel="stylesheet" href="stylesheet.css" />`
- `<script> </script>`: 定义脚本,可外链或写在页面上. 加载外链如`<script type="text/javascript" src="/jsmol/JSmol.min.js"></script>`, type指明类型,当为JS时可以忽略.
- `<meta />`,用来储存一些不显示但可以被分析利用的数据.如`<meta http-equiv="content-type" content="text/html; charset=utf-8" /> <meta name="author" content="Hom" />`

### 页面基础元素：

- `<hr>`: 一条大横分隔线，无结束符。
- `<div> </div>`：分块,容器一种.块级元素.
- `<span> </span>`：将整体内容分各部分处理,不同span只占在一个块内,例如只占一行.一般用来控制不同样式.普通元素.
- `<p> </p>` : 段落元素, 其实就是上下空一行隔开内容.常用文字元素. 
- `<h1>`到`<h6>`: 标题元素，从1到6减小字体大小，加粗，上下留空。属性：align="center"
- `<img src=url/>`: 图片，无结束符。使用src属性指定图片，可以是本地或者超链接。
- `<a> </a>`: 锚标签，用来连接到别的地方。`<a>显示内容（可以是图片）</a>`.
	- `href`属性指定超链接，邮件可用`"mailto:abc@163.com?subject=Hello%20again"`这样子指定，注意?分隔内容。
	- `target="_blank" `属性将以新链接打开，target定义从什么地方打开连接地址。
	- `name`属性用来定义定义锚的名字，用`"#name"`进行业内跳转，也可以`url#name`来去某节跳转。
	- `text-decoration:none/underline`可以取消超链接的下划线
- `<li></li>`: 在有序和无序列表中的每一项内容.
- `<ol> </ol>`: 有序列表; 
- `<ul></ul>`: 无序列表，默认起始一个大点。每个项为一行，用`<li></li>`表示该项。li的前符号可用list-style-type定义
- `<table> </table>`:
	- `<thead> </thead>`和`<tbody> </tbody>`:头和主体(一般头是第一行)
	- `<tr></tr>`行`<tc></tc>`列
	- `<td> </td>`一般数据格，
	- `<th></th>`thead内用tr创建行后用来加首行的格内容；
	- 注意tbody用`align`属性可以全部整体align；`colspan="3", rowspan=3`属性进行单元格合并（适于th，td）；style很多，如`padding`; `border`(一个框),`border-left/right/bottom/top`:1px solid/dashed/dotted black/#123456; table有`border-collapse:collapse`. 范例:`<table border="1px"><thead><tr><th>name</th><th>age</th></tr></thead><tbody style="align:center"><tr><td>hom</td><td>30</td></tr></tbody></table>`

### 高级元素:

- `<button type="button" onclick="alert('Welcome!')">Text shown</button>`: 按钮;  
- `<input type="text" name="fname" />` : 输入框; 
- `<form> </form>` : 输入空键; 
- `<label for="male">Male</label> <input type="radio" name="sex" id="male" />`: 单选
- `<label><input name="Fruit" type="checkbox" value="" />苹果 </label>`: 复选 
- `<video src="/i/movie.ogg" controls="controls">Hi</video>` : 视频元素
- `<select><option value ="volvo">Volvo</option><option value ="saab">Saab</option></select>`: 下拉菜单

~~~ javascript
	var chkObjs = document.getElementsByName("SURFACE_METHOD");
    for(var i=0;i<chkObjs.length;i++){
        if(chkObjs[i].checked){
            stype=chkObjs[i].value;
            break;
        }
    }
~~~

## 格式控制：

### 简单HTML控制

- `<br>`: 换行
- `&nbsp`: 强制空格; `&amp` 相当于`&`; `&quot`双引号. 更多[特殊字符](https://www.utexas.edu/learn/html/spchar.html)参见.
- `<pre>`: 预格式化，就是按输入的内容显示，包括输入的多个空格、换行这些元素。一般在css中`pre code`这样去专门定义,更优先.
- `<b>` : 内容被加粗
- `<strong>`: 内容被强调，显示起来和bold一样，可以修改强调的格式。
- `<i>`:italic，斜体
- `<em>`: 强调，显示也是斜体
- `<del>`: 标记被删除（就是文字中间一横）
- `<ins>`: 标记为插入（就是下划线）
- `<big>`/`<small>`: 变大变小
- `<sup>`/`<sub>`:上下标
- `<code>/<kbd>/<tt>/<samp>/<var>`: 一般用来显示计算机输出结果。。
- `<address>`: 地址的格式，一般为斜体。
- `<abbr title="United Nations">UN</abbr>`: 缩写，鼠标移到UN上时显示缩写
- `<acronym title="World Wide Web">WWW</acronym>`: 首字母缩写, 和abbr差不多。
- `<bdo>`: 文字从右到左。。。
- `<q>`和`<blockquote>`: 小块引用（只加引号）和大块引用（新行，起始空几格）

![characters style](http://csis.pace.edu/~marchese/HTML/L1/logchrsty.jpg)
 
## 属性：

- `id`: 指明特定ID，用于CSS和JS操作.
- `class`: 指明属于某类型，用于CSS渲染.
- `title`: 效果像提示信息解释,如`<abbr>`.
- `align`: 水平对齐,top,bottom,center
- `valign`: 垂直对齐,top,bottom,center
- `style`: 放在标签内，格式为`style="name:value; name2:value2"` name例如:
	- `color`(green,[更多](http://www.w3.org/TR/css3-color/#svg-color)， 采用16进制6个数字，可搜[hex color picker](http://www.w3schools.com/tags/ref_colorpicker.asp)来辨认.
	- `font-size`(10px 无空格，或者用1em，em表示默认字体大小倍数，和硬件无关)
	- `font-weight`(bold)
	- `font-family`（Times,Arial,[更多](http://www.w3.org/TR/CSS21/fonts.html#generic-font-families),注意大小写敏感. css一般支持：serif, sans-serif, cursive草书； 可用`,`来分隔多个可能字体，因为不一定都支持，会按顺序选择字体，将serif等放最后.
	- `background-color`, white/black.., 底色.
	- `text-align`（center，left，right），文字对齐方法. justify分散对齐
	- `text-decoration`:none/underline. 针对超链接a(修饰为下划线)；
	- `width`,`height`: 宽和长.
	- `display`: `block` 默认竖排放置block；`inline-block`：横排放置block；`inline`：以最小尺寸横放，若为空会叠放一起，适合于`<p><h1>`等；`none`：不显示。
	- `margin/border/padding`:见下方图说明.margin控制内容边界和block边界的间距(也可理解为不同元素的间距),padding控制内容到边界间距.
	- `border`: `1px dashed black`同时设三者格式，其实对应子属性`border-width`,`border-style`, `border-color`；
	- `border-radius`表示块的四角的弯曲度(5px),100%时变成圆.
	- `margin`(auto,居中保持两边一致)；支持逐个输入,分别是`margin-top,margin-right,margin-bottom,margin-left`. 支持负值.
	- `float`：放置位置，left/right，会一个挨一个一行放置(不够位置就换行)，注意这个left/right是相对剩余空间而言。
	- `clear`:right/left/both 当有使用`float`的元素时，使用clear时，若有对应位置的float的元素，则换新行(取消float的同行设定)。
	- `right/left/top/bottom`相对位置偏移，针对核心部分，受position控制。
	- `position`：`static`(默认)/`absolute`/`relative`/`fixed`/`inherit` 子元素相对母元素的位置。static是默认的放置，不管left等的变化。absolute是相对非static的上级父元素的left时的位置，若没有则根据html的位置; relative是相对用static时的位置而言；fixed是固定位置，不受滚动条控制。
	- `z-index`：叠放时的优先序
	- `overflow`: 溢出后滚动条,一般auto就可以了.scroll就会一直在.

PS: margin控制边缘空白，padding控制和边界的距离，border为边界宽度。margin：auto为左右相等，即居中处理。1 2 3 4表示上右下左顺时针的距离，若只指明一个表示四面一样。也可以专用margin-top/right/bottom/left来指明。同理border和padding。注意padding会使用bgcolor。注意这些px值可以为负值，因为相对位置。

![boxdim](http://www.w3.org/TR/REC-CSS2/images/boxdim.gif) 

一些常用的字体. 名字大小写敏感. CSS最基础三种: serif, sans-serif, cursive.

![font-family](https://dhhmzgirqh63s.cloudfront.net/127.gif)

## JavaScript
HTML网页支持的脚本语言.基于Java语言开发.用于很多复制操作和调用. 这里不进行讨论了, 可以参加另外的Ref4教程.

- `document.writeln("context")`将内容写到html页面上.

## CSS：Cascading Style Sheets

- 选择器: `选择器 {属性 : 值；.....}` : 选择器一般是各种网页元素如p,img,div等,属性和值和一般style设置类似规则.
	- css注释和c一致，采用`/*  */`和`//`格式。
	- 多个选择器可以同时设置,此时使用`,`分隔,如`ol,ul,li{..}`.
	- `#id名`要是定义了id，可以用此来定义特点。
	- `.ClassName`要是定义了class,对应用此来指明类别特点.
	- `.bold` 将对bold特点体进行修饰.
	- 选择器若为某种标签，可根据**嵌套环境**作选择，例如div div p {...}这样。用`*`可以作通配所有选择器。
	- `div > p {....}` 强制直接相连，否则div li p {}也会受影响。
	- **优先级**: ID>Class>特点环境元素>一般元素>通配`*`  
- 准类选择器: `selector: pseudo-class-selector{...}` 准类选择器为更针对地对一些改变和行为的样式. 如: 
	- `hover`悬停,`link`未点击,`visited` 已点击,
	- `first-child`第一个满足条件的元素,`nth-child(n)`第N个满足的元素,类似地`last-child`. 
	- 注意`selector:nth-child(n)`和`selector :nth-child(n)`有区别，没有空格的前者是body中第n个的selector，有空格的后者是selector中第n个子元素。

~~~ css
selector {
	property: value;
}
p,span {
	font-size: 16px;
	font-family: Courier;
	//background-color: green;
}

#hello {
	color: #8B1C62;
}

.class {
	border:1px dashed black;
}

div ol > li {
	font-size: 10px;
}

p:nth-child(3){
	font-weight:bold;
}
~~~

## Reference
1. [html术语表](http://www.codecademy.com/zh/glossary/html)
2. [css术语表](http://www.codecademy.com/zh/glossary/css)
3. [w3school](http://www.w3schools.com/){: target="_parent"}
4. [Javascript基础篇](http://platinhom.github.io/2015/06/23/Javascript-basic/)
5. [HTML标签参考手册](http://www.w3school.com.cn/tags/index.asp){: target="_blank"}

---
