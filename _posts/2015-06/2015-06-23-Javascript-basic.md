---
layout: post_small
title: Javascript基础篇
date: 2015-06-22 22:47:49
categories: Coding
tags: JS
---

JavaScript 是属于网络的轻量级脚本语言,可以直接插入HTML页面中使用, 因此被数百万计的网页用来改进设计、验证表单、检测浏览器、创建cookies以及更多的应用,是因特网上最流行的脚本语言。
Javasciprt使用浏览器即可运行和查看结果,不需另装任何解析器! JavaScript和Java语法类似,但是完全是两种不同的语言.  

JavaScript 是面向对象的语言，但JS不使用类。在JS中，不会创建类，也不会通过类来创建对象（就像在其他面向对象的语言中那样）。JavaScript 基于 prototype，而不是基于类的.

在HTML中使用外链(`src="/*.js"`)或者内嵌的方法引入JS.例如下面的例子. 其中. HTML type默认是JS, 所以可以不写.

~~~ html
<!--外链-->
<script type="text/javascript" src="/jsmol/JSmol.min.js"></script>
<!--内嵌-->
<script type="text/javascript">
var hello;
</script>
~~~

测试和练习十分容易, 新建一个txt文件,改名为test.html, 文本编辑器打开后, 写入以下基本信息.在中间填入指令, 并用浏览器打开刷新即可.

~~~ html
<!DOCTYPE html>
<html lang="zh-cn">
<head>
<meta charset="utf-8" />
</head>
<body>
<p> This is a test for javascript! </p>
<script type="text/javascript">



</script>
<button type="button" onclick="alert('Welcome!')">点击这里测试</button>
</body>
</html>
~~~

JS的内容会在页面加载时加载. 事件发生时动作可以利用函数来调用. 通过事件来操作页面元素是JS重要的作用.


## 基础知识

