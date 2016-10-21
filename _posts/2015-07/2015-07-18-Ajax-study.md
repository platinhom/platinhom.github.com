---
layout: post
title: AJAX学习
date: 2015-07-18 06:42:38
categories: Coding
tags: JS
---

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>

AJAX就是**异步 JavaScript 和 XML（Asynchronous JavaScript and XML）**. 简短地说，在不重载整个网页的情况下，AJAX 通过后台加载数据，并在网页上进行显示。使用XML进行数据交流, 使得数据可以按需要进行加载.

## 加载数据  
- **$(selector).load(URL,data,callback);** [.load()加载页面或元素](http://www.w3school.com.cn/jquery/ajax_load.asp)  
几乎与 *$.get(url, data, success)* 等价，不同的是它不是全局函数，并且它拥有隐式的回调函数。当侦测到成功的响应时（比如，当 textStatus 为 "success" 或 "notmodified" 时），*.load()* 将匹配元素的 HTML 内容设置为返回的数据。如果提供的*data*是对象，则使用 POST 方法；否则使用 GET 方法。由于浏览器安全方面的限制，大多数 "Ajax" 请求遵守同源策略；请求无法从不同的域、子域或协议成功地取回数据。
	1. url	规定要将请求发送到哪个 URL。后面可以跟空格加jquery的selector.如:*"ajax/test.html #container"*
	1. data	可选。规定连同请求发送到服务器的数据
	1. function(response,status,xhr) 可选。规定当请求完成时运行的函数。额外的参数：
		2. response - 包含来自请求的结果数据
		2. status - 包含请求的状态（"success", "notmodified", "error", "timeout" 或 "parsererror"）
		2. xhr - 包含 XMLHttpRequest 对象
- **$(selector).get(url,data,success(response,status,xhr),dataType)** [Ajax html get方法](http://www.w3school.com.cn/jquery/ajax_get.asp)  
类似于HTML GET, 请求成功时可调用回调函数。如果需要在出错时执行函数，请使用 $.ajax。可以不加selector直接`$.get()`
	1. url	必需。规定将请求发送的哪个 URL。
	1. data	可选。规定连同请求发送到服务器的数据。如{name:"hom",age:"30"}这样,懂html-get就懂了.
	1. dataType - 可选。规定预计的服务器响应的数据类型。默认地，jQuery 将智能判断。可能的类型："xml", "html", "text", "script", "json", "jsonp"  
	1. success(response,status,xhr)	可选。规定当请求成功时运行的函数。额外的参数：  
		2. response - 包含来自请求的结果数据
		2. status - 包含请求的状态
		2. xhr - 包含 XMLHttpRequest 对象  
例如: `$.get("test.cgi", { name: "John", time: "2pm" },function(data){alert("Data Loaded: " + data);});`
- **jQuery.post(url,data,success(data, textStatus, jqXHR),dataType)** [Ajax html post方法](http://www.w3school.com.cn/jquery/ajax_post.asp)
和.get类似,使用post方法提交请求.

## 数据处理
- **$(selector).serialize()** 序列化表单数据返回字符串  
就是将表单成功submit时数据转成 *a=1&b=1* 这种get方式字符串.可以对整个form,也可以对某些标签,取决于selector.
- **$(selector).serializeArray()** 序列化表单返回jason对象.
和上类似,但返回的是jason对象,注意操作.
- **jQuery.param(object,traditional)** 将数组或对象字符串化  
可以将数组/对象字符串化成get请求那种字符串.第二参数规定是否使用传统的方式浅层进行序列化（参数序列化）,默认false.

## 请求完成处理
如**.ajaxError()**

jQuery.ajax()	|  执行异步 HTTP (Ajax) 请求。
.ajaxComplete()	|  当 Ajax 请求完成时注册要调用的处理程序。这是一个 Ajax 事件。
.ajaxError()	|  当 Ajax 请求完成且出现错误时注册要调用的处理程序。这是一个 Ajax 事件。
.ajaxSend()	|  在 Ajax 请求发送之前显示一条消息。
jQuery.ajaxSetup()	|  设置将来的 Ajax 请求的默认值。
.ajaxStart()	|  当首个 Ajax 请求完成开始时注册要调用的处理程序。这是一个 Ajax 事件。
.ajaxStop()	|  当所有 Ajax 请求完成时注册要调用的处理程序。这是一个 Ajax 事件。
.ajaxSuccess()	|  当 Ajax 请求成功完成时显示一条消息。
jQuery.get()	|  使用 HTTP GET 请求从服务器加载数据。
jQuery.getJSON()	|  使用 HTTP GET 请求从服务器加载 JSON 编码数据。
jQuery.getScript()	|  使用 HTTP GET 请求从服务器加载 JavaScript 文件，然后执行该文件。
.load()	|  从服务器加载数据，然后把返回到 HTML 放入匹配元素。
jQuery.param()	|  创建数组或对象的序列化表示，适合在 URL 查询字符串或 Ajax 请求中使用。
jQuery.post()	|  使用 HTTP POST 请求从服务器加载数据。
.serialize()	|  将表单内容序列化为字符串。
.serializeArray()	|  序列化表单元素，返回 JSON 数据结构数据。


##### An example to get pdb information online and show it

~~~html
<input type="button" value="1: Get PDB" id="getpdb"> <input type="text" value="1AJJ" id="pdbnum">
<p id="showpdb"></p>
<script>
$(document).ready(function(){
	$("#getpdb").click(function(){
		var pdbnum=$("#pdbnum").val();
		$.get("http://www.rcsb.org/pdb/files/"+pdbnum+".pdb",function(data,status){
			//alert("Data: " + data + "\nStatus: " + status);
			$("#showpdb").html(data);
		});
	});
});</script>
~~~

<input type="button" value="1: Get PDB" id="getpdb"> <input type="text" value="1AJJ" id="pdbnum">

<p id="showpdb"></p>

<script>
$(document).ready(function(){
	$("#getpdb").click(function(){
		var pdbnum=$("#pdbnum").val();
		$.get("http://www.rcsb.org/pdb/files/"+pdbnum+".pdb",function(data,status){
			//alert("Data: " + data + "\nStatus: " + status);
			$("#showpdb").html(data);
		});
	});
});</script>

## Reference
1. [Jquery-Ajax参考](http://www.w3school.com.cn/jquery/jquery_ref_ajax.asp)
2. [AJAX教程](http://www.w3school.com.cn/ajax/index.asp)

------
