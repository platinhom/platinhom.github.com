---
layout: post
title: PHP读取POST表单数据值
date: 2015-07-02 21:10:41
categories: Coding
tags: PHP HTML Website
---

今天和组里开会和讨论. 没啥时间学啥干啥,灌篇水吧....

## `$_POST`变量

- 是一个关联数组, 索引是表单form里面成员标签的`name`属性.值就是提交后的对应value咯.  
- `$_POST`只能在form标签属性`method="POST"`时才能产生. 所以最好用`$_SERVER["REQUEST_METHOD"] == "POST"`来控制走向.  
- form标签的`action='process.php'`action属性指明了提交后处理的页面.这个页面处理一般是在服务器端完成的,指向相应的php,cgi脚本等._POST变量会被传递到该脚本页面当中.
- `F5`刷新的话,会提示重新提交表单. 这时方式还是POST,变量还存在; 但是在地址栏重新enter, 就会当作普通进入,而非表单提交.
- 提交的数据常用`$data = htmlspecialchars($data)`将特殊字符转为HTLM实体`&nbsp`这种,避免黑客利用

## 常见标签的读取和处理

- 没有定义name的任何元素都不能用_POST提取!
- `input type="text/password/hidden/range/number/date/color/email/url` 一般直接用`$_POST["name"]`来读取.
- `select option` 和`input type='radio'`也是一般直接用select的name来读取,获得的是选取项的值
- `input checkbox`要是每个选项的name都不同,那就是直接调用,要是用数组形式区分.那就数组形式处理(见下面的讲解).
- `<input type='checkbox' name='Fruit[1]' value=1><input type='checkbox' name='Fruit[2]' value=2>` 这种数组形式的时候,`$_POST["Fruit"]`获取的是个关联数组,数组里面就是被选中的项,例如有四个这样的checkbox,选中1,3项,返回值就是: `$_POST[Fruit] => Array ( [1] => 1 [3] => 3 ) `.然后再通过指定索引读取.好处是可以把checkbox归组.例如我喜欢吃的水果,那么一下子就可以知道喜欢多少种了`count($_POST[Fruit])`,而不是一个一个去循环.对于别的归组处理同样的.
- `input type=file` 一般在_post里面没有相应的值. 存在于`$_FILES`里面.不过要是加入`name=fname`就可以了.
- `input type=submit name=sm value=Submit` 用sm索取,可以获得`Submit`这个值.(旧版本如果不用value去指明,那么不存在该项.新版本即使没有value,都可以获取Submit这个串.) 当有多个form时,或者一个form有多个submit时,可以给submit的value赋不同的值,然后检查_POST里面有没有该项.
- `foreach ($_POST as $key => $value) {$kv[] = "$key=$value";}`循环出每个值

~~~ php
<!--
将POST的提交数据转为GET的字符串.
-->
<?php
$query_string = "";
if ($_POST) {
  $kv = array();
  foreach ($_POST as $key => $value) {
    $kv[] = "$key=$value";
  }
  $query_string = join("&", $kv);
}
else {
  $query_string = $_SERVER['QUERY_STRING'];
}
echo $query_string;
?>
~~~

- `input type=hidden` 其实就可以当作是一个储存变量信息被提交的控件.例如我提交时用不同的JobID,可以把JobID变量储存到hidden里,提交后就会同时被传递.但是post后才获得的值不能储存..例如上传一个文件,想储存这个文件的名字.因为名字要post后才反映出来,此时hidden的值也早已提交. 解决办法是利用JS的DOM来在客户端控制隐藏值!

##### 利用hidden属性传递变量值,包括用户交互时的值.

~~~ php
<!--
利用hidden属性传递变量值,包括用户交互时的值
-->
<html>
<body>
<?php
$JobID=uniqid("hiddentest-");
if ($_SERVER["REQUEST_METHOD"] == "POST") {
print_r($_POST);
}
?>
<!--JS script for change user provided information in hidden-->
<script>function updatefilename(){document.getElementById("hideFilename").value=document.getElementById("Givenfile").value}</script>
<form method="POST">
<!--saving var in php load for user-->
<input type="hidden" name="hideJobID" id="hideJobID" value= <?php echo "'$JobID'" ?> >
<!--saving var provided by user-->
<input type="hidden" name="hideFilename" id="hideFilename" value=''>

<input type='file' name='Givenfile' id="Givenfile" onchange="updatefilename()" />
<input type='submit' name="submit1">
</form>
</body>
</html>
~~~


## Reference
1. [PHP-POST VARS](http://www.php.net/manual/en/reserved.variables.post.php)




---
