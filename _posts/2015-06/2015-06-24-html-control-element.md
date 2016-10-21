---
layout: post_small
title: HTML常用控件元素的用法
date: 2015-06-23 21:11:05
categories: Coding
tags: Website HTML
---

这篇东东的工作量真TM大啊....慢慢写吧...分几篇吧...  
前篇: 经典HTML控件  
后篇: HTML5新控件  

## 表单 Form 对象
[Form](http://www.w3school.com.cn/tags/tag_form.asp) 主代码 `<form>contents</form>`  
表单是HTML块级对象, 能够包含各种对象如input类等, 用于向服务器提交数据.

## 标签 Label 对象
[Label](http://www.w3school.com.cn/tags/tag_label.asp) 主代码`<label>...</label>`  
简单的HTML表单,一般用for属性指明绑定控件,可以在用户点击标签时触发控件将焦点移动到表单.

属性事件:

- for: 指明绑定控件的id.
- formid: 指明所属的一个或多个表单.

~~~ html
<form>
<label for="email">Email</label>
<input type="text" id="email">
<label for="name">Name</label>
<input type="text" id="name">
</form>
~~~

<form><label for="email">Email</label><input type="text" id="email"><label for="name">Name</label><input type="text" id="name"></form>

## 输入框 Text 对象
[Text](http://www.w3school.com.cn/jsref/dom_obj_text.asp)主代码: `<input type="text"/>`   
一般的文件输入框. 很基础. 注意一旦`disabled=true`, POST后就没有值,对于别的空间也是.

`<form>Email: <input type="text" name="email" /></form>`

<form>Email: <input type="text" name="email" /></form>

## 多行文本输入控件 Textarea 对象
[Textarea](http://www.w3school.com.cn/tags/tag_textarea.asp)主代码: `<textarea rows="3" cols="20">预设文字</textarea>`   
多行的输入框,例如写评论.

属性和方法

- rows: 显示行数. 输入超过了就下拉
- cols: 宽度.
- height/width: 也可以控制大小.
- readonly: 只读的.
- disabled: 不可用,true/false.
- name: 名称,用于表单调用.
- required: 必须填的.HTML5.
- maxlength: 最大字符数
- form: 所属的一个或多个表单.

`<textarea rows="3" cols="20">预设文字</textarea>`  

<textarea rows="3" cols="20">预设文字</textarea>

## 密码输入框 Password 对象
[Password](http://www.w3school.com.cn/jsref/dom_obj_password.asp)主代码: `<input type="password"/>`

`<form><input type="password" name="pwd" /></form>`

<form><input type="password" name="pwd" /></form>

## 按钮 Button 对象
[Input Button](http://www.w3school.com.cn/jsref/dom_obj_button.asp)主代码: `<input type="button"/>`  
[Button](http://www.w3school.com.cn/jsref/dom_obj_pushbutton.asp)主代码:`<button>text</button>`  
最一般普通的按钮. 

常用属性和事件:

- value :
- onclick :

`<form><input type="button" value="Click me" onclick="alert('Hello World')" /></form>`

<form><input type="button" value="Click me" onclick="alert('Hello World')" /></form>

`<button onclick="alert('Hello World')"> Click me</button>`

<button onclick="alert('Hello World')"> Click me</button>


## 单选 Radio 对象
[Radio](http://www.w3school.com.cn/jsref/dom_obj_radio.asp)主代码:`<input type="radio"/>`

常用属性事件: 

- checked: 被选中. 也用来最终获取值.

~~~ html
<form action="" method="get"> 
您最喜欢水果？<br />
<label><input name="Fruit" type="radio" value="" checked/>苹果 </label> 
<label><input name="Fruit" type="radio" value="" />桃子 </label> 
<label><input name="Fruit" type="radio" value="" />香蕉 </label> 
<label><input name="Fruit" type="radio" value="" />梨 </label> 
<label><input name="Fruit" type="radio" value="" />其它 </label> 
</form> 
~~~


<form action="" method="get"> 您最喜欢水果？<br /><label><input name="Fruit" type="radio" value="" checked/>苹果 </label><label><input name="Fruit" type="radio" value="" />桃子</label> <label><input name="Fruit" type="radio" value="" />香蕉 </label> <label><input name="Fruit" type="radio" value="" />梨 </label> <label><input name="Fruit" type="radio" value="" />其它 </label> </form> 


## 多选 checkbox 对象
[Checkbox](http://www.w3school.com.cn/jsref/dom_obj_checkbox.asp) 主代码: `<input type="checkbox"/>`

常用属性事件: 

- checked: 被选中. 也用来最终获取值.

~~~ html
<form action="" method="get"> 
您喜欢的水果？<br /><br /> 
<label><input name="Fruit1" type="checkbox" value="" checked/>苹果 </label> 
<label><input name="Fruit2" type="checkbox" value="" />桃子 </label> 
<label><input name="Fruit3" type="checkbox" value="" />香蕉 </label> 
<label><input name="Fruit4" type="checkbox" value="" />梨 </label> 
</form> 
~~~

<form action="" method="get"> 您喜欢的水果？<br /><br /> <label><input name="Fruit1" type="checkbox" value="" checked/>苹果 </label> <label><input name="Fruit2" type="checkbox" value="" />桃子 </label> <label><input name="Fruit3" type="checkbox" value="" />香蕉 </label> <label><input name="Fruit4" type="checkbox" value="" />梨 </label> </form> 


## 选择器 Select对象
[Select](http://www.w3school.com.cn/jsref/dom_obj_select.asp)主代码: `<select><option value="v1">option1</option></select>`

常用属性事件: 

- add(option,before): 增加option对象,before某元素前.默认before是null,即追加最后.一般需要先`document.createElement('option')`.
- options[]: 所有的选项,使用options.length=0 可以清空,如果length<当前数目会删除最后的.

[Option](http://www.w3school.com.cn/jsref/dom_obj_option.asp) 选项对象.

常用属性事件: 

- text: 显示内容
- value: 具体值
- index: 返回索引值(下拉时位置)
- selected: 是否被选中,可以用于默认值.

~~~ html
<form>
<select id="sel">
<option value="1">1</option>
<option value="2">2</option>
<option value="3">3</option>
<option value="4">4</option>
<option value="5">5</option>
</select></form>
~~~

<form><select id="sel"><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option></select></form>

## 文件提交 FileUpload 对象
[File](http://www.w3school.com.cn/jsref/dom_obj_fileupload.asp) 主代码: `<input type="file">` 

`<form><input type="file" /></form>`

<form><input type="file" /></form>

## Image 对象
[Input Image](http://www.w3school.com.cn/jsref/dom_obj_input_image.asp) 主代码`<input type="image" />`  
[img](http://www.w3school.com.cn/jsref/dom_obj_image.asp) 主代码`<img src="" />`  

`<form><input type="image" src="http://platinhom.github.io/images/shortcut.png" alt="Submit" /></form>`

`<img src="http://platinhom.github.io/images/shortcut.png"/>`

<form><input type="image" src="http://platinhom.github.io/images/shortcut.png" alt="Submit" /></form><img src="http://platinhom.github.io/images/shortcut.png"/>


## 控件块 Fieldset 对象
[fieldset](http://www.w3school.com.cn/jsref/dom_obj_fieldset.asp) 主代码`<fieldset></fieldset>`  
相当于一个容器,可以统一操作管理内部功能.

常用属性事件:  

- disabled: 禁用,内部控件也被禁用.

~~~html
<fieldset id="myFieldset" name="personalia">
  Name: <input type="text" name="username"><br>
  Email: <input type="text" name="usermail"><br>
</fieldset>
<p>点击按钮来禁用 fieldset。</p>
<button onclick="myFunctionfieldset()">试一下</button>
<script>
function myFunctionfieldset()
{
var x = document.getElementById("myFieldset");
x.disabled = true;
}
</script>
~~~

<fieldset id="myFieldset" name="personalia">Name: <input type="text" name="username"><br>Email: <input type="text" name="usermail"><br></fieldset>点击按钮来禁用 fieldset。<button onclick="myFunctionfieldset()">试一下</button>

<script>function myFunctionfieldset(){var x = document.getElementById("myFieldset");x.disabled = true;}</script>

## Fieldset标题 Legend 对象
[Legend](http://www.w3school.com.cn/tags/tag_legend.asp) 主代码:`<legend>Caption</legend>`

~~~ html
<fieldset>
<legend>健康信息</legend>
    身高：<input type="text" />
    体重：<input type="text" />
</fieldset>
~~~

<fieldset><legend>健康信息</legend>身高：<input type="text" />体重：<input type="text" /></fieldset>


## 提交表单 Submit 对象
[submit](http://www.w3school.com.cn/jsref/dom_obj_submit.asp)主代码:`<input type="submit">`   
主要使用form的`onsubmit`属性来调用检查函数.形式其实只是个普通按钮.

~~~ html
<script type="text/javascript">
function validate()
{
var at=document.getElementById("email").value.indexOf("@")
var age=document.getElementById("age").value
var fname=document.getElementById("fname").value
submitOK="true"

if (fname.length>10)
 {
 alert("名字必须小于 10 个字符。")
 submitOK="false"
 }
if (isNaN(age)||age<1||age>100)
 {
 alert("年龄必须是 1 与 100 之间的数字。")
 submitOK="false"
 }
if (at==-1) 
 {
 alert("不是有效的电子邮件地址。")
 submitOK="false"
 }
if (submitOK=="false")
 {
 return false
 }
}
</script>

<body>
<form action="/example/hdom/hdom_submitpage.html" onsubmit="return validate()">
名字（最多 10 个字符）：<input type="text" id="fname" size="20"><br />
年龄（从 1 到 100）：<input type="text" id="age" size="20"><br />
电子邮件：<input type="text" id="email" size="20"><br />
<br />
<input type="submit" value="提交"> 
</form>
~~~

## 重置表格 Reset 对象
[Reset](http://www.w3school.com.cn/jsref/dom_obj_reset.asp) 主代码: `<input type="reset"> `

`<form><input type="reset" /></form>`

<form><input type="reset" /></form>

## 隐藏字段 Hidden 对象
[hidden](http://www.w3school.com.cn/jsref/dom_obj_hidden.asp) 主代码:`<input type="hidden">`  
一般用于储存一些不显示的信息,又可以通过JS进行操作修改,保存内容,被进一步调用等.  

`<form><input type="hidden" name="country" value="Norway" /></form>`

<form><input type="hidden" name="country" value="Norway" /></form>

## 显示细节 Details 对象
[Details](http://www.w3school.com.cn/jsref/dom_obj_details.asp) 主代码:`<details>....</details>`   
创建一个可显示详细细节的对象.

`<details id="myDetails">Some additional details...</details>`

<details id="myDetails">Some additional details...</details>


----------------
一些常用处理代码

### 可以用以下JS代码创建和访问对象

~~~ javascript
var x = document.createElement("INPUT");
x.setAttribute("type", "text");
document.body.appendChild(x);
x.setAttribute("id", "myColor");
var y = document.getElementById("myColor");
~~~

### 可以用以下JS代码访问多选栏(checkbox,radio)中被选中的值.

~~~ javascript
function GetValueFromNames(name){
	var chkObjs = document.getElementsByName(name);
    for(var i=0;i<chkObjs.length;i++){
        if(chkObjs[i].checked){
            stype=chkObjs[i].value;
            return stype;
        }
    }
}
~~~

## Reference
1. [HTML \<input\> 标签](http://www.w3school.com.cn/tags/tag_input.asp)以及[HTML \<input\> 标签的 type 属性](http://www.w3school.com.cn/tags/att_input_type.asp)
2. [HTML 标签参考手册](http://www.w3school.com.cn/tags/)

TODO: Update the property and events. More tags.

---