- 分割语句`;`,注释`//`和`/* comment */`, 大小写敏感, 字符串`' '`和`" "`相等. null空值清空变量; undefined是没赋值.
- 基础对象: `String`[字符串型](http://www.w3school.com.cn/jsref/jsref_obj_string.asp); [数字类型](http://www.w3school.com.cn/jsref/jsref_obj_number.asp)只有一种浮点类型`Number`,可以用科学计数法`y=123e-5`,支持8/16进制`0577,0x1f`;`Boolean`[布尔型](http://www.w3school.com.cn/jsref/jsref_obj_Boolean.asp)`true/false`;
- 内置对象: `Date`[日期型](http://www.w3school.com.cn/jsref/jsref_obj_date.asp); `Array`[数组型](http://www.w3school.com.cn/jsref/jsref_obj_array.asp); `Math` [数学型](http://www.w3school.com.cn/jsref/jsref_obj_math.asp); `Regexp`[正则表达式类型](http://www.w3school.com.cn/jsref/jsref_obj_regexp.asp); `Event`[事件类型](http://www.w3school.com.cn/jsref/jsref_events.asp) (其实就是各种相应罢了,不怎么算对象); `Object` 对象型; `Function`[函数型](http://www.w3school.com.cn/jsref/jsref_obj_global.asp).
- 浏览器对象: `Window` [窗口对象](http://www.w3school.com.cn/jsref/dom_obj_window.asp); `Navigator`[浏览器对象](http://www.w3school.com.cn/jsref/dom_obj_navigator.asp); `Screen` [显示屏对象](http://www.w3school.com.cn/jsref/dom_obj_screen.asp); `History` [浏览历史记录对象](http://www.w3school.com.cn/jsref/dom_obj_history.asp); `Location` [网站地址对象](http://www.w3school.com.cn/jsref/dom_obj_location.asp)
- 变量 `var v1=1,v2="age";` var万能的动态类型. 全局变量(在函数外声明的)生存期是页面; 局部变量是函数结束. 函数内使用 `vname=value` 不声明就赋值的会被作为全局变量.
- 数组,`var=new Array();var[0]=1;var[1]=2;`也可以`=new Array(1,2)`或`=[1,2]`.数组下标`0`开始.
- 字典, 本质是数组,也是对象. `var a = new Array(); a['hi']=1;a['hh']=2;`也可以用`var a={"hi":1,"hh":2};`. 可以用`for (var key in ary)`作循环. 字典的key既可以作为key,也可以作为对象的属性 *a.hi*. 字典的length属性不起效..
- 对象(`Object`), `var person={name:"Bill", id:5566};`,调用属性`person.name;person["name"];`,方法类似. 对象当然还有方法了. Java的想法: 一切皆对象. 利用函数构造`function person(name,age){this.name=name;this.age=age;}`(对象构造器,this是自身);`this.changeName=changeName;function changeName(name){this.lastname=name;}` 对象内创建方法.
- 函数 `function fname([var1,var2]){..}`, 可以`return var1;`返回值.JS居然不支持参数默认值方法..
- 运算: 和C类似,支持`%`求余,`++`累加,`+=`自运算.
- 字符串: 连接也是用加号. 数字和字符串相加,数字会转为字符串再处理.
- 比较: `==`等于(5=="5"是对),`===`全等于(值和类型),`!=`不等于, `>,>=`, `&&`与,`||`或,`!`非. 
- 条件句: `if (){;} else if {;} else {;}`; `switch(var1){case val1: {;} break; default:{;}}`; 三目: `var1=(condition)?trueValue:falseValue`
- 循环: `for (var i=0;循环条件;i++){;}`; `for (x in person){;}`遍历对象属性(x此时为属性名); `while (循环条件){;}`和`do {;} while (循环条件)` 先判后做和先做后判; `break`和`continue`;
- 标签: `labelname: {..;break/continue labelname;..}` 可用于跳出指定代码块.
- 错误: `try{;} catch(err){;}` 测试并捕获. `throw exception` 抛出错误,一般是字符串.

## HTML DOM
DOM就是document objective model.就是HTML各个元素对象. JS可以操控他们, 通过id,标签名,类名来找到元素, 并可以改变他们的元素,属性,css,对事件作出反应. 更多事件[参考](http://www.w3school.com.cn/jsref/dom_obj_event.asp).

- `x=document.getElementById("demo")` : 获取元素
- `var y=x.getElementsByTagName("p");` : 在获取元素后使用tag名来获取子元素(所有子元素).
- `document.write("");` : 写入内容到网页,加载完网页后执行,会覆盖网页...
- `document.getElementById("p1").innerHTML="New_Val"`: 改变其HTML内容.
- `document.getElementById(id).attribute=new_value`: 改变属性值
- `document.getElementById("p2").style.color="blue"` 改变样式.
- `document.getElementById("myBtn").onclick=function(){displayDate()};` 对事件做响应,这里通过调用元素事件完成. 
- `document.getElementsByName("name")` 通过元素名来获取元素,可能是个多对象的数组.
- `document.createElement("p");` 创建元素(节点)
- `document.createTextNode("这是新段落。");`创建元素内容
- `para.appendChild(node);div1.appendChild(para)` 向元素添加内容,再把元素放到父元素里
- `child.parentNode.removeChild(child);` 删除子元素.这里通过调用父元素属性再实现移除.

- `<h1 onclick="changetext(this)">请点击该文本</h1>` 对事件作出响应,这里调用函数完成,函数中参数是id,这里this就是该元素.
- `<body onload="checkCookies()">` onload事件就是页面加载时做的东东,`onunload`是离开页面做的.经常用于cookie处理,检查浏览器等.
- `<input type="text" id="fname" onchange="upperCase()">` onchange事件是离开输入框/按下确定时的[事件](http://www.w3school.com.cn/tiy/t.asp?f=js_dom_event_onchange).
- `<div onmouseover="mOver(this)" onmouseout="mOut(this)">` onmouseover/out是鼠标移入和移出事件,相应不同函数.
- `onmousedown, onmouseup` 这两个事件对应鼠标按下和释放的事件.和onclick相关

## 常用属性和方法

### 全局对象(属性和方法)

 | Infinity | 代表正的无穷大的数值。 | 
 | java | 代表 java.* 包层级的一个 JavaPackage。 | 
 | NaN | 指示某个值是不是数字值。 | 
 | Packages | 根 JavaPackage 对象。 | 
 | undefined | 指示未定义的值。 | 

- [decodeURI()](http://www.w3school.com.cn/jsref/jsref_decodeURI.asp) : 解码某个编码的 URI。
- [decodeURIComponent()](http://www.w3school.com.cn/jsref/jsref_decodeURIComponent.asp) : 解码一个编码的 URI 组件。
- [encodeURI()](http://www.w3school.com.cn/jsref/jsref_encodeuri.asp) : 把字符串编码为 URI。
- [encodeURIComponent()](http://www.w3school.com.cn/jsref/jsref_encodeURIComponent.asp) : 把字符串编码为 URI 组件。
- [escape(str)](http://www.w3school.com.cn/jsref/jsref_escape.asp) : 将字符串转为网址那种编码.被废弃,应该用encodeURI()和encodeURIComponent()来代替.
- [eval()](http://www.w3school.com.cn/jsref/jsref_eval.asp) : 计算 JavaScript 字符串，并把它作为脚本代码来执行。
- [getClass()](http://www.w3school.com.cn/jsref/jsref_getClass.asp) : 返回一个 JavaObject 的 JavaClass。
- [isFinite()](http://www.w3school.com.cn/jsref/jsref_isFinite.asp) : 检查某个值是否为有穷大的数。
- [isNaN()](http://www.w3school.com.cn/jsref/jsref_isNaN.asp) : 检查某个值是否是数字。
- [Number()](http://www.w3school.com.cn/jsref/jsref_number.asp) : 把对象的值转换为数字。
- [parseFloat()](http://www.w3school.com.cn/jsref/jsref_parseFloat.asp) : 解析一个字符串并返回一个浮点数。
- [parseInt()](http://www.w3school.com.cn/jsref/jsref_parseInt.asp) : 解析一个字符串并返回一个整数。
- [String()](http://www.w3school.com.cn/jsref/jsref_string.asp) : 把对象的值转换为字符串。
- [unescape()](http://www.w3school.com.cn/jsref/jsref_unescape.asp) : 对由 escape() 编码的字符串进行解码。

### Number对象

 | constructor | 返回对创建此对象的 Number 函数的引用。 | 
 | MAX_VALUE | 可表示的最大的数。 | 
 | MIN_VALUE | 可表示的最小的数。 | 
 | NaN | 非数字值。 | 
 | NEGATIVE_INFINITY | 负无穷大，溢出时返回该值。 | 
 | POSITIVE_INFINITY | 正无穷大，溢出时返回该值。 | 
 | prototype | 使您有能力向对象添加属性和方法。 | 

- [toString(radix)](http://www.w3school.com.cn/jsref/jsref_tostring_number.asp) : 把数字转换为字符串，使用指定的基数(默认10,10进制)。
- [toLocaleString()](http://www.w3school.com.cn/jsref/jsref_tolocalestring_number.asp) : 把数字转换为字符串，使用本地数字格式顺序。
- [toFixed(num)](http://www.w3school.com.cn/jsref/jsref_tofixed.asp) : 把数字转换为字符串，结果的小数点后有指定位数的数字。num是小数位数,0~20. 会四舍五入.
- [toExponential(num)](http://www.w3school.com.cn/jsref/jsref_toexponential.asp) : 把对象的值转换为指数计数法。num是小数位数,0~20.
- [toPrecision(num)](http://www.w3school.com.cn/jsref/jsref_toprecision.asp) : 把数字格式化为指定的长度指数计数法。num是小数位数,1~21. 一般用于大整数.
- [valueOf](http://www.w3school.com.cn/jsref/jsref_valueof_number.asp) : 返回一个 Number 对象的基本数字值。

### 字符串对象

- `str.length` 返回长度
- [anchor()](http://www.w3school.com.cn/jsref/jsref_anchor.asp) : 创建 HTML 锚。
- [big()](http://www.w3school.com.cn/jsref/jsref_big.asp) : 用大号字体显示字符串。
- [blink()](http://www.w3school.com.cn/jsref/jsref_blink.asp) : 显示闪动字符串。
- [bold()](http://www.w3school.com.cn/jsref/jsref_bold.asp) : 使用粗体显示字符串。
- [charAt()](http://www.w3school.com.cn/jsref/jsref_charAt.asp) : 返回在指定位置的字符。
- [charCodeAt()](http://www.w3school.com.cn/jsref/jsref_charCodeAt.asp) : 返回在指定的位置的字符的 Unicode 编码。
- [concat()](http://www.w3school.com.cn/jsref/jsref_concat_string.asp) : 连接字符串。
- [fixed()](http://www.w3school.com.cn/jsref/jsref_fixed.asp) : 以打字机文本显示字符串。
- [fontcolor()](http://www.w3school.com.cn/jsref/jsref_fontcolor.asp) : 使用指定的颜色来显示字符串。
- [fontsize()](http://www.w3school.com.cn/jsref/jsref_fontsize.asp) : 使用指定的尺寸来显示字符串。
- [fromCharCode()](http://www.w3school.com.cn/jsref/jsref_fromCharCode.asp) : 从字符编码创建一个字符串。
- [indexOf(str2[,start])](http://www.w3school.com.cn/jsref/jsref_indexOf.asp) : 检索字符串。从start位开始(默认0)搜索str2,找到后返回首个匹配字母的索引,没找到返回-1.
- [italics()](http://www.w3school.com.cn/jsref/jsref_italics.asp) : 使用斜体显示字符串。
- [lastIndexOf()](http://www.w3school.com.cn/jsref/jsref_lastIndexOf.asp) : 从后向前搜索字符串。
- [link()](http://www.w3school.com.cn/jsref/jsref_link.asp) : 将字符串显示为链接。
- [localeCompare()](http://www.w3school.com.cn/jsref/jsref_localeCompare.asp) : 用本地特定的顺序来比较两个字符串。
- [match()](http://www.w3school.com.cn/jsref/jsref_match.asp) : 找到一个或多个正则表达式/子串的匹配。
- [replace(regexp/substr,replacement)](http://www.w3school.com.cn/jsref/jsref_replace.asp) : 替换与正则表达式匹配的子串。
- [search()](http://www.w3school.com.cn/jsref/jsref_search.asp) : 检索与正则表达式相匹配的值。
- [slice()](http://www.w3school.com.cn/jsref/jsref_slice_string.asp) : 提取字符串的片断，并在新的字符串中返回被提取的部分。
- [small()](http://www.w3school.com.cn/jsref/jsref_small.asp) : 使用小字号来显示字符串。
- [split(separator,max)](http://www.w3school.com.cn/jsref/jsref_split.asp) : 把字符串分割为字符串数组。必须指明分隔符. max是最大分的次数,默认无穷.
- [strike()](http://www.w3school.com.cn/jsref/jsref_strike.asp) : 使用删除线来显示字符串。
- [sub()](http://www.w3school.com.cn/jsref/jsref_sub.asp) : 把字符串显示为下标。
- [substr(start[,len])](http://www.w3school.com.cn/jsref/jsref_substr.asp) : 从起始索引号提取字符串中指定数目的字符。从start开始长度为len. 注意序号0开始,支持-1负数表示从后倒数起.len省略则返回到结尾.
- [substring(x,y)](http://www.w3school.com.cn/jsref/jsref_substring.asp) : 提取字符串中两个指定的索引号之间的字符。和python的语法类似,0开始[x,y)返回x+1到y的子串.
- [sup()](http://www.w3school.com.cn/jsref/jsref_sup.asp) : 把字符串显示为上标。
- [toLocaleLowerCase()](http://www.w3school.com.cn/jsref/jsref_toLocaleLowerCase.asp) : 把字符串转换为小写。
- [toLocaleUpperCase()](http://www.w3school.com.cn/jsref/jsref_toLocaleUpperCase.asp) : 把字符串转换为大写。
- [toLowerCase()](http://www.w3school.com.cn/jsref/jsref_toLowerCase.asp) : 把字符串转换为小写。
- [toUpperCase()](http://www.w3school.com.cn/jsref/jsref_toUpperCase.asp) : 把字符串转换为大写。
- [toString()](http://www.w3school.com.cn/jsref/jsref_toString_string.asp) : 返回字符串。
- [valueOf()](http://www.w3school.com.cn/jsref/jsref_valueOf_string.asp) : 返回某个字符串对象的原始值。
- toSource()	代表对象的源代码。

## 数组

- `ary.length` 返回数组的长度
- [concat(arrayX,arrayY,......)](http://www.w3school.com.cn/jsref/jsref_concat_array.asp) : 连接两个或更多的数组，并返回结果。
- [join([separator])](http://www.w3school.com.cn/jsref/jsref_join.asp) : 把数组的所有元素放入一个字符串。元素通过指定的分隔符进行分隔。默认分隔符`,`
- [pop()](http://www.w3school.com.cn/jsref/jsref_pop.asp) : 删除并返回数组的最后一个元素
- [push(ele....)](http://www.w3school.com.cn/jsref/jsref_push.asp) : 向数组的末尾添加一个或更多元素，并返回新的长度。
- [reverse()](http://www.w3school.com.cn/jsref/jsref_reverse.asp) : 颠倒数组中元素的顺序。改变数组而非返回新数组
- [shift(ele....)](http://www.w3school.com.cn/jsref/jsref_shift.asp) : 删除并返回数组的第一个元素
- [slice(start,end)](http://www.w3school.com.cn/jsref/jsref_slice_array.asp) : 从某个已有的数组返回选定的元素, 分片.支持负数
- [sort()](http://www.w3school.com.cn/jsref/jsref_sort.asp) : 对数组的元素进行排序
- [splice(index,N,ele....)](http://www.w3school.com.cn/jsref/jsref_splice.asp) : 从数组中index开始(可以负数)删除N个元素,N=0则不删除只增加.ele是要添加的元素. 改变原来数组,返回删除的项目.`ary.splice(0,ary.length);`清空数组,和`ary=[]`;一样
- [toSource()](http://www.w3school.com.cn/jsref/jsref_tosource_array.asp) : 返回该对象的源代码。很多浏览器不支持.
- [toString()](http://www.w3school.com.cn/jsref/jsref_toString_array.asp) : 把数组转换为字符串，并返回结果。自动用`,`连接
- [toLocaleString()](http://www.w3school.com.cn/jsref/jsref_toLocaleString_array.asp) : 把数组转换为本地数组，并返回结果。
- [unshift(ele....)](http://www.w3school.com.cn/jsref/jsref_unshift.asp) : 向数组的开头添加一个或更多元素，并返回新的长度。
- [valueOf()](http://www.w3school.com.cn/jsref/jsref_valueof_array.asp) : 返回数组对象的原始值
- `ary.hasOwnProperty(key);` 字典判断是否有键值.返回true/false
- `$.inArray("value", ary);` 检查数组是否有值,返回所在位置(0起),没有则返回-1.

### Math对象方法

 | E | 返回算术常量 e，即自然对数的底数（约等于2.718）。 | 
 | LN2 | 返回 2 的自然对数（约等于0.693）。 | 
 | LN10 | 返回 10 的自然对数（约等于2.302）。 | 
 | LOG2E | 返回以 2 为底的 e 的对数（约等于 1.414）。 | 
 | LOG10E | 返回以 10 为底的 e 的对数（约等于0.434）。 | 
 | PI | 返回圆周率（约等于3.14159）。 | 
 | SQRT1_2 | 返回返回 2 的平方根的倒数（约等于 0.707）。 | 
 | SQRT2 | 返回 2 的平方根（约等于 1.414）。 | 

- [abs(x)](http://www.w3school.com.cn/jsref/jsref_abs.asp) : 返回数的绝对值。
- [acos(x)](http://www.w3school.com.cn/jsref/jsref_acos.asp) : 返回数的反余弦值。
- [asin(x)](http://www.w3school.com.cn/jsref/jsref_asin.asp) : 返回数的反正弦值。
- [atan(x)](http://www.w3school.com.cn/jsref/jsref_atan.asp) : 以介于 -PI/2 与 PI/2 弧度之间的数值来返回 x 的反正切值。
- [atan2(y,x)](http://www.w3school.com.cn/jsref/jsref_atan2.asp) : 返回从 x 轴到点 (x,y) 的角度（介于 -PI/2 与 PI/2 弧度之间）。
- [ceil(x)](http://www.w3school.com.cn/jsref/jsref_ceil.asp) : 对数进行上舍入。
- [cos(x)](http://www.w3school.com.cn/jsref/jsref_cos.asp) : 返回数的余弦。
- [exp(x)](http://www.w3school.com.cn/jsref/jsref_exp.asp) : 返回 e 的指数。
- [floor(x)](http://www.w3school.com.cn/jsref/jsref_floor.asp) : 对数进行下舍入。
- [log(x)](http://www.w3school.com.cn/jsref/jsref_log.asp) : 返回数的自然对数（底为e）。
- [max(x,y)](http://www.w3school.com.cn/jsref/jsref_max.asp) : 返回 x 和 y 中的最高值。
- [min(x,y)](http://www.w3school.com.cn/jsref/jsref_min.asp) : 返回 x 和 y 中的最低值。
- [pow(x,y)](http://www.w3school.com.cn/jsref/jsref_pow.asp) : 返回 x 的 y 次幂。
- [random()](http://www.w3school.com.cn/jsref/jsref_random.asp) : 返回 0 ~ 1 之间的随机数。
- [round(x)](http://www.w3school.com.cn/jsref/jsref_round.asp) : 把数四舍五入为最接近的整数。
- [sin(x)](http://www.w3school.com.cn/jsref/jsref_sin.asp) : 返回数的正弦。
- [sqrt(x)](http://www.w3school.com.cn/jsref/jsref_sqrt.asp) : 返回数的平方根。
- [tan(x)](http://www.w3school.com.cn/jsref/jsref_tan.asp) : 返回角的正切。
- [toSource()](http://www.w3school.com.cn/jsref/jsref_tosource_math.asp) : 返回该对象的源代码。
- [valueOf()](http://www.w3school.com.cn/jsref/jsref_valueof_math.asp) : 返回 Math 对象的原始值。

### 事件参考

onabort | 图像加载被中断 | onblur | 元素失去焦点 
onchange | 用户改变域的内容 | onclick | 鼠标点击某个对象 
ondblclick | 鼠标双击某个对象 | onerror | 当加载文档或图像时发生某个错误 
onfocus | 元素获得焦点 | onkeydown | 某个键盘的键被按下 
onkeypress | 某个键盘的键被按下或按住 | onkeyup | 某个键盘的键被松开 
onload | 某个页面或图像被完成加载 | onmousedown | 某个鼠标按键被按下 
onmousemove | 鼠标被移动 | onmouseout | 鼠标从某元素移开 
onmouseover | 鼠标被移到某元素之上 | onmouseup | 某个鼠标按键被松开 
onreset | 重置按钮被点击 | onresize | 窗口或框架被调整尺寸
onselect | 文本被选定 | onsubmit | 提交按钮被点击 
onunload | 用户退出页面 | . | .

## JS常用浏览器对象方法

- `alert('Welcome!')` : 弹出提示框
- `confirm(str);`:弹出对话框,提示字符串str,返回true/false(确定/取消)
- `prompt(str1, str2);`: 提问对话框,可输入值.str1是提示信息,str2是预设内容.按确定返回输入字符串,取消null.
- `console.log(command)` 执行命令后将结果返回到控制台.控制台要另外在浏览器调用.

### Screen对象

- `screen.availHeight` : 返回显示屏幕的高度 (除 Windows 任务栏之外)。
- `screen.availWidth` : 返回显示屏幕的宽度 (除 Windows 任务栏之外)。
- `screen.bufferDepth` : 设置或返回调色板的比特深度。
- `screen.colorDepth` : 返回目标设备或缓冲器上的调色板的比特深度。
- `screen.deviceXDPI` : 返回显示屏幕的每英寸水平点数。
- `screen.deviceYDPI` : 返回显示屏幕的每英寸垂直点数。
- `screen.fontSmoothingEnabled` : 返回用户是否在显示控制面板中启用了字体平滑。
- `screen.height` : 返回显示屏幕的高度。
- `screen.logicalXDPI` : 返回显示屏幕每英寸的水平方向的常规点数。
- `screen.logicalYDPI` : 返回显示屏幕每英寸的垂直方向的常规点数。
- `screen.pixelDepth` : 返回显示屏幕的颜色分辨率（比特每像素）。
- `screen.updateInterval` : 设置或返回屏幕的刷新率。
- `screen.width` : 返回显示器屏幕的宽度。

### Location对象(Window对象的属性)

- `location.hash` : 设置或返回从井号 (#) 开始的 URL（锚）。
- `location.host` : 设置或返回主机名和当前 URL 的端口号。
- `location.hostname` : 设置或返回当前 URL 的主机名。
- `location.href` : 设置或返回完整的 URL。
- `location.pathname` : 设置或返回当前 URL 的路径部分。
- `location.port` : 设置或返回当前 URL 的端口号。
- `location.protocol` : 设置或返回当前 URL 的协议。
- `location.search` : 设置或返回从问号 (?) 开始的 URL（查询部分）。
- `location.assign(URL)` : 加载新的文档。
- `location.reload([force])` : 重新加载当前文档,相当于刷新。force为true/false,是否强制刷新,默认false时若服务器网页没修改则从缓存加载
- `location.replace(newURL)` : 用新的文档替换当前文档。不会产生新历史记录而是直接覆盖当前历史记录.

### Window对象

- `window.frames[]` : 返回窗口中所有命名的框架。该集合是 Window 对象的数组，每个 Window 对象在窗口中含有一个框架或 <iframe>。
- `window.closed` : 返回窗口是否已被关闭。
- `window.defaultStatus` : 设置或返回窗口状态栏中的默认文本。
- `window.document` : 对 Document 对象的只读引用。请参阅 Document 对象。
- `window.history` : 对 History 对象的只读引用。请参数 History 对象。
- `window.innerheight` : 返回窗口的文档显示区的高度。
- `window.innerwidth` : 返回窗口的文档显示区的宽度。
- `window.length` : 设置或返回窗口中的框架数量。
- `window.location` : 用于窗口或框架的 Location 对象。请参阅 Location 对象。
- `window.name` : 设置或返回窗口的名称。
- `window.Navigator` : 对 Navigator 对象的只读引用。请参数 Navigator 对象。
- `window.opener` : 返回对创建此窗口的窗口的引用。
- `window.outerheight` : 返回窗口的外部高度。
- `window.outerwidth` : 返回窗口的外部宽度。
- `window.pageXOffset` : 设置或返回当前页面相对于窗口显示区左上角的 X 位置。
- `window.pageYOffset` : 设置或返回当前页面相对于窗口显示区左上角的 Y 位置。
- `window.parent` : 返回父窗口。
- `window.Screen` : 对 Screen 对象的只读引用。请参数 Screen 对象。
- `window.self` : 返回对当前窗口的引用。等价于 Window 属性。
- `window.status` : 设置窗口状态栏的文本。
- `window.top` : 返回最顶层的先辈窗口。
- `window.window` : window 属性等价于 self 属性，它包含了对窗口自身的引用。
- `window.screenLeft`,`window.screenTop`,`window.screenX`,`window.screenY` : 只读整数。声明了窗口的左上角在屏幕上的的 x 坐标和 y 坐标。IE、Safari 和 Opera 支持 screenLeft 和 screenTop，而 Firefox 和 Safari 支持 screenX 和 screenY。
- [window.alert()](http://www.w3school.com.cn/jsref/met_win_alert.asp) : 显示带有一段消息和一个确认按钮的警告框。
- [window.blur()](http://www.w3school.com.cn/jsref/met_win_blur.asp) : 把键盘焦点从顶层窗口移开。
- [window.clearInterval()](http://www.w3school.com.cn/jsref/met_win_clearinterval.asp) : 取消由 setInterval() 设置的 timeout。
- [window.clearTimeout()](http://www.w3school.com.cn/jsref/met_win_cleartimeout.asp) : 取消由 setTimeout() 方法设置的 timeout。
- [window.close()](http://www.w3school.com.cn/jsref/met_win_close.asp) : 关闭浏览器窗口。这里window也可以是window.open打开后的返回值窗口变量.
- [window.confirm()](http://www.w3school.com.cn/jsref/met_win_confirm.asp) : 显示带有一段消息以及确认按钮和取消按钮的对话框。
- [window.createPopup()](http://www.w3school.com.cn/jsref/met_win_createpopup.asp) : 创建一个 pop-up 窗口。
- [window.focus()](http://www.w3school.com.cn/jsref/met_win_focus.asp) : 把键盘焦点给予一个窗口。
- [window.moveBy()](http://www.w3school.com.cn/jsref/met_win_moveby.asp) : 可相对窗口的当前坐标把它移动指定的像素。
- [window.moveTo()](http://www.w3school.com.cn/jsref/met_win_moveto.asp) : 把窗口的左上角移动到一个指定的坐标。
- [window.open(<URL>, <窗口名称>, <参数字符串>)](http://www.w3school.com.cn/jsref/met_win_open.asp) : 打开一个新的浏览器窗口或查找一个已命名的窗口。
- [window.print()](http://www.w3school.com.cn/jsref/met_win_print.asp) : 打印当前窗口的内容。
- [window.prompt()](http://www.w3school.com.cn/jsref/met_win_prompt.asp) : 显示可提示用户输入的对话框。
- [window.resizeBy()](http://www.w3school.com.cn/jsref/met_win_resizeby.asp) : 按照指定的像素调整窗口的大小。
- [window.resizeTo()](http://www.w3school.com.cn/jsref/met_win_resizeto.asp) : 把窗口的大小调整到指定的宽度和高度。
- [window.scrollBy()](http://www.w3school.com.cn/jsref/met_win_scrollby.asp) : 按照指定的像素值来滚动内容。
- [window.scrollTo()](http://www.w3school.com.cn/jsref/met_win_scrollto.asp) : 把内容滚动到指定的坐标。
- [window.setInterval()](http://www.w3school.com.cn/jsref/met_win_setinterval.asp) : 按照指定的周期（以毫秒计）来调用函数或计算表达式。
- [window.setTimeout()](http://www.w3school.com.cn/jsref/met_win_settimeout.asp) : 在指定的毫秒数后调用函数或计算表达式。

### Navigator对象

- `navigator.plugins[]` : 返回对文档中所有嵌入式对象的引用。该集合是一个 Plugin 对象的数组，其中的元素代表浏览器已经安装的插件。
- `navigator.appCodeName` : 返回浏览器的代码名。
- `navigator.appMinorVersion` : 返回浏览器的次级版本。
- `navigator.appName` : 返回浏览器的名称。
- `navigator.appVersion` : 返回浏览器的平台和版本信息。
- `navigator.browserLanguage` : 返回当前浏览器的语言。
- `navigator.cookieEnabled` : 返回指明浏览器中是否启用 cookie 的布尔值。
- `navigator.cpuClass` : 返回浏览器系统的 CPU 等级。
- `navigator.onLine` : 返回指明系统是否处于脱机模式的布尔值。
- `navigator.platform` : 返回运行浏览器的操作系统平台。
- `navigator.systemLanguage` : 返回 OS 使用的默认语言。
- `navigator.userAgent` : 返回由客户机发送服务器的 user-agent 头部的值。
- `navigator.userLanguage` : 返回 OS 的自然语言设置。
- `navigator.javaEnabled()`	: 规定浏览器是否启用 Java。
- `navigator.taintEnabled()` :	规定浏览器是否启用数据污点 (data tainting)。

### History对象

- `history.length`	返回浏览器历史列表中的 URL 数量。
- `history.back()`	加载 history 列表中的前一个 URL。后退.
- `history.forward()`	加载 history 列表中的下一个 URL。前进.
- `history.go(number|URL)`	加载 history 列表中的某个具体页面。-1等于back.

## Reference
1. [w3school-cn-javascript教程](http://www.w3school.com.cn/js/index.asp)
2. [Codecademy-JS教程练习](http://www.codecademy.com/zh/tracks/javascript)
3. [JavaScript面向对象精要(一)](http://segmentfault.com/a/1190000002890067), [JavaScript面向对象精要(二)](http://segmentfault.com/a/1190000002896562)


---