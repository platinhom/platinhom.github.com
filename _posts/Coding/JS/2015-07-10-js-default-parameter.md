---
layout: post
title: JS不支持缺省参数
date: 2015-07-09 16:19:39
categories: Coding
tags: JS
---

# JavaScript don't support default argument

---------

Today, I add some new functions to control the radios in the webpage. I want to make the web identify the surface the user choose. But it makes some problems. The visualization part can't work finally. After half and hour toss, I found that in the new function, I used a default argument for the surface. This made it stuck! Default argument in JS maybe add in ECMAScript 6.. Maybe... So, it's not safe to use it.

`function showsurface(name, method='ESES'){....}` --> Doesn't work at all!

It shows that the default argument is not supported in many browser, including Chrome, IE, Opera, Safari. To solve this problem, we can check whether the argument has been defined. If it is undefined, we give it a value in the function.

- 1\. Ternary Operator `? :`  
To judge undefined value will give false! To use the array `arguments` to get the given arguments.

~~~javascript
function example(a,b){
	var a = arguments[0] ? arguments[0] : 1;//set default as 1
	var b = arguments[1] ? arguments[1] : 2;//set default as 2
	return a+b;
}
~~~
&nbsp;&nbsp;&nbsp;&nbsp;or  

~~~javascript
function _IsDate(a,f){ 
    var a = (typeof(arguments[0])=="undefined")?null:arguments[0]; 
    var f = (typeof(arguments[1])=="undefined")?true:arguments[1];
} 
~~~

- 2\. `If` statement

~~~javascript
function example(name,age){
	if(!name){name='James';}
	if(!age){age=30;}
	alert('Hi, I'm '+name+'，at age'+age+'.');
}
~~~

- 3\. `||` expression   
When false give the latter values.  

~~~javascript
	name=name || 'James';
	age=age || 30;
	alert('Hi, I'm '+name+'，at age'+age+'.');
}
~~~
- 4\. Use JQuery  
It's suitable when many argument need to set default values. Use the `$.extend` function.  

~~~javascript
function example(setting){
	var defaultSetting={
		name:'IfengLin',
		age:'30',
		sex:'Female',
		phone:'13611876347',
		QQ:'10086',
		birthday:'1985.3.15' 
	};
	$.extend(defaultSetting,settings);
	var message='Name: '+defaultSetting.name
	+'，Gender: '+defaultSetting.sex
	+'，Age: '+defaultSetting.age
	+'，Phone#:'+defaultSetting.phone
	+'，QQ: '+defaultSetting.QQ
	+'，Birthday: '+defaultSetting.birthday
	+'。';
	alert(message);
}
~~~

---------
